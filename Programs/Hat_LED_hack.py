###LED Hat Hack###
###TeCoEd###
import os
import time;
import sys, subprocess, urllib, time, tweepy
import RPi.GPIO as GPIO

time.sleep(10)

####TWITTER SECTION###
# == OAuth Authentication ==###############
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key= 'xxxxxxxxxxxxxxxxx'
consumer_secret= 'xxxxxxxxxxxxxxxxxxxxxxxxx'

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
access_token= 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret= 'xxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

 
###CODE TO GET TWITTER TO LISTEN FOR Phrase###
class Crimbo_Lights(tweepy.StreamListener):
    def on_status(self, tweet):
        
        tweet_to_check = tweet.text ##gets the tweet
        print tweet_to_check
        
        ###Checks for tweets to @Your_Twitter_User_ID ###Add Yours
        does_the_tweet_contain_key_word = tweet_to_check.find("@Your_Twitter_User_ID ON")
        ###change to use code to find key word###
        print does_the_tweet_contain_key_word

        if does_the_tweet_contain_key_word == 0:
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(9, GPIO.OUT)
                pic = '/home/pi/lights.jpg' 
                user = str(tweet.user.screen_name)              
                time_sent = time.asctime( time.localtime(time.time()) )
                message = "You turned on the LED Hat!", time_sent
                #print error_tweet
                final_tweet = "@%s" %(user), message
                #print type(error)
                
                ###Turn the lights on
                GPIO.output(9, GPIO.LOW)
                time.sleep(8)
                ###Turn them off
                GPIO.setup(9, GPIO.HIGH) 
                #GPIO.output(10, GPIO.HIGH)lights_on()
                api.update_with_media(pic, final_tweet)
                              
           
        else:
                print "no lights"
                 

     

stream = tweepy.Stream(auth, Crimbo_Lights())            
            
while True:
    stream.userstream()    
