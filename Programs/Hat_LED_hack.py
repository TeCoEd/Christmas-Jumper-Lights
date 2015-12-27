###TeCoEd Hat LED###
import os
import time;
import sys, subprocess, urllib, time, tweepy
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(9, GPIO.OUT)

time.sleep(15)
#GPIO.setup(9, GPIO.IN)

####TWITTER SECTION###
# == OAuth Authentication ==###############
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'xxxxxxxxxxxxx'
consumer_secret= 'xxxxxxxxxxxxxxxx'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'xxxxxxxxxxxxxx'
access_token_secret= 'xxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

##CODE TO GET TWITTER TO LISTEN FOR KEY WORD###
class Crimbo_Lights(tweepy.StreamListener):
    def on_status(self, tweet):
        
        tweet_to_check = tweet.text ##gets the tweet
        print tweet_to_check
        
        ###Checks for tweets to @PiTests
        does_the_tweet_contain_key_word = tweet_to_check.find("@PiTests ON")
        ###change to use code to find key word###
        print does_the_tweet_contain_key_word

        if does_the_tweet_contain_key_word == 0:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(9, GPIO.OUT)
                pic = '/home/pi/lights.jpg' 
                user = str(tweet.user.screen_name)              
                time_sent = time.asctime( time.localtime(time.time()) )
                message = "You turned LED Hat!", time_sent
                #print error_tweet
                final_tweet = "@%s" %(user), message
                #print type(error)
                api.update_with_media(pic, final_tweet)
                ###Turn the lights on
                GPIO.output(9, GPIO.LOW)
                time.sleep(5)
                ###Turn them off
                GPIO.setup(9, GPIO.HIGH) 
                
          
        else:
                print "error"
                 
stream = tweepy.Stream(auth, Crimbo_Lights())            
            
while True:
    stream.userstream()    
