import json
import os
import boto3

def handler(event, context):

    id = event["pathParameters"]["id"]

    client = boto3.client('dynamodb')

    item = client.get_item(TableName=os.environ['TABLE_NAME'], Key={'id':{'S': id}})

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