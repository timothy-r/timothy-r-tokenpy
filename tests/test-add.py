import unittest
import uuid
import urllib
import os
import requests
import json
import random
from datetime import datetime

""" 
    test adding tokens
    https://jgrk6gidqd.execute-api.eu-west-2.amazonaws.com/Prod/{id}
"""
class AddTokenTestCase(unittest.TestCase):
    def test_add_token(self):

        server = os.environ['TEST_SERVER']
        tokenId = uuid.uuid4()

        """ create a token """
        today = datetime.now().isoformat()
        data = {"name": "test-"+ str(random.random()), "date": today}
        endpoint = "https://" + server + "/" + str(tokenId)
        r1 = requests.put(endpoint, json.dumps(data))

        self.assertEqual(200, r1.status_code)

        """ get the token """
        r2 = requests.get(endpoint)

        """ assert they are the same """
        self.assertEqual(200, r2.status_code)
        responseData = r2.json()
        self.assertEqual(data["name"], responseData["name"])
        self.assertEqual(data["date"], responseData["date"])


if __name__ == '__main__':
    unittest.main()
