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

@app.route('/:username', methods=['GET', 'POST', 'DELETE'])
def read_user():
    if(request.method == 'GET'):
        return {'route': '/:username', 'method': 'get'}
    elif( request.method == 'POST' ):
        return {'route': '/:username', 'method': 'post'}
    else:
        return {'route': '/:username', 'method': 'delete'}

@app.route('/:username/update', methods=['PUT', 'PATCH'])
def update_user():
    if(request.method == 'PUT'):
        return {'route': '/:username/update', 'method': 'put'}
    else:
        return {'route': '/:username/update', 'method': 'patch'}

@app.route('/:username/date/:date', methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def read_journal():
    if(request.method == 'GET'):
        return {'route': '/:username/date/:date', 'method': 'get'}
    elif( request.method == 'DELETE' ):
        return {'route': '/:username/date/:date', 'method': 'delete'}
    elif( request.method == 'PUT' ):
        return {'route': '/:username/date/:date', 'method': 'put'}
    else:
        return {'route': '/:username/date/:date', 'method': 'patch'}
