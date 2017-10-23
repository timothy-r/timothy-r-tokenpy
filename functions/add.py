import json
import os
import boto3

def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])

    """
     ensure body is json first
    """
    try:
        data = json.loads(event["body"])
        data["id"] = event["pathParameters"]["id"]

        table.put_item(
            Item = data
        )

        response = {
            "statusCode": 200
        }
    except:
        response = {
            "statusCode": 400
        }

    return response