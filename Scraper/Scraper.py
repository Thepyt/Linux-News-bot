import requests
from bs4 import BeautifulSoup 
import json

class Scraper:
    def __init__(self, url_code):
        self.url_code = url_code
        with open("config.json", "r") as file:
            self.code = json.load(file)
        self.content = self.getURL()

    def getURL(self):
        url = self.code[self.url_code]["url"]
        content = requests.get(url)
        return content.content

    def scrapeData(self):
        format :dict = {}
        """
        Steps: 
            - Get the homepage element (normally a div with an id)
            - Get 2 nested elements in each homepage (the first 2)
            - Find the links and titles
            - Open the links
            - Scrape the byline and first paragraph
        """
        count_ = self.code[self.url_code]["number"]
        for i in range(count_):
            format[i] = {}

        soup = BeautifulSoup(self.content, "html5lib")
        homepage = ""
        if "class" in self.code[self.url_code]["home-page"]:
            homepage = soup.find(self.code[self.url_code]["home-page"]["tag"], class_ = self.code[self.url_code]["home-page"]["class"])
        elif "id" in self.code[self.url_code]["home-page"]:
            homepage = soup.find(self.code[self.url_code]["home-page"]["tag"], id = self.code[self.url_code]["home-page"]["id"])
        else:
            homepage = soup.find_all(self.code[self.url_code]["home-page"]["tag"])

        Links = homepage.find_all(self.code[self.url_code]["Link"]["tag"])
        Links = [Links[self.code[self.url_code]["Link"]["count"][0]], Links[self.code[self.url_code]["Link"]["count"][1]]]

        title_1 = ""
        title_2 = ""
        if self.code[self.url_code]["Link"]["Data"]["Title"] == "get":
            title_1 = Links[0].get_text()
            title_2 = Links[1].get_text()
        else:
            title_1 = Links[0].get(self.code[self.url_code]["Link"]["Data"]["Title"]).replace(self.code[self.url_code]["Link"]["Data"]["replace"][0], self.code[self.url_code]["Link"]["Data"]["replace"][1])
            title_2 = Links[1].get(self.code[self.url_code]["Link"]["Data"]["Title"]).replace(self.code[self.url_code]["Link"]["Data"]["replace"][0], self.code[self.url_code]["Link"]["Data"]["replace"][1])

        title = [title_1, title_2]
        link = [Links[0].get(self.code[self.url_code]["Link"]["Data"]["Url"]), Links[1].get(self.code[self.url_code]["Link"]["Data"]["Url"])]
        for i in range(len(link)):
            if self.code[self.url_code]["Link"]["Data"]["Url-incomplete"]:
                link[i] = self.code[self.url_code]["url"] + link[i]

        paragraph = []
        for i in link:
            new_content = requests.get(i)
            parse = BeautifulSoup(new_content.content, "html5lib")
            para = parse.find_all(self.code[self.url_code]["Paragraph"]["tag"])
            para_list = [para[self.code[self.url_code]["Paragraph"]["count"][0]].get_text(), para[self.code[self.url_code]["Paragraph"]["count"][1]].get_text()]
            paragraph.append(para_list)

        for x in format:
            format[x]["title"] = title[x]
            format[x]["url"] = link[x]
            format[x]["para"] = paragraph[x]
        return format   