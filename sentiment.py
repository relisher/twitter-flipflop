import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
   username='65007b47-f861-472e-9716-d832227af4cf',
   password='HKOLUotXGrY7',
   version='2016-05-19&sentences=false')

def analyze(tweet):
	x = json.dumps(tone_analyzer.tone(text=tweet), indent=2)
	open("info.json", "w").close()
	f = open('info.json', 'r+')
	f.write(x)
	print("finished parse")
	f.close()
