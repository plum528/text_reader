import random
import uuid
import linecache
import bottle
from bottle import Bottle, run, static_file, template
from bottle import request
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
    create_test_file()
    return static_file('index.html', root = './webroot/views')

@app.route('/load/<keyword>')
def load(keyword):
    print(keyword)
    line_number = get_line_number_matched(keyword)
    print('line_number:', line_number)
    #f = open('./text_file.txt', 'r')
    content = []
    content.append(linecache.getline('./text_file.txt', line_number))
    
    return content

def get_line_number_matched(keyword):
    f = open('./text_file.txt', 'r')
    try:
        for line, text in enumerate(f, 1):
            if keyword in text :
                return line
        return -1
    finally:
        f.close()

def create_test_file():
    name_line = random.randint(0, 10000)
    f = open('text_file.txt', 'w')
    for line in range(10000):
        f.write(str(uuid.uuid4())+'\n')
        if(name_line == line):
            f.write('李明杰\n')
    f.close()

run(app, host='localhost', port=8080, debug=True)