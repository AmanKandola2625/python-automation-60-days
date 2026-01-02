import unittest
from unittest.mock import patch, Mock

from api_client import fetch_status

class TestApiClient(unittest.TestCase):

    @patch("api_client.requests.get")
    def test_fetch_status(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        status = fetch_status("https://api.github.com")
        self.assertEqual(status, 200)

if __name__ == "__main__":
    unittest.main()
