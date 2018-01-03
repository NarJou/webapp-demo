# Imports the Google Cloud client library
from google.cloud import datastore
import json

# If you don't specify credentials when constructing the client, the
# client library will look for credentials in the environment.

def main():

    # The kind for the new entity
    kind = 'Catalogue'
    project_id = 'test-gcp-178420'

    # Instantiates a client
    client = datastore.Client(project_id)
    key = client.key(kind)

    with open('products.json', 'r') as f:
        products = json.load(f)

    for product in products:
        entity = datastore.Entity(key=key)
        entity.update(product)
        client.put(entity)

    #update_entity(basic_entity(get_incomplete_key(client, kind)), get_file())
#    query = client.query(kind=kind)

#    for enti in query.fetch():
#        print enti['name']

if __name__ == '__main__':
    main()
