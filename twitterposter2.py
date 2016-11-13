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
		message = self.topic[top][0][1] + " just changed their opinion on " + self.topic[top][0][2] + rando
		if (self.topic[top][2] > self.topic[top][3] and pos > neg):
			print ("a" + str(self.topic[top][1]))
			print ("id" + str(id))
			m = api.get_status(id)
			a = m.text[:136] + rando
			api.update_status(status=a)
			api.retweet(self.topic[top][1])
			api.update_status(status=message)
			self.topic[top][1] = id
			self.topic[top][2] = neg
			self.topic[top][3] = pos
		elif (self.topic[top][2] < self.topic[top][3] and neg > pos):
			print ("a" + str(self.topic[top][1]))
			print ("id" + str(id))
			m = api.get_status(id)
			a = m.text[:136] + rando
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
	
	def runp(self, file, number):
		name = file[0].user.name
	        user = file[0].user.screen_name
	        tweet = []
		for it in file:
		        print it.id_str
			body = it.text
			num = int(it.id_str)
			sentiment.analyze(body)
	                emote = parsejson.parseit()
	                neg = max(max(emote[0], emote[2]), emote[3])
	                pos = emote[1]
			self.tweetlist.append((body, name, user, "10-10-10", num, neg, pos))
		for item in self.tweetlist:
                        rando = str(random.randint(0,100))
                        print item[4]
 			self.newtweet(number, item[4], item[5], item[6], rando)
	
	def run(self, file, number):
	        name = getcsv.getName(file)
	        user = getcsv.getUser(file)
	        tweet = getcsv.getTweets(file)
	        for item in tweet:
	                #print item
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
