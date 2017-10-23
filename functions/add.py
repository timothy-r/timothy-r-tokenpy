import json
import os
import boto3

def handler(event, context):

    id = event["pathParameters"]["id"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    table.put_item(
        Key = Key={'id':{'S': id}},
        Item = event['body']
    )

    response = {
        "statusCode": 200
    }

    return response