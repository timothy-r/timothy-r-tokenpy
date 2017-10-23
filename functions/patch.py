import json
import os
import boto3

def handler(event, context):

    id = event["pathParameters"]["id"]

    body = {
        "message": "patch",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response