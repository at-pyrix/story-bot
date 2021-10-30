# Introduction

This is a story bot, that will scrape stories from r/stories subreddit and convert it into an Audio File

# Installation

> `pip install -r requirements.txt` to install all required Packages.

# How to Run?

- First Run `Reddit_Scraper.py`. This will scrap 300 stories and save it into a json file. Also fill the `client_id`, `client_secret` and `user_agent`. ![Learn More](https://www.jcchouinard.com/get-reddit-api-credentials-with-praw/)
- Then Run `Script_Generator.py`. This will take the Json file and select a random story from it and save it in a text file
- Finally Run `Podcast_Generator.py`. This will convert the text file into text-to-speech audio and add background music accordingly.

## How to add your own music

- Add the Music you want in the `Music`(CREATE) Folder in `story-bot`
- Add the Sad Songs in `Sad-Music`(CREATE) and the other ones in `Happy-Music`(CREATE).
- Only `.wav` files will work however.
