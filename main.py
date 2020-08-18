''' 
Import needed packages:

pip install praw
pip install beautifulsoup4
pip install google
pip install requests
'''

import time
import praw_service

while True:
    # Check recent posts for calls to class bot in comments
    praw_service.reply()
    # Wait 5 minutes between checks
    time.sleep(300)
