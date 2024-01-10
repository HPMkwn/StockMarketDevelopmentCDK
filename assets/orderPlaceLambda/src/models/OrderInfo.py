from utils.logger import Logger
from models.Exchange import Exchange
from models.OrderType import OrderType
from models.OrderVariety import OrderVariety
from models.TransactionType import TrnsactionType
from models.PriceType import PriceType
from exceptions.ValidationError import ValidationError

class OrderInfoBuilder():

    def __init__(self):
        self.trading_symbol = None
        self.exchange = None
        self.transactionType = None
        self.orderType = None
        self.orderVariety = None
        self.quantity = None
        self.price = None

    def setTradingSymbol(self, trading_symbol : str):
        Logger.logger.info("Trading Symbol : " + trading_symbol)
        if trading_symbol is not None:
            self.trading_symbol = trading_symbol
        else : 
            raise ValidationError("Trading Symbol must be provided")

        return self

    def setExchange(self, exchange : str): 
        Logger.logger.info("Exchange : " + exchange)
        if exchange in Exchange:
            self.exchange = Exchange[exchange]
        else:
            raise ValidationError("Exchange must be from Exchange")

        return self
    
    def setTransactionType(self, transactionType : str):
        Logger.logger.info("TransactionType : " + transactionType)

        if transactionType in TrnsactionType:
            self.transactionType = TrnsactionType[transactionType]
        else :  
            raise ValidationError("TransactionType must be from TransactionType")
        return self
    
    def setOrderType(self, orderType : str):
        Logger.logger.info("OrderType : " + orderType)
        if orderType in OrderType:
            self.orderType = OrderType[orderType]
        else :
            raise ValidationError("OrderType must be from OrderType")
        return self
    
    def setOrderVariety(self, orderVariety : str):
        Logger.logger.info("setOrderVariety " + orderVariety)
        if orderVariety in OrderVariety:
            self.orderVariety = OrderVariety[orderVariety]
        else : 
            raise ValidationError("OrderVariety must be from OrderVariety")
        return self
    
    def setQuantity(self, quantity : str):
        Logger.logger.info("setQuantity " + quantity)
        try : 
            self.quantity = int(quantity)
        except Exception as e :
            raise ValidationError("Quantity must be an integer", e)

        return self

    def setPrice(self, price : str):
        Logger.logger.info("setPrice " + price)
        try : 
            self.price = float(price)
        except Exception as e :
            if price in PriceType: 
                self.price = PriceType[price].value
            else :
                raise ValidationError("Price must be a float or PriceType", e)
        return self

    def build(self):
        Logger.logger.info("Building OrderInfo")
        try :
            return OrderInfo(self.trading_symbol, self.exchange, self.transactionType, self.orderType, self.orderVariety, self.quantity, self.price)
        except Exception as e:
            Logger.logger.error("Error building OrderInfo : " + str(e))
            raise e


class OrderInfo():

    def __init__(self, trading_symbol : str, exchange : Exchange, transactionType : TrnsactionType, orderType : OrderType, orderVariety : OrderVariety, quantity : str, price):
        self.trading_symbol = trading_symbol
        self.exchange = exchange.value
        self.transactionType = transactionType.value
        self.orderType = orderType.value
        self.orderVariety = orderVariety.value
        self.quantity = quantity
        self.price = price
        self.instrument = self.exchange + ":" + self.trading_symbol

        Logger.logger.info("OrderInfo : " + str(self))  

    def __str__(self):
        return f"OrderInfo(trading_symbol={self.trading_symbol}, exchange={self.exchange}, transactionType={self.transactionType}, orderType={self.orderType}, orderVariety={self.orderVariety}, quantity={self.quantity}, price={self.price})"
    
    def __repr__(self):
        return f"OrderInfo(trading_symbol={self.trading_symbol}, exchange={self.exchange}, transactionType={self.transactionType}, orderType={self.orderType}, orderVariety={self.orderVariety}, quantity={self.quantity}, price={self.price})"
    
    def __eq__(self, other):        
        return self.trading_symbol == other.trading_symbol and self.exchange == other.exchange and self.transactionType == other.transactionType and self.orderType == other.orderType and self.orderVariety == other.orderVariety and self.quantity == other.quantity and self.price == other.price

    def getTradingSymbol(self):
        return self.trading_symbol

    def getExchange(self):
        return self.exchange

    def getTransactionType(self):
        return self.transactionType

    def getOrderType(self):
        return self.orderType

    def getOrderVariety(self):
        return self.orderVariety

    def getQuantity(self):
        return self.quantity

    def getPrice(self):
        return self.price

    def getInstrument(self):
        return self.instrument
  


