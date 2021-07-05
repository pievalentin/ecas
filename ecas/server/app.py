import random
import re
import time
from datetime import datetime

import click
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@click.command(name='run_web_server')
def run():
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=True)
