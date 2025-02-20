import json
import sqlite3

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