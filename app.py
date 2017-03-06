# -*- coding:utf-8-*-
from flask import Flask, render_template
from http import bannerController
import json
import rediscli.rediscli

application = Flask(__name__)


@application.route("/")
def index():
    resp = banner()
    return render_template('main.html', data=resp)


@application.route("/main")
def main():
    return render_template('main.html')


def banner():
    r = rediscli.rediscli.rediscli()
    resp = r.get("banner")
    if not resp:
        b = bannerController.bannerController()
        resp = b.getBanner()
        r.set("banner", resp)

    return json.loads(resp)

def getposts():

    pass


if __name__ == "__main__":
    # init_db()
    application.run(host='0.0.0.0')
