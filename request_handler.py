import json
import sqlite3
import uuid
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
    # get needed data from the database
    listing = db_execute(f"SELECT * FROM tbItems WHERE itemID = {data["listing_id"]}", 1)
    seller = db_execute(f"SELECT Name FROM tbAccounts WHERE accID={listings[i][1]}",1)
    # fill in return data
    return_data = {
        "type" : "get_listing",
        "data" : {
            "id" : listings[0][0],
            "seller_id" : listings[0][1],
            "seller_name" : seller[0][0],
            "item" : listings[0][2],
            "price": listings[0][3],
            "quantity" : listings[0][4],
            "campus" : listings[0][5],
            "image_data" : listings[0][5],
            "description" : listings[0][6],
            "listing_date" : listings[0][7],
            "tags" : listings[0][8],
            "sold" : listings[0][9]
        }
    },
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
            "contact" : account_data[0][6]
        }
    }
    return_data = json.dumps(return_data)
    return(return_data) 

def create_account(data):
    # setup sql statement to find most recent accID used
    statement = f"SELECT accID FROM tbAccounts SORT descending"
    account_data = db_execute(statement, 1)
    return_data = {
        "type" : "create_account",
        "data" : {
            "error" : 0,
            "accID" : account_data[0][0],
            "name" : account_data[0][1],
            "course": account_data[0][2],
            "campus" : account_data[0][3],
            "pfp_data" : account_data[0][4],
            "sales" : 0,
            "contact" : account_data[0][6]
        }
    }
    return_data = json.dumps(return_data)
    return(return_data) 

def create_listing(data)

#
# TO DO
#
def login(data):

    # get password from DB form the account name given
    password = db_execute(f"SELECT password FROM tbAccounts WHERE userName={data["name"]}", 1)[0]
    # if the password is correct send a validation key (for some requests this is used to prove the user is logged in)
    if (hash(decrypt(data["password"])) == password[0]):
        # create a validation key
        key = uuid.uuid4()
        return_data = {
            "type" : "login",
            "data" : {
                "success" : True,
                "key" : key
            }
        }
    # save the key to the account DB

    return_data = json.dumps(return_data)
    return(return_data) 

def search(data):
    # setup return data
    return_data = {
        "type" : "search",
        "data" : []
    }

    # setup the sql statement
    statement = f"SELECT * FROM tbItems WHERE name LIKE '%{data["search_term"]}%' AND itemID>{data["last_loaded"]}"
    filters = data["filters"]
    # if there are filters
    if len(filters) != 0:
        # add them to the sql statement
        for i in filter:
            statement+=f"AND {i}"

    # retrieve data from the database about listings
    listings = db_execute(statement, data["to_load"])
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

#example
def n(data):
    #some sql stuff
    return_data = {
        "type" : "ping",
        "data" : ""
    }
    return_data = json.dumps(return_data)
    return(return_data) 
