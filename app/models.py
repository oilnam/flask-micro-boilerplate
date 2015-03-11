from app import db

class Entity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)

    def __init__(self, _content):
        self.content = _content

    def __repr__(self):
        return 'Entity {0}'.format(self.content)
