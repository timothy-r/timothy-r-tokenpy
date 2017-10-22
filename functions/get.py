import json


def handler(event, context):

    id = event["pathParameters"]["id"]

    body = {
        "message": "get",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response