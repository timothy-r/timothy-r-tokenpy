import json
import os
import boto3

def handler(event, context):

    id = event["pathParameters"]["id"]

    client = boto3.client('dynamodb')

    response = client.get_item(
        TableName = os.environ['TABLE_NAME'],
        Key = {'id': {'S': id} }
    )

    if (response["item"]):
        response = {
            "statusCode": 200,
            "body": json.dumps(response["item"])
        }
    else:
        response = {
            "statusCode": 404
        }

    return response