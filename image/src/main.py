import kiteapp as kt

def handler(event, context) : 

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
    return {
        "statusCode" : 200,
        "body" : {
            "message" : "Hello From Lambda Function with an Docker Image",
        } 
    }
