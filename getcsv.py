import csv


def getName(csvfile):
	name = ""
	with open(csvfile, 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter == 1:
                                name = row[19]
                        counter += 1
		return name

def getUser(csvfile):
	user = ""
	with open(csvfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter == 1:
                                user = row[20]
                        counter += 1
                return user

def getTweets(csvfile):
	tweet = []
	with open(csvfile, 'rb') as csvfile:
		spamreader = csv.reader(csvfile)
                counter = 0
                for row in spamreader:
                        if counter > 0:
                                tweet.append((row[2],row[0],row[1]))
                        if counter == 1:
                                name = row[19]
                                user = row[20]
                        counter += 1
                return tweet
