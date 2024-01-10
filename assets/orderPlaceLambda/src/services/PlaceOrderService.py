from utils.logger import Logger
from models.OrderInfo import OrderInfo
from models.PriceType import PriceType
from exceptions.OrderPlaceError import OrderPlaceError
from constants import OrderTypeMappings as om
from constants import VarietyMappings as vm
class OrderPlaceService():
    
    def __init__(self, kite):
        self.logger = Logger.logger
        self.logger.info("Initializing Order Place Service")
        self.kite = kite

    def place_order(self, orderRequest : OrderInfo) -> str:
        self.logger.info("Placing order!!!!")
        order_id = None;

        try : 
            tradingsymbol = orderRequest.getTradingSymbol()
            self.logger.info("Trading Symbol : " + tradingsymbol)
            instrument=orderRequest.getInstrument()
            self.logger.info("Instrument : " + instrument)
            price = orderRequest.getPrice() 
            self.logger.info("Price : " + str(price))
            orderType = orderRequest.getOrderType()
            self.logger.info("Order Type : " + orderType)

            self.logger.info(self.kite.ltp(self.kite.EXCHANGE_BSE+ ":TAPARIA"))

            self.logger.info(self.kite.quote(instrument)[instrument][price])

            if isinstance(price,str): 
                price = self.kite.quote(instrument)[instrument][price]
            elif price is None:
                orderType = self.kite.ORDER_TYPE_MARKET

            self.logger.info("Price : " + str(price))


            order_id = self.kite.place_order(
                tradingsymbol=tradingsymbol,
                exchange=orderRequest.getExchange(),
                transaction_type=orderRequest.getTransactionType(),
                quantity=int(orderRequest.getQuantity()),
                variety=vm.get_variety_type_enum()[orderRequest.getOrderVariety()],
                order_type=om.get_order_type_enum()[orderType],
                price=float(price),
                product=self.kite.PRODUCT_CNC,
                validity=self.kite.VALIDITY_DAY
            )
        except Exception as e: 
            self.logger.error("Error while placing order : " + str(e))
            raise OrderPlaceError("Error while placing order", str(e))
        

        self.logger.info("Hurrrray!!!!!! Order placed with order_id " + str(order_id))
        return order_id
        

