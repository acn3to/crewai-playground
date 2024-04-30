"""This module contains unit tests for the Flask application defined in 'src/app.py'."""

import unittest
from src.app import app


class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask application defined in 'src/app.py'."""

    def setUp(self):
        """
        Set up Flask app for testing.
        """
        app.testing = True
        self.app = app.test_client()

    # No tearDown method needed, as there's no cleanup required

    def test_hello_endpoint(self):
        """
        Test the '/hello' endpoint.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
