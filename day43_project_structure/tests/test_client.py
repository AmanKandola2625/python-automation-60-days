import unittest
from unittest.mock import patch, Mock

from app.client import fetch_status

class TestClient(unittest.TestCase):

    @patch("app.client.requests.get")
    def test_fetch_status(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        status = fetch_status()
        self.assertEqual(status, 200)

if __name__ == "__main__":
    unittest.main()
