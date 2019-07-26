# -*- coding: utf-8 -*-

"""
Auteur : Anaïs HOAREAU
Date : 07/2019
GitHub : https://github.com/anaishoareau
Linkedin : https://www.linkedin.com/in/ana%C3%AFs-hoareau-a2a042183/

"""

""" 
Il ne doit pas y avoir de fichier pour les 10 derniers jours, 
sinon le code réécrit les mêmes tweets que ceux déjà présents dans 
les fichiers correspondants.
"""
# IMPORTS 
import tweepy
from tweepy import OAuthHandler
import json

# CONSTANTES GENERALES
#max_tweets : Nombre de tweet max a recuperer
#tw_block_size : Nombre de Tweet par requete
#since_id : Recuperation des tweets du plus recent au plus ancien
    
# FONCTION D'EXTRACTION DES TWEETS SUR LES 10 DERNIERS JOURS

class Collector(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret, extracted_tweets_dir_path):
        
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.extracted_tweets_dir_path = extracted_tweets_dir_path
        
        # AUTHENTIFICATION
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
    def collect(self, search_query, max_tweets = 10000000, tw_block_size = 3000, since_id = None):
        
        # INITIALISATION DES VARIABLES
        tweet_count = 0
        max_id = -1
        
        # EXTRACTION
        while tweet_count < max_tweets:
                try:
                    if (max_id <= 0):
                        if (not since_id):
                             new_tweets = self.api.search(q=search_query, count=tw_block_size, tweet_mode ='extended')
                        else:
                             new_tweets = self.api.search(q=search_query, count=tw_block_size, since_id=since_id, tweet_mode ='extended')
                    else:
                        if (not since_id):
                             new_tweets = self.api.search(q=search_query, count=tw_block_size, max_id=str(max_id - 1), tweet_mode ='extended')
                        else:
                             new_tweets = self.api.search(q=search_query, count=tw_block_size, max_id=str(max_id - 1), since_id=since_id, tweet_mode ='extended')
    
                    if not new_tweets:
                        print("Collecte terminee.")
                        break
                    for tweet in new_tweets:
                        day = tweet.created_at.strftime('%Y-%m-%d')
                        with open( "%s\\%s_tweets.json" % (self.extracted_tweets_dir_path, day), 'a') as f:
                            f.write(json.dumps(tweet._json))
                            f.write('\n')
                    tweet_count += len(new_tweets)
                    print("{0} tweets téléchargés".format(tweet_count))
                    max_id = new_tweets[-1].id
                except tweepy.TweepError as e:
                    print("Une erreur est intervenue.")
                    print("Error : " + str(e))
                    break
