import json

class Depack:
    def __init__(self, dict, code):
        self.dict = dict
        self.code = code
        with open("url.json", "r") as file:
            self.url_list = json.load(file)
        self.verify()
    
    def verify(self):
        list = self.url_list[self.code]
        for x in self.dict:
            if self.dict[x]["url"] in list:
                self.dict[x]["D"] = True

    def unpack(self):
        final = ""
        data = []
        for i in self.dict:
            if "D" in self.dict[i]:
                continue
            final = "# " + self.dict[i]["title"] + "\n"
            final = final + "**"+self.dict[i]["para"][0]+"**\n"
            final = final +self.dict[i]["para"][1]+"...\n"
            final = final + "Read More:" + self.dict[i]["url"]
            self.url_list[self.code].append(self.dict[i]["url"])
            data.append(final)
        
        with open("url.json", "w") as file:
            json.dump(self.url_list, file)

        return data