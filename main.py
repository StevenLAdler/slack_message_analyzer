import json
import os
from loadconfig import GetConfig 

def countMessages(path):
	count = 0
	with open(path, encoding="utf8") as json_file:
		data = json.load(json_file)
	count = len([count for message in data if message["type"]=="message"])
	print(count)


#class DataGetter(object):
#	def __init__(self):
#		

cfg = GetConfig()
cfg.readJson()

start = cfg.getStart()
end = cfg.getEnd()
inc = cfg.getIncrement()
path = cfg.getPath()
channels = cfg.getChannels()

for item in channels:
	folder = f"{path}/{item}"
	for file in os.listdir(folder):
		if start <= file <= end:
			countMessages(f"{folder}/{file}")