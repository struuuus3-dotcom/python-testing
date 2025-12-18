# patch `main3.requests` with raise_for_staus
import unittest
from unittest.mock import Mock, patch

from requests import exceptions
from requests.exceptions import HTTPError

from main3 import get_joke


class TestGetJoke(unittest.TestCase):
    @patch("main3.requests")
    def test_get_joke_succes(self, requests_mock):
        response_mock = Mock()
        response_mock.raise_for_status.side_effect = HTTPError("Error")

        requests_mock.get.return_value = response_mock
        requests_mock.exceptions = exceptions

        result = get_joke()
        self.assertEqual(result, "HTTPError was raised")


if __name__ == "__main__":
    unittest.main(verbosity=2)
