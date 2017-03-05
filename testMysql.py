#coding=utf-8
from models import Posts,dbSession



new = Posts.Posts("搞","萌")

dbSession.add(new)
dbSession.commit()
dbSession.close()

