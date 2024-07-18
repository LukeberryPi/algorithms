# https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

def invalid_tweets(tweets):
    return tweets.loc[tweets["content"].str.len() > 15, ["tweet_id"]]