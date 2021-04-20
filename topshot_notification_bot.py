#importing required modules

import time
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup

# Account sid and token from twilio dashboard goes here:

account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

client = Client(account_sid, auth_token)

# Twilio whatsapp number and the number you are going to use:

from_whatsapp_number = "whatsapp:+10000000000"
to_whatsapp_number = "whatsapp:" + "+905333333333"

# I will be taking the data from the nbatopshot blog page

url = "https://blog.nbatopshot.com/"

response = requests.get(url)

soup = BeautifulSoup(response.content,"html.parser")

condition = True
while condition:
    # I choose the category of the newest headline in the blog
    for drop in soup.find_all("div", {"class", "top-post-text"}):
        drops = drop.a.text
        print(drops)
        # If the category of the headline is == "Drops" then it means there will be a pack drop
        if drops[:5] == "Drops":
            client.messages.create(body="DROP ALERT",
                                from_ = from_whatsapp_number,
                                to = to_whatsapp_number)
            time.sleep(43200)
        else:
            time.sleep(1800)








