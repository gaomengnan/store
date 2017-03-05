from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker,relationships

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:@localhost:3306/app?charset=utf8",convert_unicode = True)


dbSession = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

dbBase = declarative_base()
dbBase.query = dbSession.query_property()


dbBase.metadata.create_all(bind=engine)


