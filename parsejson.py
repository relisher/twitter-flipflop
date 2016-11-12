import json
from pprint import pprint

def parseit():
	with open('info.json') as data_file:    
    		data = json.load(data_file)


	anger = data["document_tone"]["tone_categories"][0]["tones"][0]["score"]
	joy = data["document_tone"]["tone_categories"][0]["tones"][3]["score"]
	disgust = data["document_tone"]["tone_categories"][0]["tones"][1]["score"]
	fear = data["document_tone"]["tone_categories"][0]["tones"][2]["score"]
	agree = data["document_tone"]["tone_categories"][2]["tones"][3]["score"]
	all = [anger, joy, disgust, fear, agree]
	print "anger:" + str(all[0]) + " joy: " + str(all[1]) + " disgust: " + str(all[2]) + " fear: " + str(all[3]) + " agree: " + str(all[4])
	return all
