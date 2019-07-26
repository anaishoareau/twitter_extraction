# TWEETER EXTRACTION

 Tweets extraction methods




## Exemple d'utilisation du collecteur

#### IMPORT 
from collect.collect import collect

#### AUTHENTIFICATION (Informations à remplir)
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#### LANCEMENT DE LA COLLECTE (Informations à remplir)
collect('mot_a_tacker',consumer_key, consumer_secret, access_token, access_token_secret, extracted_tweets_dir_path)



## Exemple d'utilisation du listener

#### IMPORT
from listener.listener import Listener

#### AUTHENTIFICATION (Informations à remplir)
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#### DEFINITION DE LA TRACK LIST (Informations à remplir)
track = ['mot_a_tracker_1', 'mot_a_tracker_1']
 
#### INITIALISAITON DE L'ECOUTEUR
listener = Listener(consumer_key, consumer_secret, access_token, access_token_secret, extracted_tweets_dir_path)

#### LANCEMENT DE L'ECOUTE
listener.stream(track)