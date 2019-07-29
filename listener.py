# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/
"""

# IMPORTS 
import tweepy
from tweepy import StreamListener
from tweepy import OAuthHandler

from datetime import date
import json, time, sys

# ECOUTEUR 
class Listener(StreamListener):

    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret,
                 extracted_tweets_dir_path):
        
        self.nb_files_per_day = 1
        self.counter = 0
        self.date = date.today()
        self.extracted_tweets_dir_path = extracted_tweets_dir_path
        self.output  = open(extracted_tweets_dir_path + "%s_tweets_%s.json" % (self.date, self.nb_files_per_day), 'w')
        self.delout  = open(extracted_tweets_dir_path + "delete.txt", 'a')
        
        # AUTHENTIFICATION
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    def on_data(self, data):

        if  'in_reply_to_status' in data:
            self.on_status(data)
        
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print(warning['message'])
            return False

    def on_status(self, status):
        
        self.output.write(status + "\n")
        self.counter += 1
        
        if self.counter >= 20000 :
            
            self.nb += 1
            self.output.close()
            self.date = date.today()
            self.output = open(self.extracted_tweets_dir_path + "%s_tweets_%s.json" % (self.date, self.nb_files_per_day), 'w')
            self.counter = 0
            
        if (self.date.year != date.today().year 
            or self.date.month != date.today().month 
            or self.date.day != date.today().day ) :
            
            self.output.close()
            self.date = date.today()
            self.output = open(self.extracted_tweets_dir_path + "%s_tweets_%s.json" % (self.date, self.nb_files_per_day), 'w')
            self.counter = 0
            self.nb_files_per_day = 1
            
        return

    def on_delete(self, status_id, user_id):
        
        self.delout.write(str(status_id) + "\n")
        return

    def on_limit(self, track):

        sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        
        if status_code == 420:
            sys.stderr.write("Error 420 : sleeping for 15 minutes...\n")
            time.sleep(60*15)
            return
        else :
            sys.stderr.write('Error: ' + str(status_code) + "\n")
            return False

    def on_timeout(self):
        
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return 
    
    def stream(self, track_list):
        stream = tweepy.Stream(self.auth, self, tweet_mode = 'extended')
        stream.filter(track = track_list)

