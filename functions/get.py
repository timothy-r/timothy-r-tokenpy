import json
import os
import boto3
import ast

def handler(event, context):

    id = event["pathParameters"]["id"]

    client = boto3.client('dynamodb')

    response = client.get_item(
        TableName = os.environ['TABLE_NAME'],
        Key = {'id': {'S': id} }
    )
    item = response.get("Item", None)

    if (item):
        """ convert ddb json data into a dict """
        data = ast.literal_eval((json.dumps(item, cls=DecimalEncoder)))
        response = {
            "statusCode": 200,
            "body": json.dumps(data)
        }
    else:
        response = {
            "statusCode": 404
        }

    return response