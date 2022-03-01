
from pypresence import Presence
import time

mm = """

1. With Time Elapsed

2. Without Time Elapsed

3. One Button

4. Two Buttons

"""

client = int(input("Paste Your Client ID here"))
client_id = (client)  # Fake ID, put your real one here
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

start_time=time.time() 
RPC.update(state="", details="By unofficialdxnny", large_image="https://imgur.com/FtuQIfw.jpg", buttons=[{"label": "unofficialdxnny", "url": "https://github.com/unofficialdxnny/"}, {"label": "unofficialdxnny Server", "url": "https://discord.gg/jm2BFbqb8h"}], start=start_time)
