#!/usr/bin/python

import praw
import time
import json

reddit = praw.Reddit('bot1')

#subreddit = reddit.subreddit("rbtvcirclejerk")
subreddit = reddit.subreddit('testingground4bots')
start_time = time.time()

#define what the bot should isten to, to not use the default matcher keyword
matcher = "!jep"

print("Welcome " + str(reddit.user.me()) + ", bot has been started sucsessfully!")


#optional validator class
#class Validator:
#    
#    def __init__(self):
#        self.valid = False
#        
#    def validateIfBotReplied(self, comment):
#        pass
#        print("Validator called")
#        for reply in comment.replies:
#            print("Entered Replies")
#            print("Reply: ", reply)
#            #check if already responded
#            self.valid = True 
#        return self.valid
    
    
#optional json parser class   
class JSONParser:
    
    def __init__(self):
        with open('responses.json', 'r') as fileText:
            self.responses = json.load(fileText)
            
    def getAllResponses(self):
        return self.responses

    def getFirstResponse(self):
        return self.getAllResponses()['responses'][1]['response']
    
    

for comment in subreddit.stream.comments():
    if comment.created_utc > start_time:
        if comment.body == matcher:
            comment.reply(JSONParser().getFirstResponse())
            comment.refresh()



#only for test system
#test_sub_matcher = "testground"
#---sumbmission related bot actions---
#for submission in subreddit.stream.submissions():
#    #just for testing purpouses
#    if submission.title == test_sub_matcher:
#        #check the submission itself
#        print("Title: ", submission.title)
#        print("Body: ", submission.selftext)
#        if submission.selftext == matcher:
#                print("Posted Answer!")
#                submission.reply(reply_message)

       
    

    
    
    
