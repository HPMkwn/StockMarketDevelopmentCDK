from Exchange import Exchange
from OrderType import OrderType
from OrderVariety import OrderVariety
from TransactionType import TrnsactionType
from PriceType import PriceType
from ..exceptions.ValidationError import ValidationError



class OrderInfoBuilder():

        def __init__(self):
            self.trading_symbol = None
            self.exchange = None
            self.transactionType = None
            self.orderType = None
            self.orderVariety = None
            self.quantity = None
            self.price = None
            pass

        def setTradingSymbol(self, trading_symbol : str):
            if trading_symbol is not None:
                self.trading_symbol = trading_symbol
            else : 
                raise ValidationError("Trading Symbol must be provided")

            return self

        def setExchange(self, exchange : str): 
            if exchange in Exchange:
                self.exchange = Exchange[exchange]
            else:
                raise ValidationError("Exchange must be from Exchange")

            return self
        
        def setTransactionType(self, transactionType : str):
            if transactionType in TrnsactionType:
                self.transactionType = TrnsactionType[transactionType]
            else :  
                raise ValidationError("TransactionType must be from TransactionType")
            return self
        
        def setOrderType(self, orderType : str):
            if orderType in OrderType:
                self.orderType = OrderType[orderType]
            else :
                raise ValidationError("OrderType must be from OrderType")
            return self
        
        def setOrderVariety(self, orderVariety : str):
            if orderVariety in OrderVariety:
                self.orderVariety = OrderVariety[orderVariety]
            else : 
                raise ValidationError("OrderVariety must be from OrderVariety")
            return self
        
        def setQuantity(self, quantity : str):
            
            try : 
                self.quantity = int(quantity)
            except Exception as e :
                raise ValidationError("Quantity must be an integer", e)

            return self

        def setPrice(self, price : str):

            try : 
                self.price = float(price)
            except Exception as e :
                if price in PriceType: 
                    self.price = PriceType[price]
                else :
                    raise ValidationError("Price must be a float or PriceType", e)
            return self
        
        def build(self):
            return OrderInfo(self.trading_symbol, self.exchange, self.transactionType, self.orderType, self.orderVariety, self.quantity, self.price)
 

class OrderInfo():

    def __init__(self, trading_symbol : str, exchange : Exchange, transactionType : TrnsactionType, orderType : OrderType, orderVariety : OrderVariety, quantity : str, price):
        self.trading_symbol = trading_symbol
        self.exchange = exchange
        self.transactionType = transactionType
        self.orderType = orderType
        self.orderVariety = orderVariety
        self.quantity = quantity
        self.price = price


    def __str__(self):
        return f"OrderInfo(trading_symbol={self.trading_symbol}, exchange={self.exchange}, transactionType={self.transactionType}, orderType={self.orderType}, orderVariety={self.orderVariety}, quantity={self.quantity}, price={self.price})"
    
    def __repr__(self):
        return f"OrderInfo(trading_symbol={self.trading_symbol}, exchange={self.exchange}, transactionType={self.transactionType}, orderType={self.orderType}, orderVariety={self.orderVariety}, quantity={self.quantity}, price={self.price})"
    
    def __eq__(self, other):        
        return self.trading_symbol == other.trading_symbol and self.exchange == other.exchange and self.transactionType == other.transactionType and self.orderType == other.orderType and self.orderVariety == other.orderVariety and self.quantity == other.quantity and self.price == other.price


    def getBuilder():
        return OrderInfoBuilder() 


           
 


orderInfo = OrderInfo.getBuilder()\
                    .setTradingSymbol('AAPL')\
                    .setExchange('NSE')\
                    .setTransactionType('BUY')\
                    .setOrderType('ORDER_TYPE_LIMIT')\
                    .setOrderVariety('VARIETY_AMO')\
                    .setQuantity('10')\
                    .setPrice('LIMIT')\
                    .build()    


print(orderInfo)