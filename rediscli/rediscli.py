import redis


class rediscli():

    redis_conn = None

    def __init__(self):
        self.connect()


    def connect(self):
        pool = redis.ConnectionPool()
        robj = redis.Redis(connection_pool=pool)
        self.redis_conn = robj

    def get(self,name):
        return self.redis_conn.get(name)

    def set(self,name,value,ex=3600):
        self.redis_conn.set(name=name,value=value,ex=ex)

