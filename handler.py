import json
from scraper import Scraper

def scrapeTx(event, context):

    # Ensure Inputs are valid
    if(checkInputs(event)):
        depth = int(event['pathParameters']['depth'])
        txid = event['pathParameters']['id']

        # Initialize TX Scraper
        s = Scraper(txid, depth)

        # Grab all responses and return valid HTTP Response
        body = { "results": s.getResults() }
        response = { "statusCode": 200, "body": json.dumps(body) }
        return response

    # If Inputs are Invalid
    else:
        body = { "results": 'Error occured' }
        response = { "statusCode": 500, "body": json.dumps(body) }

# Function to check Inputs
def checkInputs(event):
    if(event['pathParameters']['depth'] and event['pathParameters']['id']): 
        return True
    else: return False