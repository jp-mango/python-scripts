import json, boto3

client = boto3.client('dynamodb')
TableName = 'ResumeSiteVisitors'

def viewCounter(event, context):
    data = client.get_item(
        TableName = 'ResumeSiteVisitors',
        Key = {
            'stat': {'S':'view-count'}
        }
    )
    prevViewCount = data['Item']['quantity']['N']

    response = client.update_item(
        TableName = 'ResumeSiteVisitors',
        Key = {
            'stat': {'S':'view-count'}
        },
        UpdateExpression = 'ADD quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N":"1"}},
        ReturnValues = 'UPDATED_NEW'
    )

    value = response['Attributes']['quantity']['N']

    return{
        'statusCode': 200,
        'body': value
    }