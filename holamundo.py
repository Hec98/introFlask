from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
    return 'Hello World'

@app.route('/post/<int:post_id>')
def lala(post_id):
    # return 'The post id is ' + str(post_id)
    return f'The post id is {post_id}'
