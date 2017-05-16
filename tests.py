from apium import create_app
from apium.config import test_config
from faker import Factory

import unittest

fake = Factory.create()


class TestCase(unittest.TestCase):
    def setUp(self):
        app = create_app(test_config)
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_world(self):
        r = self.app.get('/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, 'Hello')


if __name__ == '__main__':
    unittest.main()
