# -*- coding:utf-8-*-
from flask import Flask, render_template
from http import bannerController
import json
import rediscli.rediscli
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
# app = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/app?charset=utf8'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
dba = SQLAlchemy(application)
dbSession = dba.session
@application.route("/")
def index():
    posts = getposts(1,10)
    resp = banner()
    # posts = getposts(1,10)
    return render_template('main.html', data=resp,posts=posts)


@application.route("/main")
def main():
    return render_template('index.html')


def banner():
    r = rediscli.rediscli.rediscli()
    resp = r.get("banner")
    if not resp:
        b = bannerController.bannerController()
        resp = b.getBanner()
        r.set("banner", resp)

    return json.loads(resp)

def getposts(page,pagesize):
    from http import postController
    __list__ = []
    resp = postController.postController().getpost(page,pagesize)
    for item in resp:
        __list__.append({
            'title':item.title,
            'cover':item.cover,
            'link':item.link,
            'meta':item.meta,
            'source':item.source

        })


    return __list__


if __name__ == "__main__":
    # init_db()
    application.run(host='0.0.0.0')
