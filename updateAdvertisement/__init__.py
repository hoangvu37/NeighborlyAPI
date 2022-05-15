from json import dumps
from unittest import result
import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')
    request = req.get_json()
    print(id)
    if request:
        try:
            url = "mongodb://cosmosdbaccount123:GScsB8MZLpl9GfxXqGslHc60i3AxDBhlP1mmnO1SmAsF94lu6A5j1vrAGtosj3gmJ4ZbZQ6NJ8LyGQcG6vYlRQ==@cosmosdbaccount123.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbaccount123@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['MongoDB']
            collection = database['advertisements']
            # result = collection.find({})

            # Updating fan quantity form 10 to 25.
            filter = { '_id': id }
            
            # Values to be updated.
            newvalues = { "$set": request }
            collection.update_one(filter, newvalues)

            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

