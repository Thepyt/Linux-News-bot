# Linux-News-bot
## Project Details
A discord bot which will scrape the title, url and the byline and first paragraph of a bunch of newsletters and send them to a discord channel. For example:
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/88c11906-1dc5-4238-b404-1cff97a63da4)
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/ba567fca-0e48-416e-8be3-e2c136bb8992)
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/0d544f91-8ac5-40e7-9cbb-0e1f900a9007)

## Capabilities
The bot is able to 
- Scrape Websites such as <a href="https://itsfoss.com">itsfoss.com</a>, <a href="https://news.itsfoss.com">news.itsfoss.com</a>, <a href="https://omgubuntu.co.uk">omgubuntu.co.uk</a>, <a href="https://9to5linux.com/
">9to5linux.com</a> and  <a href="https://pointieststick.com/">pointieststick.com</a>
- Get access to the top 2 latest articles published by these at a given time and access their url, title (article heading) and the first 2 paragraphs (usually a byline and a paragraph, depending on the website).
- Verify if the article has already been posted to the server
- If not, formats the data and sends the data as a message on a timely basis.

## Working
The program here is fairly straightforward. The program makes use the <a href="https://pypi.org/project/requests/">requests</a> library to access the web content of a website to which it is directed. The required data is then extracted using the <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup</a> library. The BeautifulSoup library acts on instructions from the `config.json` file. The data is then formatted into a message using the depack class and then sent via the bot.  
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/17b26041-13dc-45c1-a443-29eb7144025e)

The `config.json` file takes 3 major elements into consideration.
- The body container (it was a div followed by an id or a class)
- The Title link (which was convenient to extract the link and the title)
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/27237482-96de-4404-8daf-12e043999862)

The `config.json` has a structure similar to this
```
{
  "Code-of-url" : {
        "Part-of-structure" : {
                "Tags"     : "tag to find",
                "class/id" : "class-to-find",
                "Data"     : {
                    "Part" : "Part-to-get"
            } 
        }
    }
}
```
This means, all we need to do is to access the data from the config file and just substitute the data into places to get the scraper ready. There have been certain parts where I handled certain exceptions to this rule using if statements like when I needed to substitute the `class_` or `id` argument
```python
if "class" in self.code[self.url_code]["home-page"]:
    homepage = soup.find(self.code[self.url_code]["home-page"]["tag"], class_ = self.code[self.url_code]["home-page"]["class"])
elif "id" in self.code[self.url_code]["home-page"]:
    homepage = soup.find(self.code[self.url_code]["home-page"]["tag"], id = self.code[self.url_code]["home-page"]["id"])
else:
    homepage = soup.find_all(self.code[self.url_code]["home-page"]["tag"])
```
This has pros and cons: 
- I needn't customise my code again and again for each and every website and can just edit the config file to my liking.
while also
- making the program overly which makes it difficult to host.

The end result is a dictionary of the structure
```
{
  count<int> : {
        "Title" : "Title",
        "Url"   : "url",
        "Paragraph" : ["para 1", "para2"]
    }
}
```
This dictionary is then unpacked using the depack module to the format of 
```
# Title
**para1**
para2
read more: url
```

It is then posted to discord using the <a href="https://github.com/Rapptz/discord.py">discord</a> API. The channel id needs to be updated to the users preference which can be done manually by right clicking the channel

![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/0e0c53c4-a061-42db-999e-d2af46b0ebf3)

The bot's token is stored in an `env` file which can be accessed using the `os.getenv()` command

## Future plans
Currently
- ways to host the bot in a server are underway
- code cleaning is underway
