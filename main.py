from Bot.bot import Bot
from Scraper.Scraper import Scraper
from Depackager.depack import Depack
import datetime

class App:
    def __init__(self, code):
        self.code = code
        self.data = Scraper(self.code).scrapeData()
        self.message = Depack(self.data, self.code).unpack()
        print(self.message)
    
    def sendMessage(self):
        if self.message:
            Bot().message(self.message)


