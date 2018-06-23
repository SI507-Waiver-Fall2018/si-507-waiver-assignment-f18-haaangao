# Han Gao / hangao

# these should be the only imports you need
import tweepy
import nltk
import json
import sys
import re
from nltk.corpus import stopwords
from collections import Counter

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
username = sys.argv[1]
num_tweets = sys.argv[2]

# Consumer keys and access tokens, used for OAuth
consumer_key = 's0jdfJmraTepTNKy17sCyKR4a'
consumer_secret = '1NGBtFvjeEjOZT7KbfZZMM6IkMRSiALlyAdHzfB0JWgjo3Gpmh'
access_token = '848842412-HRmTJXbkrWy8QBNFsGbyEZ4NmRUevZh9t1e0klAi'
access_token_secret = 'eEf6ReNi8JMVC0MzOf2OtLzQqisRTlLGZFd6h2KKtJioE'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
public_tweets = api.user_timeline(id=username,num=num_tweets,tweet_mode='extended')

corpus = ""
for tweet in public_tweets:
    corpus += tweet.full_text + " "

tokens = nltk.word_tokenize(corpus)

stopWords = set(stopwords.words('english'))
stopWords.update(['http','https','RT'])

filtered_tokens = []
for w in tokens:
    if w not in stopWords and re.match("[a-zA-Z]", w):
        filtered_tokens.append(w)

tagged_tokens = nltk.pos_tag(filtered_tokens)
# print(tagged_tokens)

tweet_tokens_verb = []
tweet_tokens_noun = []
tweet_tokens_adj = []
for (token,tagger) in tagged_tokens:
    if tagger.startswith('VB'):
        tweet_tokens_verb.append(token)
    elif tagger.startswith('NN'):
        tweet_tokens_noun.append(token)
    elif tagger.startswith('JJ'):
        tweet_tokens_adj.append(token)

def top_five(filtered_tokens):
    tweet_tokens_freq = Counter(filtered_tokens)
    top_five = tweet_tokens_freq.most_common(5)
    common_words = ''
    for token in top_five:
        common_words += token[0] + '(' + str(token[1]) + ') '
    return common_words

# sorted(filtered_tokens, key=lambda s: s.lower() )

# print(top_five(tweet_tokens_noun))

original_tweets = api.user_timeline(id=username,num=num_tweets,include_rts=False,tweet_mode='extended')

fav = 0
for tweet in original_tweets:
    fav += tweet.favorite_count

rt = 0
for tweet in original_tweets:
    rt += tweet.retweet_count

def print_results():
    print('***** Part 1 Output *****')
    print('USER:',username)
    print('TWEETS ANALYZED:', num_tweets)
    print('VERBS: ', top_five(tweet_tokens_verb))
    print('NOUNS: ', top_five(tweet_tokens_noun))
    print('ADJECTIVES: ', top_five(tweet_tokens_adj))
    print('ORIGINAL TWEETS: ', len(original_tweets))
    print('TIMES FAVORITED (ORIGINAL TWEETS ONLY): ', fav)
    print('TIMES RETWEETED (ORIGINAL TWEETS ONLY): ', rt)

print_results()

noun_data = open('noun_data.csv','w')
noun_data.write("Noun,Number\n")

tmp = top_five(tweet_tokens_noun)
words = re.findall('\w+',tmp)
for i,j in zip(words[0::2],words[1::2]):
    noun_data.write(i + "," + j + "\n")

