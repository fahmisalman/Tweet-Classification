import tweepy
import csv
import Preprocessing as pre
import TweetCleaning as tc
import numpy as np
import NaiveBayes as nb
from Secret import *


# consumer_key = ""
# consumer_secret = ""
# access_key = ""
# access_secret = ""


def get_all_tweets(screen_name):

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    alltweets = []

    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    alltweets.extend(new_tweets)

    oldest = alltweets[-1].id - 1

    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        alltweets.extend(new_tweets)

        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
    return outtweets


def preprocessing(sentence):
    sentence = pre.caseFolding(sentence)
    token = pre.tokenization(sentence)
    token = pre.stopwordRemoval(token)
    token = pre.lemmatization(token)
    return token


if __name__ == '__main__':
    tweets = get_all_tweets("")

    x = []

    for i in range(len(tweets)):
        x.append(tc.url_removal(tc.hashtag_removal(tc.at_removal(str(tweets[i][0])))))
        x[i] = preprocessing(x[i])

    i = 0
    while i < len(x):
        if len(x) == 0:
            tweets.pop(i)
            x.pop(i)
        else:
            i += 1

    likelihood_emotion = np.array(list(csv.reader(open("Model/Emotion/likelihood_emotion.csv"), delimiter=","))).astype("float")
    prior_emotion = np.array(list(csv.reader(open("Model/Emotion/prior_emotion.csv"), delimiter=","))).astype("float")
    label_emotion = np.array(list(csv.reader(open("Model/Emotion/label_emotion.csv"), delimiter=",")))
    words_emotion = np.array(list(csv.reader(open("Model/Emotion/words_emotion.csv"), delimiter=",")))
    likelihood_gender = np.array(list(csv.reader(open("Model/Gender/likelihood_gender.csv"), delimiter=","))).astype("float")
    prior_gender = np.array(list(csv.reader(open("Model/Gender/prior_gender.csv"), delimiter=","))).astype("float")
    label_gender = np.array(list(csv.reader(open("Model/Gender/label_gender.csv"), delimiter=",")))
    words_gender = np.array(list(csv.reader(open("Model/Gender/words_gender.csv"), delimiter=",")))

    words_emotion = words_emotion.tolist()
    label_emotion = label_emotion.tolist()
    words_gender = words_gender.tolist()
    label_gender = label_gender.tolist()

    result = []
    for i in range(len(x)):
        print(tweets[i], ' -> (', nb.testing(x[i], label_emotion[0], words_emotion[0],
                                             prior_emotion[0], likelihood_emotion),' --- ',
              nb.testing(x[i], label_gender[0], words_gender[0], prior_gender[0], likelihood_gender),')')
