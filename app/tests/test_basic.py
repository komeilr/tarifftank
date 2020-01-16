import os
import unittest

from app.factory import create_app, db
import config


class BasicTests(unittest.TestCase):
    def setUp(self):        
        self.app = create_app(config.TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_index(self):
        tester = self.app.test_client()
        response = tester.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    
    def test_about(self):
        tester = self.app.test_client()
        response = tester.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    
    def test_contact(self):
        tester = self.app.test_client()
        response = tester.get('/contact', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    def test_404(self):
        tester = self.app.test_client()
        response = tester.get('/other', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__=='__main__':
    unittest.main()