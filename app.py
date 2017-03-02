# -*- coding:utf-8-*-
from flask import Flask,render_template
from http import bannerController
import json
application = Flask(__name__)
@application.route("/")
def index():
	resp = banner()
	return render_template('main.html',data=resp)
@application.route("/main")
def main():
    return render_template('main.html')

def banner():
	b = bannerController.bannerController()
	resp = b.getBanner()
	return json.loads(resp)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
