import tweepy

trumpObama =[]
trumpRigged = []
trumpObamacare = []
trumpGay = []
clintonTPP = []
clintonRussia = []
clintonGay = []
clintonKeystone =[]

def search():
    auth = tweepy.OAuthHandler("xmE8yTuZ65lFReEbDUEIn5aqV", "z0tlMMPm7fxmIM5o21cbhfG5SS0NPgBLF6w4YxhyR0kCi4eeyE")
    auth.set_access_token("797478447283077121-LsPU9sTIlxD7Mp54hYtoH1N9mR86rUV", "HAI9RdL4Mci6c2V5fAt4eK0wO3Geyat1Oq7KAxDINTKlu")

    api = tweepy.API(auth)

    statusesTrump = tweepy.Cursor(api.user_timeline, user_id="25073877", count="100").items()
    statusesClinton = tweepy.Cursor(api.user_timeline, user_id="1339835893", count="100").items();


    for s in statusesTrump:
        if(!s.text.startsWith("RT")):
            if("rigged" in s.text.lower()):
                trumpRigged.append(s)
            elif("obamacare" in s.text.lower()):
                trumpObamacare.append(s)
            elif("gay" in s.text.lower()):
                trumpGay.append(s)
            elif("obama" in s.text.lower()):
                trumpObama.append(s)

    for s in statusesClinton:
        if(!s.text.startsWith("RT")):
            if("tpp" in s.text.lower()):
                clintonTPP.append(s)
            elif("russia" in s.text.lower()):
                clintonRussia.append(s)
            elif("keystone" in s.text.lower()):
                clintonKeystone.append(s)
            elif("gay" in s.text.lower()):
                clintonGay.append(s)

    return

def getClintonGay():
    return clintonGay
def getTrumpGay():
    return trumpGay
def getTrumpObama():
    return trumpObama
def getTrumpRigged():
    return trumpRigged
def getTrumpObamacare():
    return trumpObamacare
def getClintonTPP():
    return clintonTPP
def getClintonRussia():
    return clintonRussia
def getClintonKeystone():
    return clintonKeystone
