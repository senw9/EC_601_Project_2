import tweepy

auth = tweepy.OAuth1UserHandler(
   "W7M4DZAh3CnXXqTNYXFNZ1u3B", "67FAbzrvLG75ttOaW5xl2L8PWw9DjAMvxYLHsDZnwAVyREuHLN","AAAAAAAAAAAAAAAAAAAAAEqwkQEAAAAA7vT60OvJzNiw844FxwKoRaxoHHo%3D2MfSHhRc2690PhvBjpAYRSxVGaTtSJ3Bij738GYq9Pzq6WeZKv"
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)