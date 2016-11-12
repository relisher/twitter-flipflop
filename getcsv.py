import csv

user = ""
name = ""
tweet = []

def initialize(csvfile):
	with open(csvfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
		counter = 0
		for row in spamreader:
			if counter > 0:
				tweet.append((row[2],row[0]))
			if counter == 1:
				name = row[19]
				user = row[20]
			counter += 1 
		print user
		print name
		for item in tweet:
			print item

def getName(csvfile):
	with open(csvfile, 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter > 0:
                                tweet.append((row[2],row[0]))
                        if counter == 1:
                                name = row[19]
                                user = row[20]
                        counter += 1
		return name

def getUser(csvfile):
	with open(csvfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter > 0:
                                tweet.append((row[2],row[0]))
                        if counter == 1:
                                name = row[19]
                                user = row[20]
                        counter += 1
                return user

def getTweets(csvfile):
	with open(csvfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter > 0:
                                tweet.append((row[2],row[0]))
                        if counter == 1:
                                name = row[19]
                                user = row[20]
                        counter += 1
                return tweet
