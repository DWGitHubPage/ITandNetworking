#!/usr/bin/env python3
# Python 3.9.5

'''Getting all the news headlines, with their links for the start of the day using
Mergefeed.net. The one below has the headlines from Hackernews, TechCrunch, and Techmeme.

You can personalize it to the sites you prefer by going to the Mergefeed.net site,
putting each website's link on each line, click the "Create Multifeed" button, and from there
copy and paste the adress from the address bar into the url below'''

import webbrowser


url = 'https://mergefeed.net/Untitled?urls=https://news.ycombinator.com/+https://techcrunch.com/+https://www.techmeme.com/'

webbrowser.open_new_tab(url)
