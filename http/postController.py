from models import Posts,dbSession
class postController():

    def __init__(self):

        pass


    def getpost(self,page,pagesize):
        offset = (page  -1 ) *pagesize
        resp = Posts.Posts.query.order_by(Posts.Posts.created_at.desc()).offset(offset).limit(pagesize).all()
        dbSession().commit()
        # dbSession().close()
        return resp



if __name__ == "__main__":

    resp = postController().getpost(1,10)
    for i in resp:
        print i.cover


