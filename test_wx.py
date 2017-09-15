# -*- coding:utf-8 -*-
__authors__ = 'gmn'

"""
你需要导入的包
↓
"""
import os, sys,datetime,time
import requests
from collections import OrderedDict
import json
__wx__ = OrderedDict()

__wx__.setdefault("openid","果酱")
__wx__.setdefault("token","iDOFlnyIm-fLGiJXKl3iN1D_ius0ovl9C0fwOxZu9KitlxscUd5fAFCPHmTXr8r4HIbijqlbYuo0zXrJHQCcDo8Iq_MiwXhuLKaIKp97x8EaW5gAqj16JY8XWfq-T2E3BWJbAJANIV")
BEGIN_DATE = "2017-03-08"


def getdaysoffset(begin = None):
    date_list = []
    if begin:
        begin_date = datetime.datetime.strptime(begin, "%Y-%m-%d")
    else:

        begin_date= datetime.datetime.now()
    # begin_date = now.strftime("%Y-%m-%d")

    end_date = begin_date - datetime.timedelta(days=7)
    # end_date = end_date.strftime("%Y-%m-%d")

    while begin_date >= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date = begin_date -  datetime.timedelta(days=1)
    return date_list

# re = getBetweenDay("2017-03-08")

# print __wx__.get("token")

# print resp.json()

for i in getdaysoffset("2017-03-08"):
    req = "https://api.weixin.qq.com/datacube/getuserread?access_token=" + __wx__.get("token")
    # print req
    # print i
    req_param = {
        "begin_date":i,
        "end_date":i
    }
    req_param = json.dumps(req_param)
    resp = requests.post(req,req_param)
    lists = json.loads(resp.text)
    lists = lists.get("list")

    if lists:

        print lists[0].get("int_page_read_user").__str__()
    else:
        print 0
    # sys.exit()
    # print resp.text









