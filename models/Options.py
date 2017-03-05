# from models import
from sqlalchemy import Column, Integer
from models import dbBase
class Options(dbBase):

    __tablename__ = "options"

    id = Column(Integer,primary_key=True)
    option_name = Column()
    option_value = Column()

    def __init__(self,option_name,value):
        self.option_name = option_name

        self.option_value = value

    def __repr__(self):
        return '<Option %r>'%self.option_name
