import os
import json
import pymongo
from flask import Flask
from flask import request
from bson.objectid import ObjectId
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://Godlin_hilda:1234@cluster0.mvqfv.mongodb.net/test?retryWrites=true&w=majority")
db = client['test']
collection = db['test']
@app.route("/", methods=['POST'])
def insert_document():
    req_data = request.get_json()
    collection.insert_one(req_data).inserted_id
    return ('', 204)
@app.route('/')
def get():
    documents = collection.find()
    response = []
    for document in documents:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
@app.route("/",methods=['DELETE'])
def delete():
    collection.remove({})
    return ("",204)
    
if __name__ == '__main__':
    app.debug=True
    app.run()