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
receive
```
{
    "type" : login
    "data" : {     <-- data should be all encrypted
        "name" : "",
        "password" : ""
    }
}
```
### create account
receive
```
{
    "type" : "create_account",
    "data" : { <-- encrypted
        "name" : ,
        "course": ,
        "campus" : ,
        "pfp_data" : ,
        "contact" : 
        "password" : 
    }
}
```
return
```
{
    "type" : "create_account",
    "data" : {
        "error" : 0-1, <-- 0/1 if there was a problem
        "accID" : ,
        "name" : ,
        "course": ,
        "campus" : ,
        "pfp_data" : ,
        "sales" : 0,
        "contact" : 
    }
}
```
### delete account

### get account

return
```
{
    "type" : "get_account",
    "data" : {
        "error" : 0-1, <-- 0/1 if there was a problem
        "accID" : ,
        "name" : ,
        "course": ,
        "campus" : ,
        "pfp_data" : ,
        "sales" : 0,
        "contact" : 
    }
}
```
### create listing

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
