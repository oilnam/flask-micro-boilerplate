from app import app, db
import flask
from models import Entity

@app.route('/')
@app.route('/index')
def index():

    e = Entity('whatever')
    db.session.add(e)
    db.session.commit()
    db.session.close()

    q = Entity.query.filter_by(content = 'whatever').first()

    return flask.render_template('index.html',
                                 title = 'boilerplate',
                                 dump = q.content)


