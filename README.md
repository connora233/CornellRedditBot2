# Cornell Class Bot

A bot that gives you extra info about classes you're interested in! This is an open source project by the Cornell community for the Cornell community. Note: Cornell Class Bot could easily be adapted for other colleges.

## About
This bot aims to help with the large amount of users asking similar questions about common classes. It checks the most recent 250 posts every 5 minutes to see if a user is calling it. If a post has been previously cached, the bot will skip over it.

If the bot determines that it is being called, it then leverages Google to find helpful posts for the caller. The results are appended to a string and automatically commented by the bot account on Reddit! 

![A screenshot of the bot replying](https://i.imgur.com/PiZT7Vi.png)
###### The bot in action

## Can I help?
Absolutely! This is an open source project and contributions are welcome. All pull requests will be approved by the moderators of `r/Cornell` before being merged.

## Known Issues
1. The CUReview links could be faulty if a CUReview page does not exist for a valid Cornell class.
2. The 5 links posted by the bot may not always be of the highest quality. There is no check beyond leveraging Google currently, and this is where the next iteration of the bot should aim to improve.


## To-do
- [ ] Check CUReview to ensure link is valid
- [ ] Come up with an algorithm to detect whether a Reddit post is discussing important information about the desired class
- [ ] Clean-up/Organize code
