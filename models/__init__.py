from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://root:@localhost:3306/app?charset=utf8",convert_unicode = True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

dbBase = declarative_base()
dbBase.query = db_session.query_property()


dbBase.metadata.create_all(bind=engine)


