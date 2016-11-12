import tweepy

auth = tweepy.OAuthHandler("xmE8yTuZ65lFReEbDUEIn5aqV", "z0tlMMPm7fxmIM5o21cbhfG5SS0NPgBLF6w4YxhyR0kCi4eeyE")
auth.set_access_token("797478447283077121-LsPU9sTIlxD7Mp54hYtoH1N9mR86rUV", "HAI9RdL4Mci6c2V5fAt4eK0wO3Geyat1Oq7KAxDINTKlu")

api = tweepy.API(auth)

statusesTrump = tweepy.Cursor(api.user_timeline, user_id="25073877", count="1000").items()
statusesClinton = tweepy.Cursor(api.user_timeline, user_id="1339835893", count="1000").items;

trumpObama =[];
trumpRigged = [];
trumpObamacare = [];
trumpGay = [];
clintonTPP = [];
clintonRussia = [];
clintonGay = [];
clintonKeystone =[];

for s in statusesTrump:
    if("rigged" in s.text.lower()):
        trumpRigged.append(s)
    else if("obamacare" in s.text.lower()):
        trumpObamacare.append(s)
    else if("gay" in s.text.lower()):
        trumpGay.append(s)
    else if("obama" in s.text.lower()):
        trumpObama.append(s)

for s in statusesClinton:
    if("tpp" in s.text.lower()):
        clintonTPP.append(s)
    else if("russia" in s.text.lower()):
        clintonRussia.append(s)
    else if("keystone" in s.text.lower()):
        clintonKeystone.append(s)
    else if("gay" in s.text.lower()):
        clintonGay.append(s)
