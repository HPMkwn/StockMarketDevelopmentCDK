import os
from utils.logger import Logger
from lib.kiteapp import KiteApp
from constants.EnvironmentVariables import EnvironmentVariables


class KiteService() : 
    def __init__(self):
        self.logger = Logger.logger
        self.logger.info("KiteService init")

        self.clientName = os.environ[EnvironmentVariables.clientName]
        self.clientId = os.environ[EnvironmentVariables.clientID]
        self.cliendEncToken = os.environ[EnvironmentVariables.clientSecret]

        self.logger.info(self.clientName + " : " + self.clientId + " : " + self.cliendEncToken);

        self.kite = KiteApp(self.clientName, self.clientId, self.cliendEncToken)

        self.logger.info(self.kite.ltp(self.kite.EXCHANGE_BSE+ ":TAPARIA"))


    
    def getKite(self):
        return self.kite
    

    def getLTP(self):
        self.logger.info(self.kite.ltp(self.kite.EXCHANGE_BSE+ ":TAPARIA"))
