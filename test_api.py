
import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_all_data(self):
        response = self.client.get('/api/v1/vacunacion')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(response.json, list))

if __name__ == '__main__':
    unittest.main()
