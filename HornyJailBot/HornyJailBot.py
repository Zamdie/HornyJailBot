import praw;
import os;
import time;
from dotenv import load_dotenv;

load_dotenv();

def GetEnv(varName: str) -> str:

    return os.getenv(varName);

class HornyJailBot():
    
    """
    This is HornyJailBot's class, which contain all the functions and properties that can be referenced in the main program.
    
    Properties:
        self.subreddits - stores all subreddits
        self.cache - cache containing the ID's of posts that have been already been replied to, when program is interrupted, they are
        appended to RepliedPosts.txt, and commited to GitHub

    Methods:

        __init__ - Constructor, creates a local Reddit object, which then creates self.subreddits with a list of monitored subreddits and
        self.cache to store submission ID's which are written to RepliedPosts.txt on termination

        CheckSubmissions - Loops through the subreddits in self.subreddits and then through the submissions, checks if they are NSFW and
        if they are, bonks it, and appends to self.cache

        OnTermination - Called when program is interrupted, writes things on self.cache to RepliedPosts.txt, clears it and commits to GitHub

        ⣿⣿⣿⣿⣯⣿⣿⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠈⣿⣿⣿⣿⣿⣿⣆⠄
        ⢻⣿⣿⣿⣾⣿⢿⣢⣞⣿⣿⣿⣿⣷⣶⣿⣯⣟⣿⢿⡇⢃⢻⣿⣿⣿⣿⣿⢿⡄
        ⠄⢿⣿⣯⣏⣿⣿⣿⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣧⣾⢿⣮⣿⣿⣿⣿⣾⣷
        ⠄⣈⣽⢾⣿⣿⣿⣟⣄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣯⢿⣿⣿⣿⣿
        ⣿⠟⣫⢸⣿⢿⣿⣾⣿⢿⣿⣿⢻⣿⣿⣿⢿⣿⣿⣿⢸⣿⣼⣿⣿⣿⣿⣿⣿⣿
        ⡟⢸⣟⢸⣿⠸⣷⣝⢻⠘⣿⣿⢸⢿⣿⣿⠄⣿⣿⣿⡆⢿⣿⣼⣿⣿⣿⣿⢹⣿
        ⡇⣿⡿⣿⣿⢟⠛⠛⠿⡢⢻⣿⣾⣞⣿⡏⠖⢸⣿⢣⣷⡸⣇⣿⣿⣿⢼⡿⣿⣿
        ⣡⢿⡷⣿⣿⣾⣿⣷⣶⣮⣄⣿⣏⣸⣻⣃⠭⠄⠛⠙⠛⠳⠋⣿⣿⣇⠙⣿⢸⣿
        ⠫⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣹⢷⣿⡼⠋
        ⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣿⣿⣿⠄⠄
        ⠄⠄⢻⢹⣿⠸⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣿⣿⣿⣿⡟⠄⠄
        ⠄⠄⠈⢸⣿⠄⠙⢿⣿⣿⣹⣿⣿⣿⣿⣟⡃⣽⣿⣿⡟⠁⣿⣿⢻⣿⣿⢿⠄⠄
        ⠄⠄⠄⠘⣿⡄⠄⠄⠙⢿⣿⣿⣾⣿⣷⣿⣿⣿⠟⠁⠄⠄⣿⣿⣾⣿⡟⣿⠄⠄
        ⠄⠄⠄⠄⢻⡇⠸⣆⠄⠄⠈⠻⣿⡿⠿⠛⠉⠄⠄⠄⠄⢸⣿⣇⣿⣿⢿⣿⠄⠄
    """

    # I miss Lua in situations like this...

    BotReply = "🏏🐕 *bonk* go to horny jail";

    def __init__(self):

        self.reddit = praw.Reddit(
            
            user_agent = GetEnv("BotUserName"),
            client_id = GetEnv("ScriptID"),
            client_secret = GetEnv("ScriptSecret"),
            username = GetEnv("BotUsername"),
            password = GetEnv("BotPassword")
            
        );

        self.subreddits = [
            
            self.reddit.subreddit("ZeroTwo"),
            self.reddit.subreddit("ZeroTwoHentai")

        ];

        self.cache = [];

    def CheckSubmissions(self):

        for subreddit in self.subreddits:

            for submission in subreddit.new(limit = 1000):

                if not submission.over_18:

                    print("-------------------------------")
                    print(f"HornyJailBot replied to {submission.title}")

                    self.cache.append(submission.id);
                    # submission.reply(botReply)

    def CheckInbox(self):

        for mention in self.reddit.inbox.mentions:

            pass

    def OnTermination(self):

        with open("RepliedPosts.txt","a") as RepliedPosts:

           for id in self.cache:

               RepliedPosts.write(id + "\n");

        self.cache.clear();
                

