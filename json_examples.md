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

### search
receive
```
{
    "type" : "search",
    "data" : {
        "search_term" : "", <- the term used to search the database
        "to_load" : 5, <- the number of items to retune
        "loaded" : 5 <- the number of items the client already has
    }
}
```

