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

## Instructions to Run
To run this program, first create a discord bot (refer <a href="https://support.appreciationengine.com/support/solutions/articles/47001211829-creating-a-discord-app">here</a>). Copy the tokens after giving the bot the appropriate permissions.

Create an `.env` file and paste the token there using the variable
```env
TOKEN=token-goes-here
```
Copy the channel id from the discord server where you intend to post the message. 

![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/0e0c53c4-a061-42db-999e-d2af46b0ebf3)

Head over to the `bot.py` file in the `Bot` directory and paste the channel id in the required place
```python
@self.client.event
async def on_ready():
    if not autosend.is_running():
        channel_id = 0 # id goes here
        channel =  await self.client.fetch_channel(channel_id)
        autosend.start(channel)
    print("Ready")
```

## Working
The program here is fairly straightforward. The program makes use the <a href="https://pypi.org/project/requests/">requests</a> library to access the web content of a website to which it is directed. The required data is then extracted using the <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup</a> library. The BeautifulSoup library acts on instructions from the `config.json` file. The data is then formatted into a message using the depack class and then sent via the bot.  
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/17b26041-13dc-45c1-a443-29eb7144025e)

The `config.json` file takes 3 major elements into consideration.
- The body container (it was a div followed by an id or a class)
- The Title link (which was convenient to extract the link and the title)
![image](https://github.com/Thepyt/Linux-News-bot/assets/87644800/27237482-96de-4404-8daf-12e043999862)

The `config.json` has a structure similar to this
```json
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
```json
{
  "Integer" : {
        "Title" : "Title",
        "Url"   : "url",
        "Paragraph" : ["para 1", "para2"]
    }
}
```
This dictionary is then unpacked using the depack module. The URL which has been unpacked is then verified with the list in `url.json` which has a file structure of 
```json
{
  "Code" : ["link1", "link2"]
}
```
If the link exists in the url list, then a `"D"` key is added to the dictionary with a value of True. This key is then ignored. Other keys are formatted as shown below
```
# Title
**para1**
para2
read more: url
```
This is appended into lists. Normally, depending on the config, there are two messages in a list.

It is then posted to discord using the <a href="https://github.com/Rapptz/discord.py">discord</a> API. The channel id needs to be updated for the users preference manually.

The bot's token is stored in an `env` file which can be accessed using the `os.getenv()` command

## Future plans
Currently
- Finding ways to host the bot in a server are underway
- Fixing the code

## Resources and Useful Links
<ol>
    <li><a href="https://www.freecodecamp.org/news/create-a-discord-bot-with-python/">freecodecamp</a></li>
    <li><a href="https://requests.readthedocs.io/en/latest/">Requests</a></li>
    <li><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/">BeautifulSoup</a></li>
    <li><a href="https://stackoverflow.com/questions/76256539/how-do-i-auto-send-a-message-using-discord-py">Discord auto send</a></li>
</ol>
