import json
import re


def lambda_handler(event, context):
    try:
        reqBody = json.loads(event['body'])
        if('str' in reqBody):
            respBody = {
                "containsAllLetters" : str(contains_all_letters(reqBody['str']))
            }
        else:
            return {
                "statusCode": 400,
                "body": "Please pass in a str."
            }
    except:
        return {
            "statusCode": 500,
            "body": "An internal server error has occurred."
        }
    response = {
        "statusCode": 200,
        "body": json.dumps(respBody)
    }

    return response

def contains_all_letters(str):
    strLetters = re.sub(r'[^a-z]', '', str.lower())
    uniqueChars = set(strLetters)
    return len(uniqueChars) == 26
