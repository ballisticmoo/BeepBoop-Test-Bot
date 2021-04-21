import discord
import os
import requests
import json
import random
import data
from ping import keep_alive
from requests_html import HTML, HTMLSession

client = discord.Client()
client = discord.Client(activity=discord.Game(
    name="Ruel's personal pet hehe :>"))


def get_cookie():
    lucky = random.randint(1, 100)
    session = HTMLSession()
    r = session.get('http://www.myfortunecookie.co.uk/fortunes/' + str(lucky))
    div = r.html.find('div', first=True)
    cookie = div.find('.fortune', first=True).text
    return (cookie)


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"] + " -" + json_data[0]["a"]
    return (quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$quote'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("$8b"):
        lucky_num = random.randint(0, len(data.response_list) - 1)
        await message.channel.send(data.response_list[lucky_num])

    if message.content.startswith("$ohayou"):
        ohayou_num = random.randint(0, len(data.ohayou_list) - 1)
        await message.channel.send(data.ohayou_list[ohayou_num])

    if message.content.startswith("$cookie"):
        cookie = get_cookie()
        await message.channel.send(cookie)

    if message.content.startswith("$help"):
        await message.channel.send(
            "The dev. is still working on it <:PeepoPing:774200189925720065>")


keep_alive()
client.run(os.getenv('BEEPBOOP'))
