import time
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f"""
    <html>
        <head>
            <title>Counter App</title>
            <style>
                body {{
                    background-color: white;
                    text-align: center;
                    font-family: Arial, sans-serif;
                }}
            </style>
        </head>
        <body>
            <h1>What's up Homie!</h1>
            <p>You've visited me {count} times.</p>
        </body>
    </html>
    """

# Runs a blocking process to not exit
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
