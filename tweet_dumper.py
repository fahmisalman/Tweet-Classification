#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv
import Preprocessing as pre
import TweetCleaning as tc
import numpy as np
import NaiveBayes as nb


# Twitter API credentials
consumer_key = "swQgOCovVEYIpGJi661shIq3A"
consumer_secret = "7Yi9VD5vcuaGgqLlzXOogvkFNi9mQl8X6gVuFxrPfRqOe9uJgF"
access_key = "152243962-vr7qTmhNiMJ4pS83IcE9z2RuiLKt9GqYs9bTDi7n"
access_secret = "j4mbGiL5xYAa0LVV0tg7xUQXA6B0GbzFpzpi64zI18ZRV"


def get_all_tweets(screen_name):

    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))

    # transform the tweepy tweets into a 2D array that will populate the csv
    # outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
    # print tweet.text.encode("utf-8")

    # write the csv
    # with open('%s_tweets.csv' % screen_name, 'w') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(["id", "created_at", "text"])
    #     writer.writerows(outtweets)
    #
    # pass

    return outtweets


def preprocessing(sentence):
    sentence = pre.caseFolding(sentence)
    token = pre.tokenization(sentence)
    token = pre.stopwordRemoval(token)
    token = pre.lemmatization(token)
    return token


if __name__ == '__main__':
    # pass in the username of the account you want to download
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

    likelihood = np.array(list(csv.reader(open("Model/Emotion/likelihood_emotion.csv"), delimiter=","))) \
        .astype("float")
    prior = np.array(list(csv.reader(open("Model/Emotion/prior_emotion.csv"), delimiter=","))) \
        .astype("float")
    label = np.array(list(csv.reader(open("Model/Emotion/label_emotion.csv"), delimiter=",")))
    words = np.array(list(csv.reader(open("Model/Emotion/words_emotion.csv"), delimiter=",")))

    words = words.tolist()
    label = label.tolist()

    result = []
    for i in range(len(x)):
        print(tweets[i], ' ->', nb.testing(x[i], label[0], words[0], prior[0], likelihood))
