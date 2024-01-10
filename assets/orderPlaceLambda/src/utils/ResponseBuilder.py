import json
from constants.Status import *

class ResponseBuilder():    
    
    def buildResponse(status : Status, isBasedEncoded : bool, data : str):
        return {
            'status' : status.value,
            'headers': json.dumps({
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }),
            'body': json.dumps({
                'message' : data
            })
        }
