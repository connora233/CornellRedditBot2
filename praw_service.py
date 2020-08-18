import praw
import passwords
import google_service
import cornell_classes

# Create instance of Reddit bot
USERNAME = 'CornellClassBot2'

reddit = praw.Reddit(client_id=passwords.client_id,
                     client_secret=passwords.client_secret,
                     username=USERNAME,
                     password=passwords.password,
                     user_agent='Made by /u/DubitablyIndubitable')


def has_replied(comment):
    """
    Function to check if the bot has replied to a comment
    Input:
    comment - a praw comment object to check
    """
    for reply in comment.replies:
        if reply.author == USERNAME:
            return True
    return False


def respond_relevant(comment):
    """
    Responds to Reddit comments that call upon the bot.
    Input:
    comment - a praw comment object to check
    """
    if "!classbot" in comment.body.lower() and (not has_replied(comment)):
        data = comment.body.lower().split(" ")
        if cornell_classes.valid_class(data[1], data[2]):
            comment.reply(
                cornell_classes.generate_class_output(data[1], data[2]))


def reply():
    """
    Checks the 250 most recent posts to see if the class bot is summoned and
    generates reply.
    """
    for submission in reddit.subreddit('cornell').new(limit=250):
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            respond_relevant(comment)
