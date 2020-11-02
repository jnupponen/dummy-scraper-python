import requests
import boto3
import json
import os


def lambda_handler(event, context):
    try:
        data = requests.get("https://jsonplaceholder.typicode.com/todos/1")

        client = boto3.client('s3')
        client.put_object(Body=json.dumps(data.json()),
                          Bucket=os.environ.get('BUCKET'),
                          Key='data.json')
        print("Success")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return "ok"
