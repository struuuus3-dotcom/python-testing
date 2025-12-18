# patch `main2.requests` with raise_for_staus
import unittest
from unittest.mock import Mock, patch

from requests import exceptions
from requests.exceptions import Timeout

from main2 import get_joke


class TestGetJoke(unittest.TestCase):

    @patch("main2.requests")
    def test_get_joke_succes(self, requests_mock):
        requests_mock.get.side_effect = Timeout("Timeout")
        requests_mock.exceptions = exceptions

        result = get_joke()

        self.assertEqual(result, "No jokes")


if __name__ == "__main__":
    unittest.main()
