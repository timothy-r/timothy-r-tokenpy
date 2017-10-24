import json
import os
import boto3

def handler(event, context):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ['TABLE_NAME'])
    id = event["pathParameters"]["id"]

    """
     ensure body is json first
    """
    try:
        data = json.loads(event["body"])

        table.update_item(
            Key={"id": id},
            AttributeUpdates = data
        )

        response = {
            "statusCode": 200
        }
    except Exception as e:
        response = {
            "statusCode": 400,
            "message": str(e)
        }

    return response