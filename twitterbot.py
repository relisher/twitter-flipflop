import tweepy

auth = tweepy.OAuthHandler("xmE8yTuZ65lFReEbDUEIn5aqV", "z0tlMMPm7fxmIM5o21cbhfG5SS0NPgBLF6w4YxhyR0kCi4eeyE")
auth.set_access_token("797478447283077121-LsPU9sTIlxD7Mp54hYtoH1N9mR86rUV", "HAI9RdL4Mci6c2V5fAt4eK0wO3Geyat1Oq7KAxDINTKlu")

api = tweepy.API(auth)

statuses = tweepy.Cursor(api.user_timeline, max_id="796897928048766976", user_id="25073877", count="200").items()

for s in statuses:
    if("obama" in s.text.lower()):
        print(s.text)
