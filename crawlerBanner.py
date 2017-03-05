#coding=utf-8
import sys,os
sys.path.append(os.path.split(os.path.realpath(__file__))[0])

import requests

import re
# from db import db
from models import Options
from models.Options import dbSession
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
		out = re.sub(r"\n", "", resp.text)
		o = re.search(r"var posterMovieGrid86981 = new posterMovieGrid\((.*?)\);", out)
		r = o.group(1)
		u  = re.search(r".*data: (.*)",r)
		f = u.group(1)
		v = f.replace(",hotcode: true}","")
		sys.stdout.write("[%s] banner?%s?\r\n"%(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),v))
		self.banner =  v
	def save(self):
		
		Options.Options.query.filter(Options.Options.option_name == "banner").update({"option_value":self.banner})
		dbSession.commit()

if __name__ == "__main__":

	obj = crawlerBanner()

	obj.run()
	
	obj.save()

#	resp = requests.get("http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A")
#	out = re.sub(r"\n","",resp.content)
#	o = re.search(r"var posterMovieGrid86981 = new posterMovieGrid\(.*data:(.+?]),.*\);",out)
