# Introduction

This is a story bot, that will scrape stories from r/stories subreddit and convert it into an Audio File

# Installation

> `pip install -r requirements.txt` to install all required Packages.

# How to Run?

- First Run `Reddit_Scraper.py`. This will scrap 300 stories and save it into a json file. Also fill the `client_id`, `client_secret` and `user_agent`. [Learn More](https://www.reddit.com/dev/api/)
- Then Run `Script_Generator.py`. This will take the Json file and select a random story from it and save it in a text file
- Finally Run `Podcast_Generator.py`. This will convert the text file into text-to-speech audio and add background music accordingly.

## How to add your own music

- Add the Music you want in the `Music` Folder in `story-bot`
- Name the Happy songs `Happy-Music-4, Happy-Music-5...` and so on.
- Name the Sad songs `Sad-Music-4...` and so on.
- Make sure to add them in the songs_list array in `Podcast Generator.py`
