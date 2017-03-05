from sqlalchemy import Column, Integer,String
from models import dbBase,dbSession,relationships

class Posts(dbBase):

    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(126))
    cover = Column(String(256))

    def __init__(self,title,cover):

        self.title = title

        self.cover = cover

    def __repr__(self):
        return '<Posts %r>' % self.title

