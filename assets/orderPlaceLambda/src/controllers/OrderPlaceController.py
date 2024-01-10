from utils.logger import Logger
from services.PlaceOrderService import OrderPlaceService
from models.OrderInfo import OrderInfo, OrderInfoBuilder
from constants.RequestParams import RequestParams 
from utils.ParseRequest import RequestParcer
from exceptions.OrderPlaceError import OrderPlaceError
import json

class OrderPlaceController():

    def __init__(self, orderPlaceService : OrderPlaceService):
        self.logger = Logger.logger
        self.orderPlaceService = orderPlaceService

    def buildOrderRequest(self, orderRequest):
        Logger.logger.info("Building Order!!!")

        try :
            orderInfo = OrderInfoBuilder()\
                                .setTradingSymbol(orderRequest[RequestParams.TRADING_SYMBOL])\
                                .setExchange(orderRequest[RequestParams.EXCHANGE])\
                                .setOrderType(orderRequest[RequestParams.ORDER_TYPE])\
                                .setTransactionType(orderRequest[RequestParams.TRANSACTION_TYPE])\
                                .setOrderVariety(orderRequest[RequestParams.VARIETY])\
                                .setQuantity(orderRequest[RequestParams.QUANTITY])\
                                .setPrice(orderRequest[RequestParams.PRICE])\
                                .build()
            return orderInfo
        except Exception as e:
            Logger.logger.error("Error while building orderInfo : " + str(e))
            raise OrderPlaceError("Error while building orderInfo", e)

                        

    def placeOrder(self, orderRequest):

        order_id = None;

        try :   
            self.logger.info("Order Request : " + json.dumps(orderRequest))

            body = RequestParcer.extractBody(orderRequest)

            self.logger.info(body)

            self.logger.info(type(body))

            orderRequest = self.buildOrderRequest(body)

            order_id = self.orderPlaceService.place_order(orderRequest) 

        except ValueError as e:
            raise e
        except Exception as e:
            raise OrderPlaceError("Error while placing order", e)
        

        return order_id


    def call(self): 

        req = {
                'trading-symbol': 'TAPARIA',
                'exchange': 'BSE',
                'transaction-type': 'BUY',
                'quantity': '1000',
                'variety': 'VARIETY_AMO',
                'order-type': 'ORDER_TYPE_LIMIT',
                'price': 'upper_circuit_limit'
            }
        
        print(type(req))

        orderInfo = self.buildOrderRequest(req);

        print(orderInfo)


orderPlaceController = OrderPlaceController(OrderPlaceService(None))

orderPlaceController.call()