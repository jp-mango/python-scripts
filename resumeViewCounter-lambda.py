import json, boto3
from botocore.exceptions import ClientError

# Initialize a DynamoDB client
client = boto3.client('dynamodb')
# Define the table name for DynamoDB
TableName = 'ResumeSiteVisitors'

def viewCounter(event, context):
    # Try to get the current view count from the DynamoDB table
    try:
        data = client.get_item(
            TableName=TableName,
            Key={'stat': {'S':'view-count'}}
        )
        # Extract the view count value; default to '0' if not found
        prevViewCount = data.get('Item', {}).get('quantity', {}).get('N', '0')
    
    # Handle any errors that might occur during the fetch operation    
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not retrieve view count'}),
            'headers': {'Content-Type': 'application/json'}
        }
    
    # Increment the view count in the DynamoDB table
    try:
        response = client.update_item(
            TableName=TableName,
            Key={'stat': {'S':'view-count'}},
            UpdateExpression='ADD quantity :inc',
            ExpressionAttributeValues={":inc" : {"N":"1"}},
            ReturnValues='UPDATED_NEW'
        )
        # Extract the updated view count from the response
        value = response['Attributes']['quantity']['N']
    
    # Handle any errors that might occur during the update operation    
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not update view count'}),
            'headers': {'Content-Type': 'application/json'}
        }
    
    # Return a successful response with the updated view count
    return {
        'statusCode': 200,
        'body': json.dumps({'viewCount': value}),
        'headers': {'Content-Type': 'application/json'}
    }