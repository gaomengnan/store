import MySQLdb




class DB():
	
	__host = "localhost"

	__user = "root"
	
	__passwd = ""

	__db = "app"

	conn = None
	cur = None	

	def __init__(self,host=None,user=None,passwd=None,db=None):

		host = host if (host!=None) else (self.__host)
		user = user if (user!=None) else (self.__user)
		passwd = passwd if (passwd!=None) else (self.__passwd)
		db = db if (db!=None) else (self.__db)
		conn = MySQLdb.Connect(host=host,user=user,passwd=passwd,db=db)
		self.conn = conn		

	def insert(self):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		self.conn.commit()
	
	def query(self,sql):
		cursor = self.conn.cursor()
		cursor.execute(sql)
		self.cur = cursor

	def close(self):
		self.cur.close()	

	def commit(self):
		self.conn.commit()
	
	

	def fetchOne(self):
		return self.cur.fetchone()
	

if __name__ == "__main__":
	
	db = DB()



	
