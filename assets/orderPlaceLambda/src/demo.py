


def handler(event, context) : 
    return {
        "statusCode" : 200,
        "body" : {
            "message" : "Hello From Lambda Function with an Docker Image inside demo.py",
        } 
    }


