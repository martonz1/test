import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask

load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route('/')
def hello_world():
    env1 = os.getenv('HOME')
    env2 = os.getenv('X')

    crt_dir = os.path.abspath(os.getcwd())
    with open(crt_dir + "index.html", "r", encoding="utf-8") as f:
        return f.read()
    # return f"Hello, aaa!<ul>{env1}</ul><ul>{env2}</ul>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
