import redis
import json

r = redis.StrictRedis(host="redis", port=6379, db=0)

## All elements are stored with a score of Zero
## So by default all elements will be ordered lexicographically by redis when using sorted set

print "Loading entries in the Redis DB\n"
with open('30-products.json',"r") as f:
    products = json.load(f)
    for product in products:
        n = product["name"]
        for c in range(1,len(n)):
            prefix = n[0:c]
            r.zadd('names',0,prefix)
        r.zadd('names',0,n+"*")
