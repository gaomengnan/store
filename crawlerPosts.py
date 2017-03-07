#coding=utf-8
from models import Posts
from models.Posts import dbSession
import click
import requests
from bs4 import BeautifulSoup
import time,sys



def crawler():
    print "开始任务 [%s] -- \r\n" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
    resp = requests.get("http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A")
    resp.encoding="utf-8"
    soup =  BeautifulSoup(resp.text,"html5lib")
    div = soup.find(id="m_86988")
    cols = div.findAll("div",attrs={"class":"yk-col4"})
    for col in cols:

        is_hovers = col.findAll("div",attrs={"class":"v ishover"})
        for is_hover in is_hovers:
            # print col
            link = is_hover.find("div",attrs={"class":"v-link"}).a['href']
            # print link
            cover = is_hover.div.img["_src"]
            title = is_hover.find("div",attrs={"class":"v-meta-title"}).text
            has = Posts.Posts.query.filter(Posts.Posts.title == title).first()
            if not has:
                new_data = Posts.Posts(title,cover,"优酷",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())),link,"院线热映")
                dbSession.add(new_data)
                dbSession.commit()
                dbSession.close()
                time.sleep(0.5)


nameMap = {
    'youku':crawler()
}

@click.command()
@click.option("--source",default=None,help="type [youku,aiqiyi.eg]")
def main(source):
    func = nameMap.get(source,None)
    if func:
        func()

if __name__ == "__main__":
    main()




