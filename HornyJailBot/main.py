import praw;
import time;
import os;
from dotenv import load_dotenv;
from HornyJailBot import HornyJailBot
#from github import Github;

load_dotenv()

HornyExterminator = HornyJailBot()
print(HornyExterminator.cache)
try:

    while True:

        time.sleep(15)

        HornyExterminator.CheckSubmissions()
        
except:

    # This code will be run after manually stopping execution (CTRL + C) because it makes things error
    HornyExterminator.OnTermination();