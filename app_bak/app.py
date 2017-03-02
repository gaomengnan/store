# -*- coding:utf-8-*-
from flask import Flask,render_template
import json
application = Flask(__name__)
@application.route("/")
def index():
    return render_template("index.html")
@application.route("/main")
def main():
    return render_template('main.html')
if __name__ == "__main__":
    application.run(host='0.0.0.0')
