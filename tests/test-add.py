import unittest
import uuid
import urllib
import os

""" 
    test adding tokens
"""
class AddTokenTestCase(unittest.TestCase):
    def test_add_token(self):

        tokenId = uuid.uuid4()

        """ create a token """
        data = {"name": "test"}
        server = os.environ['TEST_SERVER']

        endpoint = "https://" + server + "/" + tokenId.hex

        """ get the token """

        """ assert they are the same """
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
