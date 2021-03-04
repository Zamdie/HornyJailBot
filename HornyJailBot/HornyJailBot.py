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
    
    return os.getenv(envName);

class HornyJailBot():
    
    """
    This is HornyJailBot's class, which contain all the functions and properties that can be referenced in the main program
    
    Arguments:

    void -> void

    Returns:
        self -> HornyJailBot - Copy of HornyJailBot's class

    Properties:
        self.reddit - Reddit object
        self.subreddits - stores all subreddits
        self.submissionsCache - cache containing the ID's of posts that have been already been replied to, when program is interrupted, they are
        appended to RepliedPosts.txt
        self.mentionsCache - cache containing the ID's of comments that mention HornyJailBot that have been already been replied to, when program is interrupted, they are
        appended to Mentions.txt

    Methods:

        __init__ - Constructor, creates a self.reddit object, which then creates self.subreddits with a list of monitored subreddits, self.submissionsCache to store submission ID's
        which are written to RepliedPosts.txt on termination, and self.mentionsCache to store mentions ID's which are written to Mentions.txt on termination

        CheckSubmissions - Loops through the subreddits in self.subreddits and then through the submissions, checks if they are NSFW and if they are, bonks them, and
        appends to self.submissionsCache

        CheckInbox - 

        OnTermination - alled when program is interrupted, writes ID's on self.submissionsCache to RepliedPosts.txt, ID's on self.mentionsCache to Mentions.txt and clears
        them

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

        Constructor, creates a self.reddit object, which then creates self.subreddits with a list of monitored subreddits, self.submissionsCache
        to store submission ID's which are written to RepliedPosts.txt on termination, and self.mentionsCache to store mentions ID's which
        are written to Mentions.txt on termination

        Arguments:

            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """

        self.reddit = praw.Reddit( # Gets Reddit
            
            user_agent = GetEnv("BotName"), # Get env variable BotName
            client_id = GetEnv("ScriptID"), # Get env variable ScriptID
            client_secret = GetEnv("ScriptSecret"), # Get env variable ScriptSecret
            username = GetEnv("BotUsername"), # Get env variable BotUsername
            password = GetEnv("BotPassword") # Get env variable BotPassword
            
        );

        self.subreddits = [ # List of subreddits
            
            self.reddit.subreddit("ZeroTwo"), # r/ZeroTwo
            # self.reddit.subreddit("ZeroTwoHentai"), #  (banned) r/ZeroTwoHentai
            # self.reddit.subreddit("DarlingInTheFranxx") # (banned) r/DarlingInTheFranxx
            self.reddit.subreddit("Horimiya"),
            # self.reddit.subreddit("HornyJailBot") # Debug
        ];

        self.submissionsCache = ""; # Cache for submissions
        self.mentionsCache = ""; # Cache for mentions

        with open("RepliedPosts.txt","r") as RepliedPosts: # Continues as RepliedPosts being the text file

            self.submissionsCache = RepliedPosts.read(); # Sets submissionsCache to the contents of RepliedPosts

        with open("Mentions.txt","r") as Mentions: # Continues as Mentions being the text file

            self.mentionsCache = Mentions.read(); # Sets mentionsCache to the contents of Mentions

    def CheckSubmissions(self):

        """
        Function CheckSubmissions:

        Loops through the subreddits in self.subreddits and then through the submissions, checks if they are NSFW and
        if they are, bonks them, and appends to self.submissionsCache

        Arguments:

            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """

        try: # Try for errors such as the post not existing anymore

            for subreddit in self.subreddits: # Loops through the subreddits

                for submission in subreddit.new(limit = 25): # Loops through 50 posts in the new category of the subreddit

                    if not submission.id in self.submissionsCache: # If the submission ID is not in the cache

                        if submission.over_18: # If submission is NSFW

                            print("-------------------------------");
                            print(f"HornyJailBot replied to {submission.title}"); # Log stuff

                            submission.reply(self.BotReply); # Reply
                            self.submissionsCache += submission.id + "\n"; # Append submission ID to cache

        except Exception as exception:
            
            print(exception) # Log exception
            self.submissionsCache += submission.id + "\n"; # Append submission ID to cache or else it's gonna error every iteration


    def CheckInbox(self):
        
        """
        Function CheckInbox:

        Loops through all mentions, checks if they have been already mentioned and if not, bonks the parent comment (if it is under the submission, bonks the submission), and appends to self.mentionsCache

        Arguments:

            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """
        
        try: # Try for errors such as the parent submission/comment not existing anymore

            for mention in self.reddit.inbox.mentions(): # Loops through the mentions

                if not mention.id in self.mentionsCache: # If comment's ID is not in the cache

                    print("-------------------------------")
                    print(f"HornyJailBot replied to mention: {mention.body} by {mention.author}"); # Log stuff

                    mention.parent().reply(self.BotReply) # Reply to parent comment
                    self.mentionsCache += mention.id + "\n"; # Append comment ID to cache

        except Exception as exception:
            
            print(exception) # Log exception
            self.mentionsCache += mention.id + "\n"; # Append mention ID to cache or else it's gonna error every iteration



    def OnTermination(self):

        """
        Function OnTermination:

        Called when program is interrupted, writes ID's on self.submissionsCache to RepliedPosts.txt, ID's on self.mentionsCache to Mentions.txt and clears them

        Arguments:
            
            self -> HornyJailBot - HornyJailBot object

        Returns:

            void -> void
        """
        
        with open("RepliedPosts.txt","w") as RepliedPosts: # Continues as RepliedPosts being the text file

            RepliedPosts.write(self.submissionsCache); # Write submissionsCache to RepliedPosts

        with open("Mentions.txt","w") as Mentions: # Continues as Mentions being the text file

            Mentions.write(self.mentionsCache); # Write submissionsCache to Mentions

        self.submissionsCache = None; # Clear submissionsCache
        self.mentionsCache = None; # Clear mentionsCache
