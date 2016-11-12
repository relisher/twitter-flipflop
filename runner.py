import getcsv as getcsv
import parsejson
import sentiment
import math

tweets = []

def run(file):
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
		tweets.append((body, name, user, date, id, neg, pos))
	print tweets





