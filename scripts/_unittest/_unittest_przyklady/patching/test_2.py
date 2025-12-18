# patch `main.requests`
import unittest

from unittest.mock import Mock, patch

from main import get_joke


class TestGetJoke(unittest.TestCase):

    @patch("main.requests")
    def test_get_joke_succes(self, requests_mock):
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            'value': 'A super joke!'
        }
        requests_mock.get.return_value = response_mock

        result = get_joke()

        self.assertEqual(result, 'A super joke!')


if __name__ == "__main__":
    unittest.main()
