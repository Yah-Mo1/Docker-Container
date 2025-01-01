from flask import Flask
from redis import Redis 

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def home():
    return "Hello, Welcome to Flask!"

@app.route("/count")
def count():
    # Increment count by one each time the user refreshes the page
    counter = redis.incr("hits")
    return counter 

    # redis.incr('page_count')
    # return "This page has been viewed {} times".format(redis.get('page_count').decode('utf-8'))

@app.route("/hello")
def hello():
    return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
