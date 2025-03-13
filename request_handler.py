import json
import sqlite3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

# encrypt important data before its sent with the public key sent with a login request
def encrypt(msg, key):
    # the 'key' variable is the public key fo the client that was sent int the request
    public_key = serialization.load_pem_public_key(key,backend=default_backend())

    # encrypt the data being sent back
    msg = public_key.encrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    return msg

# decrypt important data that was encrypted with /keys/public_key
def decrypt(msg):
    # get private key from file 
    file = open("keys/private_key.pem", "rb")
    private_key = serialization.load_pem_private_key(file.read(),password=None,backend=default_backend())
    file.close()

    # decrypt the data
    msg = private_key.decrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    return msg

# execute a command to the database
def db_execute(statement, return_num):
    print(statement)
    # open the database
    db = sqlite3.connect("test.db") # 'test.db' to be changed later
    # execute the sql statement given
    db_cursor = db.cursor()
    db_cursor.execute(statement)
    print(db_cursor.fetchall)
    # if the command returns data
    if (return_num != 0):
        print("getting items")
        # read the amount of entries needed
        data = db_cursor.fetchmany(return_num)
        print(data)
        # close the database and return the data
        db.commit()
        db.close()
        return data
    # close the database
    db.commit()
    db.close()
'''
basic example to copy and paste
def n(data):
    some sql stuff
    return_data = {
        "type" : "ping",
        "data" : ""
    }
    return_data = json.dumps(return_data)
    return(return_data) 
'''

def ping(data):
    return_data = {
        "type" : "ping"
    }
    return_data = json.dumps(return_data)
    return(return_data)

def request_public_key(data):
    key = open("keys/private_key.pem", "rb")
    public_key = serialization.load_pem_public_key(key,backend=default_backend())
    return_data = {
        "type" : "request_public_key",
        "data" : {
            "key" : public_key
        }
    }
    return_data = json.dumps(return_data)
    return(return_data)

def get_listing(data):
    seller = null # some sql stuff
    item = null
    price = null
    campus = null
    image_data = null
    listing_date = null
    return_data = {
        "type" : "get_listing",
        "data" : {
            "seller" : seller,
            "item" : item,
            "price": price,
            "campus" : campus,
            "image_data" : image_data,
            "listing_date" : listing_date
        }
    }
    return_data = json.dumps(return_data)
    return(return_data) 

def get_account(data):
    # setup sql statement
    statement = f"SELECT * FROM tbAccounts WHERE accID = {data["accID"]}"
    account_data = db_execute(statement, 1)
    return_data = {
        "type" : "get_account",
        "data" : {
            "accID" : account_data[0][0],
            "name" : account_data[0][1],
            "course": account_data[0][2],
            "campus" : account_data[0][3],
            "pfp_data" : account_data[0][4],
            "sales" : account_data[0][5],
            "contact" : account_data[0][6],
        }
    }
    return_data = json.dumps(return_data)
    return(return_data) 


def login(data):
    #some sql stuff
    return_data = {
        "type" : "login",
        "data" : ""
    }
    return_data = json.dumps(return_data)
    return(return_data) 

def search(data):
    # setup return data
    return_data = {
        "type" : "search",
        "data" : []
    }

    # setup the sql statement
    statement = f"SELECT * FROM tbItems WHERE itemID>{data["last_loaded"]}"
    filters = data["filters"]
    # if there are filters
    if len(filters) != 0:
        # add them to the sql statement
        for i in filter:
            statement+=f"AND {i}"

    # retrieve data from the database about listings
    listings = db_execute(statement, data["to_load"]+1) # +1 to account for 'fetchmany' starting at 1
    # fill in the "data" area of the return statement with listings retrieved from the database

    for i in range(0,data["to_load"]):
        # get seller name from the seller ID
        seller = db_execute(f"SELECT Name FROM tbAccounts WHERE accID={listings[i][1]}",1)
        # fill in listing data into a dictionary
        listing_data = {
                "id" : listings[i][0],
                "seller_id" : listings[i][1],
                "seller_name" : seller[0][0],
                "item" : listings[i][2],
                "price": listings[i][3],
                "quantity" : listings[i][4],
                "campus" : listings[i][5],
                "image_data" : listings[i][5],
                "description" : listings[i][6],
                "listing_date" : listings[i][7],
                "tags" : listings[i][8],
                "sold" : listings[i][9]
            },
        # add listing to the return data
        return_data["data"].append(listing_data)
    # convert return data into json and return it
    return_data = json.dumps(return_data)
    return(return_data) 

def n(data):
    #some sql stuff
    return_data = {
        "type" : "ping",
        "data" : ""
    }
    return_data = json.dumps(return_data)
    return(return_data) 
