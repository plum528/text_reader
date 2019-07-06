import bottle
from bottle import Bottle, run, static_file, template

bottle.TEMPLATE_PATH.append('./webroot/views')

app = Bottle()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./webroot/static')

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/')
@app.route('/index')
def index():
    return static_file('index.html', root = './webroot/views')

@app.route('/load')
def load():
    return ['123','234']

run(app, host='localhost', port=8080, debug=True)