import redis
import json

r = redis.StrictRedis(host="redis", port=6379, db=0)

# par simplificite, on part sur le fichier de noms de femme
# car pr les noms de produits il faut d'abord utiliser un genre de process EMR
# afin d'avoir des noms faciles a traiter
# (car il ny a aucune coherence dans les noms et cela ne facilite pas linsertion dans redis ni la recuperation de linfo)

print "Loading entries in the Redis DB\n"
with open('ten-products.json',"r") as f:
    products = json.load(f)
    for product in products:
        n = product["name"]
        for c in range(1,len(n)):
            prefix = n[0:c]
            r.zadd('names',0,prefix)
        r.zadd('names',0,n+"*")

## With female name file
#print "Loading entries in the Redis DB\n"
#with open('female-names-2.txt',"r") as f:
#    for line in f:
#        n = line.strip()
#        for l in range(len(n)):
#            prefix = n[0:l+1]
#            r.zadd('names',0,prefix)
#        r.zadd('names',0,n+"*")

