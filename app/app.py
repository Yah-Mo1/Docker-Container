from flask import Flask
from redis import Redis 
import os
app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

redis = Redis(host=redis_host, port=redis_port)

@app.route('/')
def home():
    return "Hello, Welcome to Flask!"

@app.route("/count")
def count():
    counter = redis.incr("hits")
    return f"Hello, this is the counter: ${counter}" 

@app.route("/hello")
def hello():
    return "Hello world"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
