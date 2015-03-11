import app
import unittest
from app.models import Entity

class BaseTestCase(unittest.TestCase):
    """ Base test case """

    def create_app(self):
        app.config.from_object('config.TestConfiguration')
        return app

    def setUp(self):
        app.db.create_all()

    def tearDown(self):
        app.db.session.remove()
        app.db.drop_all()


class FirstTest(BaseTestCase):
    def test_tautology(self):
        assert 1 == 1

    def test_orm(self):
        e = Entity('batman')
        app.db.session.add(e)
        app.db.session.commit()
        app.db.session.close()
        
        q = Entity.query.filter_by(content = 'batman').first()
        assert q.content == 'batman'
        

if __name__ == '__main__':
    unittest.main()
