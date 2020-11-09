from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'DELETE'])
def read_root():
    if( request.method == 'GET' ):
        return {'route': '/', 'method': 'get'}
    elif( request.method == 'POST' ):
        return {'route': '/', 'method': 'post'}
    else:
        return {'route': '/', 'method': 'delete'}

@app.route('/user/<username>', methods=['GET', 'POST', 'DELETE'])
def read_user(username):
    if(request.method == 'GET'):
        if('id' in request.args):
            request_date = request.args['id']
            return {'id': str(request_date)}
        else:
            return {'route': '/:username', 'method': 'get'}
    elif( request.method == 'POST' ):
        if ('id' not in request.args):
            return {'route': '/:username', 'method': 'post'}
    elif( request.method == 'DELETE' ):
        if('id' in request.args):
            request_date = request.args['id']
            return {'id': str(request_date)}
        else:
            return {'route': '/:username', 'method': 'delete'}
    elif( request.method == 'PUT' ):
        if('id' in request.args):
            return {'function': 'update a journal'}
    elif(request.method == 'PATCH'):
        if('id' in request.args):
            return {'function': 'update a journal - patch'}


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
