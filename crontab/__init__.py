from models import Posts
from models.Posts import dbSession

import requests
from bs4 import BeautifulSoup

def cawler():
    resp = requests.get("http://movie.youku.com/?spm=a2hww.20023042.topNav.5~1~3!3~A")
    resp.encoding="utf-8"
    soup =  BeautifulSoup(resp.text,"html5lib")
    div = soup.find(id="m_86988")
    cols = div.findAll("div",attrs={"class":"yk-col4"})
    for col in cols:
        # print col
        cover = col.div.div.img["_src"]
        title = col.find("div",attrs={"class":"v-meta-title"}).text


        has = Posts.Posts.query.filter(Posts.Posts.title == title).first()
        if not has:
            new_data = Posts.Posts(title,cover)
            dbSession.add(new_data)
            dbSession.commit()
            dbSession.close()



if __name__ == "__main__":
    resp = cawler()


