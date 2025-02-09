import unittest
from app import app as weather_app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = weather_app.test_client()
        self.app.testing = True

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weather_page_no_location(self):
        response = self.app.post('/weather', data={'location': ''})
        self.assertEqual(response.status_code, 302)  

    def test_weather_page_with_location(self):
        response = self.app.post('/weather', data={'location': 'New York'})
        self.assertEqual(response.status_code, 200) 

    def test_error_page(self):
        response = self.app.get('/error')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()