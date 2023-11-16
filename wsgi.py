import os
import pymongo
import json
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello Saurabh!"

if __name__ == "__main__":
    application.run()
