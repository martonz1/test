"""
This is the entry point for web server, built with Flash.
"""

import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, render_template

load_dotenv(find_dotenv())

app = Flask(__name__)


@app.route('/')
def home():
    """
    The method when landing on the top page.
    """
    _ = os.getenv('X') # X variable is pass from Docply, placeholder.
    return render_template("index.html")

@app.route('/subpages/<name>')
def subpages(name):
    """
    The method when landing on the subpages.
    """
    return render_template(f"{name}")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
