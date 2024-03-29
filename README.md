# **Discord RPC**
Make custom Discord RPC's easily

## Requirements :

- [Python 3](https://www.python.org/downloads/)

- [Pypresence](https://www.pygame.org/download.shtml) which can be easily installed after installing python with the command -

```
pip3 install pypresence
```

or in case that doesn't work
```
python3 -m pip3 install pypresence
```

- [requests](https://pypi.org/project/requests/) 

```
pip install requests
```

## How to use :



- **Usage:**

```
python3 rpc.py optional_template_id
```

#### NOTE: 
To change the deafault title "Adrick's Tavern" you need to create your own dc application. Head over to https://discord.com/developers/applications to create a new application. The name of your application will be displayed once you change the client id on line 8 
```
client_id = '992798462565417051'  # My app ID, (optional : put your's here)
```
Head over to https://support-dev.discord.com/hc/en-us/articles/360028717192-Where-can-I-find-my-Application-Team-Server-ID to find where your client id is located : )

<br />


- **Example 1**
```
Press Enter to skip a field
Available images : [python, c, cpp, visual-studio-code, gh, terminal, yt]

state: Lookie Lookie  
details: Editing rpc.py
large_image: https://github.com/Aditya-Gaur/DiscordRPC/raw/main/assets/python.jpg
large_text: Python
small_image: https://github.com/Aditya-Gaur/DiscordRPC/raw/main/assets/visual-studio-code.jpg 
small_text: VS code
No. of buttons(<=2): 2
url: https://github.com/Aditya-Gaur/DiscordRPC
label: View repo
Button 0 added.
url: https://open.spotify.com/album/40TZNoA3ePd2eFXzd4dtB2?si=n1sJOeNRTu6XjH2rtIaOZw
label: Worth a listen <3
Button 1 added.
Add timer (y/n): y
Running..
```
![ss1](https://user-images.githubusercontent.com/75514601/205442045-ed9ccb65-d497-428a-91c6-db66b75ac995.png)

<br />

### 1. **Using anime quotes**
```
state: anime_quote
```

### 2. **Using anime gifs**
```
large_image: anime_gif
```
- Optional functionality add a gif topic from ["airkiss","angrystare","bite","bleh","blush","brofist","celebrate","cheers","clap","confused","cool","cry","cuddle","dance","drool","evillaugh","facepalm","handhold","happy","headbang","hug","kiss","laugh","lick","love","mad","nervous","no","nom","nosebleed","nuzzle","nyah","pat","peek","pinch","poke","pout","punch","roll","run","sad","scared","shrug","shy","sigh","sip","slap","sleep","slowclap","smack","smile","smug","sneeze","sorry","stare","stop","surprised","sweat","thumbsup","tickle","tired","wave","wink","woah","yawn","yay","yes"]
```
large_text: blush
``` 
Or just write whatever if you dont care

### 3. **Using philosophy quotes**
```
state: p_quote
```

### 4. **Using custom tenor gifs**
```
large_image: gif
large_text: gif search topic(any)
```
- NOTE: Tenor API key required head over to https://developers.google.com/tenor/guides/quickstart to get one and change line 9
```
API_KEY = "sasasYourapikeybruh"
```

<br />

### **Screenshots**
![Screenshot_20221203-185240_Discord](https://user-images.githubusercontent.com/75514601/205442988-b6e32a18-36dd-474d-aaf7-f44ccaebb615.jpg)
![Screenshot 2022-12-03 185918](https://user-images.githubusercontent.com/75514601/205443202-45034374-f4fa-4d0c-a5e0-5bc37a16b2b6.png)


<br />

## Known issues with fixes : 

**1. ConnectionRefusedError: [Errno 111] Connection refused**

- Restart your pc
- Restart your network service/wifi

**2. pypresence.exceptions.DiscordNotFound: Could not find Discord installed and running on this machine.**

- Restart Discord

**3. Pypresense not detecting in discord**

- Check if another instance of this script is running in the background, if yes close it
