import json
import boto3
from botocore.exceptions import ClientError

client = boto3.client("dynamodb")
TableName = "ResumeSiteVisitors"


def viewCounter(event, context):
    increment = (
        event.get("queryStringParameters", {}).get("increment", "true").lower()
        == "true"
    )

    try:
        data = client.get_item(TableName=TableName, Key={"stat": {"S": "view-count"}})
        currentCount = data.get("Item", {}).get("quantity", {}).get("N", "0")

        if increment:
            response = client.update_item(
                TableName=TableName,
                Key={"stat": {"S": "view-count"}},
                UpdateExpression="ADD quantity :inc",
                ExpressionAttributeValues={":inc": {"N": "1"}},
                ReturnValues="UPDATED_NEW",
            )
            currentCount = response["Attributes"]["quantity"]["N"]

    except ClientError as e:
        print(e.response["Error"]["Message"])
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Could not retrieve or update view count"}),
            "headers": {"Content-Type": "application/json"},
        }

    return {
        "statusCode": 200,
        "body": json.dumps({"viewCount": currentCount}),
        "headers": {"Content-Type": "application/json"},
    }
