# -*- coding:utf-8-*-
from flask import Flask,render_template
from http import bannerController
import json
import redis
application = Flask(__name__)
@application.route("/")
def index():
	r = redis.Redis()
	resp = r.get("banner")
	if not resp:
		resp = banner()
	else:
		resp  = r.get("banner")
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
