import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = os.environ["MyDbConnection"] or "mongodb://cosmosdbaccount123:GScsB8MZLpl9GfxXqGslHc60i3AxDBhlP1mmnO1SmAsF94lu6A5j1vrAGtosj3gmJ4ZbZQ6NJ8LyGQcG6vYlRQ==@cosmosdbaccount123.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosdbaccount123@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['MongoDB']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

