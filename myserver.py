import mysql.connector
import socket
import threading
import pickle
from datetime import datetime

# create database connection
db = mysql.connector.connect(
user='root',
password='code9643',
host='127.0.0.1',
database='db',
auth_plugin='mysql_native_password'
)
# store cursor
mycursor = db.cursor()

# setup server address
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 9000
ADDR = (SERVER, PORT)
BYTES = 1024
#define format to be used for transmission
FORMAT = 'utf-8'
# message to be sent to cleanly disconnect from server
DISCONNECTOR = "!DISCONNECT"

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
# bind address to socket
server.bind(ADDR)

# function to manage connections
def connection_handler(conn, addr):
    connected = True
    # fetch ids and quantity of items
    index = fetch_db_stck()
    receipt = {}
    while connected:
        data = ''
        try:
            data = conn.recv(BYTES).decode(FORMAT)
            print(data)
        except OSError:
            pass

        # check received signals
        if data == DISCONNECTOR:
            # cleanly disconnect user
            connected = False
            now = datetime.now().strftime("%H:%M:%S")
            print(f">>>>>> {now} : {addr} has successfully disconnected")
            conn.close()
        # catch signal to restock
        elif data == "#####":
            restock()
            conn.send("restocked successfully".encode(FORMAT))
        # process order
        elif '#' in data:
            id, qty = data.split("#")
            id = int(id)
            qty = int(qty)

            # check if item exists
            if id not in index.keys():
                conn.send('Invalid ID'.encode(FORMAT))
            elif id in index.keys() :
                index = fetch_db_stck()
                # check if stock is available
                if (index[id] - qty) > 0 :
                    createrecpt(id, receipt, qty)
                    conn.send('it guuuuuuuuuuuuuud'.encode(FORMAT))
                else:
                    conn.send('Item not available in desired quantity'.encode(FORMAT))

        elif data == 'stock':
            # fetch name and quantity of items
            conn.send(stck())

        elif data == 'payout':
            # send receipt its client
            conn.send(pickle.dumps(receipt))
            update_db(receipt)
        else:
            conn.send('Please use format: ID#Quantity'.encode(FORMAT))

# function to replenish stock of vending machine
def restock():
    mycursor.execute("UPDATE Stock SET stock = 30 WHERE NOT stock = 30")
    db.commit()

# function to update database after items have been purchased
def update_db(receipt):
    dct = fetch_db_stck()
    for key in receipt:
        mycursor.execute(f"UPDATE Stock  SET stock = (stock - {receipt[key][2]}) WHERE id = {key}")
    db.commit()

# function to create receipt
def createrecpt(id, receipt, qty):
    if id not in receipt.keys():
        x = fetch_name_price()
        choice = x[id]
        choice.append(qty)
        receipt[id] = choice

    else:
        receipt[id][2] += qty

# starting point of server
def start():
    server.listen()
    print("[SERVER IS NOW LISTENING]\n")
    while True:
        # split socket and address
        conn, addr = server.accept()
        now = datetime.now().strftime("%H:%M:%S")
        print(f">>>>>> {now} : {addr} has successfully connected")
        # create new thread for the user that has just connected
        thread = threading.Thread(target=connection_handler, args=(conn, addr))
        thread.start()

# function to delete database
# def drop():
#     mycursor.execute("DROP TABLE Stock")
#
# function to create database
# def create():
#     # create table
#     mycursor.execute("CREATE TABLE Stock (id smallint unsigned PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(20) , stock smallint UNSIGNED, price smallint UNSIGNED)")

# function to populate database
# def pop(name, qty, price):
#     # populate table
#     a = (name, qty, price)
#     mycursor.execute("INSERT INTO Stock (name, stock, price) VALUES (%s, %s, %s)", a)
#     db.commit()


# function to fetch is, current stock from database
def fetch_db_stck():
    mycursor.execute("SELECT id, stock FROM Stock")
    dct = {}
    for row in mycursor:
        dct[row[0]] = row[1]
    return dct

# function to fetch id, name and price of items in the database
def fetch_name_price():
    temp={}
    mycursor.execute("SELECT id, name, price FROM Stock")
    for row in mycursor:
        temp[row[0]] = [row[1], row[2]]
    return temp

# function to fetch name and stock of items in database
def stck():
    buffer=[]
    mycursor.execute("SELECT name, stock FROM Stock ")
    for item in mycursor:
        buffer.append(item)
    return pickle.dumps(buffer)


if __name__ == '__main__':
    start()

    # drop()
    # create()
    # mycursor.execute("SELECT id FROM Stock")
    # pop("coke", 30, 30)
    # pop("fanta", 30, 30)
    # pop("dahi", 30, 10)
    # pop("caprisun", 30, 30)
    # pop("twix", 30, 35)
    # pop("kitkat", 30, 25)
    # pop("sando", 30, 8)
    # pop("sprite", 30, 30)
    # pop("oreo", 30, 20)
