import unittest
from app import app


class TestGetDataAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_data_with_valid_params(self):
        response = self.app.get('api/v1/data?value=5&startTime=2008-01-01T05:00:00&endTime=2008-01-25T08:00:00')
        self.assertEqual(response.status_code, 200)
        data = response.json.get('data')
        self.assertIsInstance(data, list)
        self.assertTrue(all('start' in item and 'end' in item and 'duration' in item for item in data))

    def test_get_data_with_invalid_params(self):
        response = self.app.get('api/v1/data?value=0&starttime=2024-04-09T08:00:00&endtime=2024-04-09T05:00:00')
        self.assertEqual(response.status_code, 400)
        error_message = response.json.get('message', '')
        self.assertIn('Invalid', error_message)



if __name__ == '__main__':
    unittest.main()