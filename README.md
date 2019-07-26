# TWEETER EXTRACTION

 Méthode d'extraction de tweets avec le package python « tweepy ».



## Manipulations nécessaires et installations

Pour pouvoir travailler avec tweepy, il est nécessaire de posséder un compte Twitter, 
en ayant renseigner un numéro de téléphone valide, d’être connecté, 
et de créer une « application » sur le site https://developer.twitter.com/en/apps, 
via le formulaire proposé à cet effet. Une fois l’application créée, il faut récupérer 
les clés d’accès présentes dans l’onglet « Keys and Tokens » : consumer_key, consumer_secret, 
access_token, access_token_secret.

#### SOURCE :

- Twitter. Authentication, Guide, Access Tokens. developer.twitter.com
https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html

### Installation du package twitter_extraction

#### Vérifier que la commande pip est installée
#### Vérifier que le package python « git » est installé
#### Exécuter la commande : pip install git+https://github.com/anaishoareau/twitter_extraction.git



## Extraction continue de données Twitter avec un écouteur

Un écouteur, comme le StreamListener de tweepy, est un outil qui va permettre de récupérer 
les tweets au fur et à mesure qu’ils sont postés sur Twitter. L’écoute est ciblée en fonction 
d'une liste de mots-clés.

#### FORMAT DE SORTIE :
Autant de fichier JSON que nécessaire par jour (création d'un nouveau ficher tout les 20 000 tweets)
(ex : 2019-07-25_tweets_1.json, 2019-07-25_tweets_2.json... ) à l'emplacement choisi (extracted_tweets_dir_path)

#### SOURCES :

- ROESSLEIN, Joshua. Streaming With Tweepy. Tweepy Documentation.
http://docs.tweepy.org/en/latest/streaming_how_to.html

- HANNA, Axel. Collecting real-time Twitter data with the Streaming API. 16 Octobre 2012.
https://badhessian.org/2012/10/collecting-real-time-twitter-data-with-the-streaming-api/

- ProgramCreek. Python tweepy.RateLimitError() Examples.
https://www.programcreek.com/python/example/94867/tweepy.RateLimitError


### Exemple d'utilisation du listener

#### IMPORT
from listener.listener import Listener

#### AUTHENTIFICATION (Informations à remplir)

##### consumer_key = ""
##### consumer_secret = ""
##### access_token = ""
##### access_token_secret = ""

#### DEFINITION DES CONSTANTES (Informations à remplir)
track = ['mot_a_tracker_1', 'mot_a_tracker_1']

extracted_tweets_dir_path = ""
 
#### INITIALISAITON DE L'ECOUTEUR
listener = Listener(consumer_key, consumer_secret, access_token, access_token_secret, extracted_tweets_dir_path)

#### LANCEMENT DE L'ECOUTE
listener.stream(track)



## Extraction ponctuelle de données Twitter

L’extraction ponctuelle consiste à récupérer tous les tweets encore disponibles dans l’API de Twitter, 
en effet, on ne peut remonter que 10 jours en arrière. Au-delà de cette date, les tweets ne sont plus 
accessibles depuis l’API. 

#### FORMAT DE SORTIE : 
un fichier JSON (ex : 2019-07-25_tweets.json) par jour 
à l'emplacement choisi (extracted_tweets_dir_path)

#### SOURCES :

- SAHNINE, Kadda. L'exploration de données Twitter. Inovia Blog. 19 08 2015. 
http://ksahnine.github.io/datascience/unix/bigdata/2015/08/19/exploration-donnees-twitter.html

- SAHNINE, Kadda. Collect of Tweets Script. GitHub. 13 04 2018. 
https://github.com/ksahnine/datascience-twitter/blob/master/scripts/collect/collect.py


### Exemple d'utilisation du collecteur

#### IMPORT 
from collector.collector import Collector

#### AUTHENTIFICATION (Informations à remplir)

##### consumer_key = ""
##### consumer_secret = ""
##### access_token = ""
##### access_token_secret = ""

#### DEFINITION DES CONSTANTES (Informations à remplir)
track_word = 'mot_a_tracker'

extracted_tweets_dir_path = ""

#### LANCEMENT DE LA COLLECTE
collector = Collector(consumer_key, consumer_secret, access_token, access_token_secret,extracted_tweets_dir_path)
collector.collect(track_word)