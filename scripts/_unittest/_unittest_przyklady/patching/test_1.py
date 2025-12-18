# patch `main.get_joke()`
import unittest
from unittest.mock import patch

from main import len_joke


class TestLenJoke(unittest.TestCase):

    # def test_len_joke(self):
    #     with patch("main.get_joke") as get_joke_mock:
    #         get_joke_mock.return_value = "A super joke"
    #         result = len_joke()
    #
    #         self.assertEqual(result, 12)


    @patch("main.get_joke")
    def test_len_joke(self, get_joke_mock):
        get_joke_mock.return_value = "A super joke"

        result = len_joke()

        self.assertEqual(result, 12)


if __name__ == "__main__":
    unittest.main()
