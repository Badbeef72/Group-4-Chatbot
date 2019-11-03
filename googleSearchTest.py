# py -3 -m pip install -U beautifulsoup4
# py -3 -m pip install -U google

# query : query string that we want to search for.
# tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
# lang : lang stands for language.
# num : Number of results we want.
# start : First result to retrieve.
# stop : Last result to retrieve. Use None to keep searching forever.
# pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
# Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

# import appropriate api

from googlesearch import search
import discord
client = discord.Client()
async def googleSearch(google_msg, googleQuery):
    # perform the search

    combinedQuery = ' '.join(googleQuery)
    print(combinedQuery)
    for j in search(combinedQuery, tld="co.in", num=5, stop=1, pause=2):
        await google_msg.channel.send('Did you mean this? ' + j)

# make the user input be the search

# query = input("What would you like to search")


