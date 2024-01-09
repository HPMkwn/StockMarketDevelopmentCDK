import json
import kiteapp as kt
import os
import time

from responsBuilder.responseBuild import * 
from responsBuilder.Status import Status
import base64


def parse_body(event):
    """Parses the JSON body of an event into a Python object."""
    try : 
        if not event.get('body'):
            return {}
        if event.get('isBase64Encoded'):
            body = base64.b64decode(event['body'])
        else:
            body = event['body']
        if isinstance(body, str):
            body = json.loads(body)
        elif not isinstance(body, dict):
            raise ValueError('Body must be a JSON object')
    except Exception as e:
        return event['body']

    return body

def handler(event, context) : 

    print(event);
    body = parse_body(event)
    print(body)


    with open("enctoken.txt") as f1:
        enctoken = f1.read()
    kite = kt.KiteApp("Herat","HN3004",enctoken)

    order_id=None

    try : 
        tradingsymbol = "TAPARIA"
        instrument="BSE:TAPARIA"
        print(kite.quote(instrument)[instrument]['upper_circuit_limit'])
        order_id = kite.place_order(
            tradingsymbol=tradingsymbol,
            exchange=kite.EXCHANGE_BSE,
            transaction_type=kite.TRANSACTION_TYPE_BUY,
            quantity=1000,
            variety=kite.VARIETY_AMO,
            order_type=kite.ORDER_TYPE_LIMIT,
            price=kite.quote(instrument)[instrument]['upper_circuit_limit'],
            product=kite.PRODUCT_CNC,
            validity=kite.VALIDITY_DAY
        )
        print(order_id)
    except Exception as e: 
        print(e)

    print(order_id)
    print(kite.ltp(kite.EXCHANGE_BSE+ ":TAPARIA"))
    # return ResponseBuild(Status.SUCCESS, True, "We have placed order with order_id " + str(order_id))

    return {
        'statusCode': 200,
        'body': json.dumps({'greeting':  "We have placed order with order_id " + str(order_id)})
    }




