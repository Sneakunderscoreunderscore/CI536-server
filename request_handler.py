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

    # decrypt the datta
    msg = private_key.decrypt(msg,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
    return msg
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

def login(data):

    return(return_data)