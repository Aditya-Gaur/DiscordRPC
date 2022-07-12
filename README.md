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

## How to use :



- **Usage:**

```
python3 rpc.py optional_template_id
```

(this REadme is currently a live project changes/additions are done almost everyday)
### TODO from here


### **Known issues with fixes**

1. ConnectionRefusedError: [Errno 111] Connection refused

- Restart your pc
- Restart your network service/wifi

2. pypresence.exceptions.DiscordNotFound: Could not find Discord installed and running on this machine.

- Restart Discord

3. Pypresense not detecting in discord

- Check if another instance of this script is running in the background, if yes close it
