#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

#subreddit = reddit.subreddit("rbtvcirclejerk")
subreddit = reddit.subreddit('testingground4bots')

#define what the bot should say
reply_message = "Super important message \n --- \n Posted by bot template \n\n Change this to ... \n\n -- !jep-Bot"
response = reply_message
#define what the bot should isten to, to not use the default matcher keyword
matcher = "!jep"

print(reddit.user.me())



class validator:
    
    def __init__(self):
        self.valid = False
        
    def validateIfBotReplied(self, comment):
        print("Validator called")
        
        
        for reply in comment.replies:
            print("Entered Replies")
            print("Reply: ", reply)
            #check if already responded
            
            self.valid = True
            
        return self.valid
    
    
#only for test system
test_sub_matcher = "testground"

for comment in subreddit.stream.comments():
        print("Comment: ", comment.body)
        if comment.body == matcher:
            if validator().validateIfBotReplied(comment):
                print("Posted Answer!")
                #comment.reply(reply_message)
                #comment.refresh()



#---not planned for submissions---
#for submission in subreddit.stream.submissions():
#    #just for testing purpouses
#    if submission.title == test_sub_matcher:
#        #check the submission itself
#        print("Title: ", submission.title)
#        print("Body: ", submission.selftext)
#        if submission.selftext == matcher:
#                print("Posted Answer!")
#                submission.reply(reply_message)

       
    

    
    
    
