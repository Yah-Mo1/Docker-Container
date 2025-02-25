from flask import Flask, render_template_string
from redis import Redis 
import os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis = Redis(host=redis_host, port=redis_port)

# Template for rendering a more appealing UI
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Redis Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: #fff;
            padding: 2rem 3rem;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
            width: 100%;
            max-width: 400px;
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 1.2rem;
            color: #555;
        }
        .button {
            margin-top: 1rem;
            padding: 0.6rem 1.2rem;
            font-size: 1rem;
            color: #fff;
            background-color: #007bff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>{{ title }}</h1>
        <p>{{ message }}</p>
        {% if show_button %}
            <a href="{{ button_link }}" class="button">{{ button_text }}</a>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template,
                                  title="Welcome to Flask!",
                                  message="Hello, welcome to the Flask application!",
                                  show_button=True,
                                  button_link="/count",
                                  button_text="View Counter")

@app.route("/count")
def count():
    counter = redis.incr("hits")
    return render_template_string(template,
                                  title="Page Counter",
                                  message=f"This page has been visited {counter} times.",
                                  show_button=True,
                                  button_link="/",
                                  button_text="Go Home")

@app.route("/hello")
def hello():
    return render_template_string(template,
                                  title="Hello World!",
                                  message="Hello, World!",
                                  show_button=True,
                                  button_link="/",
                                  button_text="Go Home")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
