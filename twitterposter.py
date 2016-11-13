import tweepy
import getcsv
import parsejson
import sentiment
import math
import twitterposter
import random
auth = tweepy.OAuthHandler("xmE8yTuZ65lFReEbDUEIn5aqV", "z0tlMMPm7fxmIM5o21cbhfG5SS0NPgBLF6w4YxhyR0kCi4eeyE")
auth.set_access_token("797478447283077121-LsPU9sTIlxD7Mp54hYtoH1N9mR86rUV", "HAI9RdL4Mci6c2V5fAt4eK0wO3Geyat1Oq7KAxDINTKlu")

api = tweepy.API(auth)

class twitterposter:

	def __init__(self):
		self.counter = 0
        	self.topic = []
        	self.tweetlist = []
		
	
	def newtweet(self, top, id, neg, pos, rando):
		message = self.topic[top][0][1] + " just changed their opinion on " + self.topic[top][0][2]
		if (self.topic[top][2] > self.topic[top][3] and pos > neg):
			m = api.get_status(id)
			a = m.text + rando
			api.update_status(status=a)
			api.retweet(self.topic[top][1])
			api.update_status(status=message)
			self.topic[top][1] = id
			self.topic[top][2] = neg
			self.topic[top][3] = pos
		elif (self.topic[top][2] < self.topic[top][3] and neg > pos):
			m = api.get_status(id)
			a = m.text + rando
                        api.update_status(status=a)
                        api.retweet(self.topic[top][1])
                        api.update_status(status=message)
                        self.topic[top][1] = id
                        self.topic[top][2] = neg
                        self.topic[top][3] = pos	
	def addtopic(self, name, issue, id, neg, pos):
		self.topic.append([[self.counter, name, issue], id, neg, pos])
		self.counter += 1
		print self.counter-1
		return self.counter-1

	def run(self, file, number):
	        name = getcsv.getName(file)
	        user = getcsv.getUser(file)
	        tweet = getcsv.getTweets(file)
	        for item in tweet:
	                print item
	                body = item[0]
	                date = item[1]
	                id = item[2]
	                sentiment.analyze(body)
	                emote = parsejson.parseit()
	                neg = max(max(emote[0], emote[2]), emote[3])
	                pos = emote[1]
	                self.tweetlist.append((body, name, user, date, id, neg, pos))
	        for item in self.tweetlist:
			rando = str(random.randint(0,100))
	                self.newtweet(number, item[4], item[5], item[6], rando)
