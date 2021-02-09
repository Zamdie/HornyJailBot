from time import sleep # Imports sleep method from time lib
from HornyJailBot import HornyJailBot; # Imports HornyJailBot class from HornyJailBot lib

HornyExterminator = HornyJailBot(); # I meant "local HornyExterminator = HornyJailBot.new()"

try: # Try statement so there is a way to detect program termination

    while True: # Infinite loop     
    
        #HornyExterminator.CheckSubmissions(); # Calls CheckSubmissions method of HornyJailBot object

        HornyExterminator.CheckInbox(); # Calls CheckInbox method of HornyJailBot object
        
        sleep(2); # Waits 15 seconds
        
except:

    # This code will be run after manually stopping execution (Ctrl + C) because it makes things error

    HornyExterminator.OnTermination(); # Calls OnTermination method of HornyJailBot object
