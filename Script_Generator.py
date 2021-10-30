import os
import json
import random
from profanityfilter import ProfanityFilter

pf = ProfanityFilter()

with open('Stories\\Stories.json','r') as file:
    data = json.load(file)
    file.close()
    title = data['title']
    body = data['body']
    author = data['author']

def nameFilter(author):
    author = list(author)
    num = []

    for i in author:
        if i.isdigit():
            num.append(i)

    for i in num:
        del author[author.index(i)]

    author_name = "".join(author)
    return author_name



while True:
    try:

        title_final = random.choice(title)
        body_final = data['body'][data['title'].index(title_final)]

    except ValueError or UnicodeError:

        body_final = random.choice(body)
        author_final = data['author'][data['body'].index(body_final)]

    else:

        author_final = data['author'][data['body'].index(body_final)]

    finally:
        if pf.is_profane(title_final) or pf.is_profane(body_final) or pf.is_profane(author_final) or len(body_final.split(' ')) <= 100:
            continue
        else:
            break;

author_name = ["".join(author_final.split(' ')[0].title()) if " " in author_final else author_final]
author_name = nameFilter(author_final)


Host_Line_1 = f"Hello Ladies and Gentlemen, Welcome to Storifaaeed Wednesday, coz it's Wednesday my dudes. Anyways I am your host Skeletor, and today here we have {author_final} with us"

Author_Line_1 = f"Hello everybody, I'm {author_name}, here to tell you a real story, I would like to thank Skeletor for inviting me here at Storified Wednesday"

Host_Line_2 = f"Thanks {author_name}, Okay, so if you're ready , let's begin the podcast!"

Author_Story = f"{title_final}. \n{body_final}"

Host_Ending = f"That was a great story {author_name}, and with that, we've reached the end of the story, skeletor will be back with a new story next wednesday, Don't forget to come back on Storifaaeed Wednesday"

content = f"{Host_Line_1}\n\n{Author_Line_1}\n\n{Host_Line_2}\n\n\n\n{Author_Story}\n\n\n\n\n\n{Host_Ending}".encode('utf-8')

os.mkdir('Scripts')
os.chdir('Scripts')

with open('Host_Line_1.txt','wb') as file:
    file.write((Host_Line_1).encode('utf-8'))
    file.close()

with open('Host_Line_2.txt', 'wb') as file:
    file.write((Host_Line_2).encode('utf-8'))
    file.close()

with open('Host_Ending.txt', 'wb') as file:
    file.write((Host_Ending).encode('utf-8'))
    file.close()

with open('Author_Line_1.txt', 'wb') as file:
    file.write((Author_Line_1).encode('utf-8'))
    file.close()

with open('Author_Story.txt', 'wb') as file:
    file.write((Author_Story).encode('utf-8'))
    file.close()

with open('Script.txt','wb') as file:
    file.write(content)
    file.close()

# I tried my best to include *sad words here*
words = ['sad','depressed','threatened','scared','frightened','gun','die','cried','cry','dead','worst','scary','scariest','ill','miserable','heartbreaking','breakup','broken','kill','suicide']

for i in words:
    if i in body_final or i in title_final:
        STORY = "SAD"
    else:
        STORY = "HAPPY"

with open('theme.txt','w') as file:
    file.write(STORY)
    file.close()
    
print("\u001B[32m"+"Script Successfully Generated"+"\u001B[0m")


