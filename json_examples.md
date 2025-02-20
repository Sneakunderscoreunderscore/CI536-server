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
            "seller" : seller,
            "item" : item,
            "price": price,
            "campus" : campus,
            "image_data" : image_data,
            "listing_date" : listing_date
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
        "loaded" : 5 <- the number of items the client already has
    }
}
```

