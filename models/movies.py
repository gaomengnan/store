from app import dba,dbSession

class movies(dba.Model):
    __tablename__ = "movies"

    id = dba.Column(dba.Integer, primary_key=True)
    title = dba.Column(dba.String(126))
    cover = dba.Column(dba.String(256))
    source = dba.Column(dba.String(100))
    created_at = dba.Column()
    link = dba.Column()
    meta = dba.Column(dba.String(256))

    def __init__(self, title, cover, source, created_at, link, meta):
        self.title = title

        self.cover = cover

        self.source = source

        self.created_at = created_at

        self.link = link

        self.meta = meta

    def __repr__(self):
        return '<Posts %r>' % self.title
