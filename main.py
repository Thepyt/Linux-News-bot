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


while True:
    hour = datetime.datetime.now().hour
    min = datetime.datetime.now().min

    if hour == 15 and min == 30:
        App("omg").sendMessage()
    elif hour == 16 and min == 45:
        App("news").sendMessage()
    elif hour == 0 and min == 15:
        App("ifoss").sendMessage()
    elif hour == 10 and min == 0:
        App("point").sendMessage()
    elif hour == 12 and min == 0:
        App("925").sendMessage()