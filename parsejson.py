import json
from pprint import pprint

with open('info.json') as data_file:    
    data = json.load(data_file)


anger = data["document_tone"]["tone_categories"][0]["tones"][0]["score"]
joy = data["document_tone"]["tone_categories"][0]["tones"][3]["score"]
disgust = data["document_tone"]["tone_categories"][0]["tones"][1]["score"]
fear = data["document_tone"]["tone_categories"][0]["tones"][2]["score"]
agree = data["document_tone"]["tone_categories"][2]["tones"][3]["score"]

pprint(agree)
