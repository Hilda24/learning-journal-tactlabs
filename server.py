import os
import json
import pymongo
from datetime import datetime
from bson.objectid import ObjectId
from flask import Flask, request
app = Flask(__name__)

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')

client = pymongo.MongoClient("mongodb+srv://"+db_user+":"+db_password+"@cluster0.mvqfv.mongodb.net/test?retryWrites=true&w=majority")
# client = pymongo.MongoClient('mongodb://localhost:27017/studentDB')
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
''' -----------------------------------------------------
# GET 
# /user/<username>
# get all journals or a specific journal with id for <username>
'''
@app.route('/user/<username>', methods=['GET'])
def read_user(username):
    if('id' in request.args):
        # request for specific journal
        request_id = request.args['id']
        print(request_id)
        journal = collection.find_one({"_id": ObjectId(request_id)})
        journal['_id'] = str(journal['_id'])
        return journal
    else:
        #request for specific user      
        users = collection.find({ "user": username}) 
        response = []                                 
        for user in users:   
            user['_id'] = str(user['_id']) #ObjectId to str 
            response.append(user)     
        return json.dumps(response)  

''' ------------------------------------------------------
# POST 
# /user/<username>
# create a new journal for the <username>
'''
@app.route('/user/<username>', methods=['POST'])
def create_journal(username):
    #get json data
    json_data = request.get_json()

    #add user name and date created
    json_data['user'] = username
    json_data['date'] = str( datetime.now().strftime('%A, %d %b %Y') )

    #insert document and return id
    new_journal_id = collection.insert_one(json_data).inserted_id
    
    return {'journal created': str(new_journal_id)}


''' ----------------------------------------------
# DELETE 
# /user/<username>
# Delete all journals for the <username>
'''
@app.route('/user/<username>', methods=['DELETE'])
def delete_journals(username):
    #delete journals with user = <username>
    result = collection.delete_many({"user": username}).deleted_count
    #return delete count
    return {'no of journals deleted': str(result)}


# @app.route('/user/<username>', methods=['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
# def read_user(username):
#     if(request.method == 'GET'):
#         if('id' in request.args):
#             request_date = request.args['id']
#             return {'id': str(request_date)}
#         else:
#             return {'route': '/:username', 'method': 'get'}
#     elif( request.method == 'POST' ):
#         if ('id' not in request.args):
#             return {'route': '/:username', 'method': 'post'}
#     elif( request.method == 'DELETE' ):
#         if('id' in request.args):
#             request_date = request.args['id']
#             return {'id': str(request_date)}
#         else:
#             return {'route': '/:username', 'method': 'delete'}
#     elif( request.method == 'PUT' ):
#         if('id' in request.args):
#             return {'function': 'update a journal'}
#     elif(request.method == 'PATCH'):
#         if('id' in request.args):
#             return {'function': 'update a journal - patch'}


# @app.route('/user/<username>/update', methods=['PUT', 'PATCH'])
# def update_user(username):
#     if(request.method == 'PUT'):
#         return {'route': '/:username/update', 'method': 'put'}
#     else:
#         return {'route': '/:username/update', 'method': 'patch'}


# @app.route('/user/<username>', methods=['GET', 'DELETE', 'PUT', 'PATCH'])
# def read_journal(username, date):
#     if(request.method == 'GET'):
#         return {'route': '/:username/date/:date', 'method': 'get'}
#     elif( request.method == 'DELETE' ):
#         return {'route': '/:username/date/:date', 'method': 'delete'}
#     elif( request.method == 'PUT' ):
#         return {'route': '/:username/date/:date', 'method': 'put'}
#     else:
#         return {'route': '/:username/date/:date', 'method': 'patch'}
