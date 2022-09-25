from pypresence import Presence
import time
import sys
import requests
from random import choice
import json 

client_id = '992798462565417051'  # My app ID, (optional : put your's here)
API_KEY = 'PUT_THY_API_KEY_HERE' # optional tenor key !required to use gif options head over to https://developers.google.com/tenor/guides/quickstart to get one
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

def update():
    RPC.update(state=data['state'],
      details=data['details'],
      large_image=data['large_image'],
      large_text=data['large_text'],
      small_image=data['small_image'],
      small_text=data['small_text'],
      buttons=data['buttons'],
      start=data['time'])  # Set the presence


data = {                      # Template 
     'state':None,
     'details':None,
     'large_image':None, 
     'large_text':None, 
     'small_image':None, 
     'small_text':None, 
     'buttons':None,
     'time':None
      }

if len(sys.argv) > 1:
    pass # Add pre-build combos   

print("Press Enter to skip a field\nAvailable images : [python, c, cpp, visual-studio-code, gh, terminal, yt]\n")

for i in data.keys():             # Ask for input if value is None in template
    if data[i] == None:
        if i != 'buttons' and i != 'time':
            data[i] = input(f'{i}: ')     
            data[i] = None if data[i] == '' else data[i]
        elif i == 'time':
            inputs = ('y', 'n')
            user = 'None'
            while user[0] not in inputs:
                user = input(f'Add timer (y/n): ')
                if user == '':
                    break
            buff = 'n' if user == '' else user[0]
            data[i] = None if buff == 'n' else time.time()
        else:
            nbuttons = 3
            data[i] = list()
            while nbuttons > 2:
                nbuttons = input(f'No. of buttons(<=2): ')
                nbuttons = 0 if nbuttons == '' else int(nbuttons)

            for j in range(nbuttons):
                url = input(f'url: ')  
                label = input(f'label: ')
                print(f"Button {j} added.")
                data[i].append({"label":label, "url":url})

            data[i] = None if nbuttons == 0 else data[i]



'''
RPC.update(state="Lookie Lookie",
      details="Editing rpc.py..",
      large_image="python",
      large_text="Python",
      small_image="visual-studio-code",
      small_text="VS code",
      buttons=[{"label": "Website", "url": "https://github.com/Aditya-Gaur"}, {"label": "TODO", "url": "https://google.com"}])  # Set the presence
'''
update()
print('Running..')

# Extra functionality
anime_quote_rpc = True if data['state'] == "anime_quote" else False         # initiate anime quotes if state= anime_quote
anime_gif_rpc = True if data['large_image'] == "anime_gif" else False       # initiate anime gifs if large_image = anime_gif also(optional) large_text=gif_type
philosophy_quote_rpc = True if data['state'] == "p_quote" else False 
gif_rpc = True if data['large_image'] == "gif" else False

gif_reactions = ["airkiss","angrystare","bite","bleh","blush","brofist","celebrate","cheers","clap","confused","cool","cry","cuddle","dance","drool","evillaugh","facepalm","handhold","happy","headbang","hug","kiss","laugh","lick","love","mad","nervous","no","nom","nosebleed","nuzzle","nyah","pat","peek","pinch","poke","pout","punch","roll","run","sad","scared","shrug","shy","sigh","sip","slap","sleep","slowclap","smack","smile","smug","sneeze","sorry","stare","stop","surprised","sweat","thumbsup","tickle","tired","wave","wink","woah","yawn","yay","yes"]

while True:  # The presence will stay on as long as the program is running
    if anime_quote_rpc:
        q = eval(requests.get("https://api.rei.my.id/v3/quotes").text)     # {'quote': 'This is what a real trump card is.', 'anime': 'Naruto', 'id': 743, 'name': 'Shino Aburame'}
        data['details'] = f"Quote from {q['anime'][0:128]}"
        data['state'] = q['quote'][0:128]      # max char length 128

    if anime_gif_rpc:
        rect = choice(gif_reactions) if data['large_text'] not in gif_reactions else data['large_text']
        i = eval(requests.get(f"https://api.otakugifs.xyz/gif?reaction={rect}").text)     # {"url":"https://cdn.otakugifs.xyz/gifs/kiss/e5ba4cf1044a70a5.gif"}
        data['large_image'] = i["url"]

    if philosophy_quote_rpc:
        with open("assets/p_quotes.txt", "r") as f :
            quotes = eval(f.read())
        q = choice(quotes) 
        data['details'] = f"Quote from {q['source'][0:50]} on {q['philosophy'][0:30]}"
        data['state'] = q['quote'][0:128]      # max char length 128         

    if gif_rpc:
        if data['large_text'] == "":
            gg = eval(requests.get(f"https://tenor.googleapis.com/v2/categories?key={API_KEY}").text)["tags"]
            gf = choice(gg)
            data["large_image"] = gf["image"]
            data["large_text"] = gf["searchterm"]
        else:
            gg = json.loads(requests.get(f"https://tenor.googleapis.com/v2/search?q={data['large_text']}&key={API_KEY}&limit=25").text)["results"]
            gf = choice(gg)
            data["large_image"] = gf["media_formats"]["gif"]["url"]
            data["large_text"] = data['large_text']

    try:
        update()
    except:
        pass
    time.sleep(20) # Can only update rich presence every 15 seconds
