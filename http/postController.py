from models import movies
class postController():

    def __init__(self):

        pass


    def getpost(self,page,pagesize):
        offset = (page  -1 ) *pagesize
        resp = movies.movies.query.order_by(movies.movies.created_at.desc()).offset(offset).limit(pagesize).all()
        # dbSession().close()
        return resp



if __name__ == "__main__":

    resp = postController().getpost(1,10)
    for i in resp:
        print i.created_at


