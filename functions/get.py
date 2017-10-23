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
    item = response.get("Item", None)

    if (item):
        response = {
            "statusCode": 200,
            "body": json.dumps(item)
        }
    else:
        response = {
            "statusCode": 404
        }

    return response