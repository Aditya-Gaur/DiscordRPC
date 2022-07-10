from pypresence import Presence
import readline
import time
import sys

client_id = '992798462565417051'  # My app ID, (optional : put your's here)
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

data = {                      # Template 
     'state':None,
     'details':None,
     'large_image':None, 
     'large_text':None, 
     'small_image':None, 
     'small_text':None, 
     'buttons':None
      }

if len(sys.argv) > 1:
    pass # Add pre-build combos   

print("Press Enter to skip a field\nAvailable images : [python, c, cpp, visual-studio-code, gh, terminal]\n")

for i in data.keys():             # Ask for input if value is None in template
    if data[i] == None:
        if i != 'buttons':
            data[i] = input(f'{i}: ')     
            data[i] = None if data[i] == '' else data[i]
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

RPC.update(state=data['state'],
      details=data['details'],
      large_image=data['large_image'],
      large_text=data['large_text'],
      small_image=data['small_image'],
      small_text=data['small_text'],
      buttons=data['buttons'])  # Set the presence

'''
RPC.update(state="Lookie Lookie",
      details="Editing rpc.py..",
      large_image="python",
      large_text="Python",
      small_image="visual-studio-code",
      small_text="VS code",
      buttons=[{"label": "Website", "url": "https://github.com/Aditya-Gaur"}, {"label": "TODO", "url": "https://google.com"}])  # Set the presence
'''

print('Running..')
while True:  # The presence will stay on as long as the program is running
    time.sleep(15) # Can only update rich presence every 15 seconds
