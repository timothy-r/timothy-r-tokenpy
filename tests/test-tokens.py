import unittest
import uuid
import os
import requests
import json
import random
from datetime import datetime

""" 
    test adding tokens
"""
class TokenTestCase(unittest.TestCase):

    def test_get_missing_token_fails(self):
        endpoint = self.createTokenEndpoint()

        r = requests.get(endpoint)
        self.assertMissing(r)


    def test_add_token(self):

        """ create a token """
        data = self.createTokenData()
        endpoint = self.createTokenEndpoint()
        r1 = requests.put(endpoint, json.dumps(data))

        self.assertSuccess(r1)

        """ get the token """
        r2 = requests.get(endpoint)

        """ assert they are the same """
        self.assertSuccess(r2)

        responseData = r2.json()
        self.assertEqual(data["name"], responseData["name"])
        self.assertEqual(data["date"], responseData["date"])


    def test_remove_token(self):

        """ create a token """
        data = self.createTokenData()
        endpoint = self.createTokenEndpoint()

        r1 = requests.put(endpoint, json.dumps(data))

        self.assertSuccess(r1)

        """ remove the token """
        r2 = requests.delete(endpoint)
        self.assertSuccess(r2)

        r3 = requests.get(endpoint)
        self.assertMissing(r3)

    """ 
        generate a new token endpoint 
    """
    def createTokenEndpoint(self):
        server = os.environ['TEST_SERVER']
        tokenId = uuid.uuid4()
        return "https://" + server + "/" + str(tokenId)

    def createTokenData(self):
        return {"name": "test-" + str(random.random()), "date": datetime.now().isoformat()}

    def assertSuccess(self, r):
        self.assertEqual(200, r.status_code)

    def assertMissing(self, r):
        self.assertEqual(404, r.status_code)

if __name__ == '__main__':
    unittest.main()
