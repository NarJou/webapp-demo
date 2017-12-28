import redis
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask,render_template,jsonify,json,request,redirect,url_for
## TODO add code to get product name from MongoDB and fill up Redis with it

application = Flask(__name__)

client = MongoClient('mongo:27017')
db = client.test.products

r = redis.StrictRedis(host="redis", port=6379, db=0)

def getProduct(key):
    try:
        productObject = db.find_one({'name':key})
        productDict = {
                'name':productObject['name'],
                'model':productObject['model'],
                'sku':productObject['sku'],
                'type':productObject['type'],
                'price':productObject['price']
                }
        return productDict
    except Exception, e:
        return str(e)

@application.route('/search/<query>', defaults={'page': 1}, methods=['GET', 'POST'])
@application.route('/search', methods=['GET', 'POST'])
def search(page,query): #FIXME
    if request.method != 'POST':
        if query:
            result = []
            results = {"results": result.append({"name":i}) for i in autocomplete(query)}
            results = {"results": result}
            return jsonify(results)
    else:
        return redirect(url_for('showProduct', product_name=query))
    #return jsonify({'results':[{'name': query},{'name': query}]})

#@application.route('/search', methods=['GET', 'POST'])
#def search(): #FIXME
#    if request.method != 'POST':
#        return redirect(url_for('showProduct'))
#
#    query = request.form.get('query', None)
#    print "SEARCH_QUERY-->"+query
#    if query:
#        return redirect(url_for('search_results', query=query))
#    else:
#        return redirect(url_for('showProduct'))

def autocomplete(query):
    print "SEARCH_RESULTS_QUERY-->"+query
    count = 50
    results = []
    rangelen = 50 # This is not random, try to get replies < MTU size
    start = r.zrank('names',query)
    print "ZRANK -->"
    print start
    if start is None:
        return []
    while (len(results) != count):
        range = r.zrange('names',start,start+rangelen-1)
        start += rangelen
        if not range or len(range) == 0:
            break
        for entry in range:
            minlen = min(len(entry),len(query))
            if entry[0:minlen] != query[0:minlen]:
                count = len(results)
                break
            if entry[-1] == "*" and len(results) != count:
                results.append(entry[0:-1])
    return results

#TODO
# /!\ catch the case where string query (prefix) do not exist on redis
@application.route('/product/<query>', defaults={'page': 1})
@application.route('/product/<query>/page-<int:page>')
def search_results(page,query): #FIXME
    results = autocomplete(query)
    STR = "Directed Electronics - Viper Audio Glass Break Sensor"
    product = getProduct(STR) #FIXME
    return render_template('index.html', product=product, results=results)


@application.route('/show/<product_name>', methods=['GET', 'POST'])
def showProduct(product_name):
    product = getProduct(product_name)
    import sys # FIXME
    print >> sys.stderr, product #FIXME
    return render_template('index.html', product=product)


@application.route('/', methods=['GET', 'POST'])
def index():
    STR = "" #FIXME
    return render_template('index.html', product=STR)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
