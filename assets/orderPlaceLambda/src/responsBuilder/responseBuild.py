from .Status import *
import json

def ResponseBuild(status : Status, isBasedEncoded : bool, data : str):
    return {
        'status' : status.value,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message' : data
        })
    }
