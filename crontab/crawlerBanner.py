#coding=utf-8
import sys,os
sys.path.append(os.path.split(os.path.realpath(__file__))[0])

import requests

import re
from db import db

import time
class crawlerBanner():
	
	url = "http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A"
	
	banner = None
		
	def __init__(self):
	
		pass	

	def run(self):
		resp = requests.get(self.url)
		
		if resp.status_code!=200:
			sys.stdout.write("[%] GET %s %s\r\n"%(time.strftime("%Y-%m-%d %h:%i:%s",time.localtime(time.time()),self.url,resp.status_code)))		

		out = re.sub(r"\n","",resp.content)
		o=re.search(r"var posterMovieGrid86981 = new posterMovieGrid\(.*data:(.+?]),.*\);",out)
		if o:
			sys.stdout.write("[%s] banner®%sº\r\n"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),o.group(1)))
			self.banner =  o.group(1)
	def save(self):
		
		d = db.DB()
		d.query("update options set option_value='"+ self.banner+"' where option_name='banner'")


if __name__ == "__main__":

	obj = crawlerBanner()

	obj.run()
	
	obj.save()

#	resp = requests.get("http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A")
#	out = re.sub(r"\n","",resp.content)
#	o = re.search(r"var posterMovieGrid86981 = new posterMovieGrid\(.*data:(.+?]),.*\);",out)
#	print o.group(1)
	pass
