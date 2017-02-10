import unittest
import os
import sys
sys.path.append('../')
import pypertrail

class TestAPI(unittest.TestCase):

    def test_exclusive_api_params(self):
        api_token = os.environ['api_token']
        pt = pypertrail.Pypertrail(api_token)
        with self.assertRaises(TypeError):
            r = pt.search_events('search_string', min_id='12345', min_time='0')

    def test_invalid_api_param(self):
        api_token = os.environ['api_token']
        pt = pypertrail.Pypertrail(api_token)
        with self.assertRaises(TypeError):
            r = pt.search_events('search_string',foo='bar')

if __name__ == '__main__':
    unittest.main()
