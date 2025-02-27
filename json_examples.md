## base layout
{
    "type" : "request type",
    "data" : "data for the request, e.g. search terms, auth token, or username and password"
}

### ping
receive and return
```
{
    "type" : "ping"
}
```
### get listing
receive
```
{
    "type" : "get_listing",
    "data" : {
        "listing_id" : "", <- the database id for the listing
    }
}
```
return
```
{
        "type" : "get_listing",
        "data" : {
            "seller" : "seller",
            "item" : "item",
            "price": 0,
            "campus" : "",
            "image_data" : image_data,
            "listing_date" : yyyy-MM-dd HH:mm:ss,
            "tags" : ["tag1", "tag2"],
            "sold" : False
        }
    }
```

### search
receive
```
{
    "type" : "search",
    "data" : {
        "search_term" : "", <- the term used to search the database
        "to_load" : 5, <- the number of items to return
        "loaded" : , <- the id of the last loaded item
        "filters" : ["tag:tag1", "tag:tag2", "after:yyyy-MM-dd HH:mm:ss"] <- a list of filters like tags dates, etc
    }
}
```
return
```
{
    "type" : "search",
    "data" : {
        "search_term" : "", <- the term used to search the database
        "to_load" : 5, <- the number of items to return
        "loaded" : , <- the id of the last loaded item
        "tags" : ["tag1", "tag2"] <- a list of tags to search for
    }
}
```

