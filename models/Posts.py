from sqlalchemy import Column, Integer,String
from models import dbBase,dbSession,relationships
class Posts(dbBase):

    __tablename__ = "movies"

    id = Column(Integer, primary_key=True)
    title = Column(String(126))
    cover = Column(String(256))
    source = Column(String(100))
    created_at = Column()
    link = Column()

    def __init__(self,title,cover,source,created_at,link):

        self.title = title

        self.cover = cover

        self.source = source

        self.created_at = created_at

        self.link = link

    def __repr__(self):
        return '<Posts %r>' % self.title




