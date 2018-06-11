#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

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
    new_tweets = api.user_timeline(screen_name=screen_name,count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    # print tweet.text.encode("utf-8")

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)

    pass

#
# if __name__ == '__main__':
#     # pass in the username of the account you want to download
#     get_all_tweets("fahmisalmann")
