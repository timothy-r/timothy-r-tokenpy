import json
import os
import boto3

def handler(event, context):

    id = event["pathParameters"]["id"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    response = table.delete_item(
        Key = {"id": id }
    )

    response = {
        "statusCode": 200
    }

    return response