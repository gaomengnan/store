from db import db



class bannerController():


	def getBanner(self):
		d = db.DB()
		sql = "select * from options where option_name='banner'"
		d.query(sql)
		resp = d.fetchOne()
		id,name,value = resp
		return value
