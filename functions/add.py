import json
import boto3

def handler(event, context):

    id = event.pathParameters.id

    body = {
        "message": "add",
        "input": event,
        "body": event.body,
        "id": id
    }

    client = boto3.client('dynamodb')

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response