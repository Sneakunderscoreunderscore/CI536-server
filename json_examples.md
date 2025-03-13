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
### login
### create account
### delete account
### change password
### change name
### get account
### get contact
### create listing
### edit listing
### remove listing
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
        "search_term" : "",
        "to_load" : 5,
        "loaded" : 0,
        "filters" : ["campus=city", "price<1000", "yyyy-MM-dd HH:mm:ss"]
    }
}
```
return
```
{
    "type" : "search",
    "data" : {
        "search_term" : "",
        "to_load" : 5,
        "loaded" : ,
        "tags" : ["tag1", "tag2"]
    }
}
```
