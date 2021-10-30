from threading import Thread
from itertools import cycle
from time import time, sleep
from sys import stdout
import praw
import json
import os

done = False
start = time()


def animate(message):
    for c in cycle([f'⡿ {message}', f'⣟ {message}', f'⣯ {message}', f'⣷ {message}', f'⣾ {message}', f'⣽ {message}', f'⣻ {message}', f'⢿ {message}']):
        if done:
            print(
                f'\u001B[32m\r✔️  Task Completed Successfully in \u001B[33m{str (round(time() - start, 2))}s \u001B[0m ')
            break
        stdout.write('\r' + '\u001B[36m' + c)
        stdout.flush()
        sleep(0.06)


Thread(target=animate, args=("Scraping Reddit Data",)).start()

reddit = praw.Reddit(client_id='client_id_here',
                     client_secret='client_secret_here', user_agent='app_name_here')

scraped_data = {
    "title": [],
    "body": [],
    "author": []
}

hot_posts = reddit.subreddit('stories').hot(limit=300)
for post in hot_posts:
    scraped_data["body"].append(str(post.selftext))
    scraped_data["title"].append(str(post.title))
    scraped_data["author"].append(str(post.author))

json_data = json.dumps(scraped_data, indent=4)

os.mkdir('Stories')
os.chdir('Stories')

with open("Stories.json", "w") as file:
    file.write(json_data)

done = True


os.system('pause')
