import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    env1 = os.getenv('HOME')
    env2 = os.getenv('X')
    return f"Hello, World!<ul>{env1}</ul><ul>{env2}</ul>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
