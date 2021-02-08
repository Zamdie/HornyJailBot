import praw; # Imports praw lib
import os; # Imports os lib
from dotenv import load_dotenv; # Imports load_dotenv method from dotenv lib

load_dotenv(); # Loads dotenv

def GetEnv(envName: str) -> str:
    """
    GetEnv function:
    
        Returns the environment variable envName

    Arguments:
        envName -> string - Name of the environment variable

    Returns:
        os.getenv(envName) -> string - Value of the environment variable envName
    """
    return os.getenv(varName);

class HornyJailBot():
    
    """
    This is HornyJailBot's class, which contain all the functions and properties that can be referenced in the main program.
    
    Returns:
        self -> HornyJailBot - Copy of HornyJailBot's class

    Properties:
        self.reddit - Reddit object
        self.subreddits - stores all subreddits
        self.cache - cache containing the ID's of posts that have been already been replied to, when program is interrupted, they are
        appended to RepliedPosts.txt

    Methods:

        __init__ - Constructor, creates a local Reddit object, which then creates self.subreddits with a list of monitored subreddits and
        self.cache to store submission ID's which are written to RepliedPosts.txt on termination

        CheckSubmissions - Loops through the subreddits in self.subreddits and then through the submissions, checks if they are NSFW and
        if they are, bonks it, and appends to self.cache

        OnTermination - Called when program is interrupted, writes things on self.cache to RepliedPosts.txt, and clears it

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

        """
        Function __init__:

        Constructor, creates a local Reddit object, which then creates self.subreddits with a list of monitored subreddits and
        self.cache to store submission ID's which are written to RepliedPosts.txt on termination

        Arguments:

            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """

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

        self.cache = ""

        with open("RepliedPosts.txt","r") as RepliedPosts:

            self.cache = RepliedPosts.read();

    def CheckSubmissions(self):

        """
        Function CheckSubmissions:

        Loops through the subreddits in self.subreddits and then through the submissions, checks if they are NSFW and
        if they are, bonks it, and appends to self.cache

        Arguments:

            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """

        for subreddit in self.subreddits:

            for submission in subreddit.new(limit = 1000):

                if not submission in self.cache:

                    if not submission.over_18:

                        print("-------------------------------")
                        print(f"HornyJailBot replied to {submission.title}")

                        self.cache.append(submission.id);
                        # submission.reply(botReply)

    def CheckInbox(self):

        for mention in self.reddit.inbox.mentions:

            pass

    def OnTermination(self):

        """
        Function OnTermination:

        Called when program is interrupted, writes things on self.cache to RepliedPosts.txt, and clears it

        Arguments:
            
            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """

        with open("RepliedPosts.txt","w") as RepliedPosts:

           for id in self.cache:

               RepliedPosts.write(id + "\n");

        self.cache.clear();
                

