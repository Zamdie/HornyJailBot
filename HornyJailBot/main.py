import time; # Imports time lib
from HornyJailBot import HornyJailBot # Imports HornyJailBot class from HornyJailBot lib

HornyExterminator = HornyJailBot() # I meant "local HornyExterminator = HornyJailBot.new()"

try: # Try statement so there is a way to detect program termination

    while True: # Infinite loop

        time.sleep(15) # Waits 15 seconds

        HornyExterminator.CheckSubmissions() # Calls CheckSubmissions method of HornyJailBot object
        
finally:

    # This code will be run after manually stopping execution (Ctrl + C) because it makes things error
    HornyExterminator.OnTermination(); # Calls OnTermination method of HornyJailBot object
