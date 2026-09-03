import unittest
from caching import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
