import json
import boto3

def lambda_handler(event, context):
    print(event)
    
    transactionID = event["queryStringParameters"]["transactionID"]

    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('transaction-details')
    resp = table.get_item(Key={'partition_key' : transactionID})

    transactionResponse = {}
    transactionResponse["transactionID"] = str(transactionID)
    transactionResponse["transactionType"] = str(resp["Item"]["transactionType"])
    transactionResponse["transactionAmount"] = str(resp["Item"]["amount"])  
    
           
    responseObject = {}
    responseObject["statusCode"] = 200
    responseObject["headers"] = {}
    responseObject["headers"]["Content-Type"] = "application/json"
    responseObject["body"] = json.dumps(transactionResponse)

    return responseObject