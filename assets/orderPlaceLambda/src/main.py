print("Loading function1")
import json
from utils.logger import Logger
from services.KiteService import KiteService
from services.PlaceOrderService import OrderPlaceService
from controllers.OrderPlaceController import OrderPlaceController
print("Loading function2")
logger = Logger.logger
kiteService = KiteService()
orderService = OrderPlaceService(kiteService.getKite())
orderController = OrderPlaceController(orderService)



def handler(event, context) : 
    message = None
    logger.info("Event : " + json.dumps(event))
    # kiteService.getLTP()   #Inorder to check that is KiteService working or not


    # return ResponseBuild(Status.SUCCESS, True, "We have placed order with order_id " + str(order_id))
    try : 
        order_id = orderController.placeOrder(event)
        message = "We have placed order with order_id " + str(order_id)
    except Exception as e :
        message = str(e);

    
    return {
        'statusCode': 200,
        'body': json.dumps({'greeting':  message})
    }




