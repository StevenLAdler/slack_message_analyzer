import json
import os

from datetime import *
from dateutil.relativedelta import *
from dateutil.parser import *

from loadconfig import GetConfig 

#declare dict
msg_data = {}

def countMessages(path):
	count = 0
	try:
		with open(path, encoding="utf8") as json_file:
			data = json.load(json_file)
		count = len([count for message in data if message["type"]=="message"])
	except:
		count = 0
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

#init dict
for channel in channels:
	msg_data[channel] = []

for item in channels:
	folder = f"{path}/{item}"
	
	start_date = parse(start)
	tmp = start_date.date()
	
	end_date = parse(end)
	e_date = end_date.date()
	
	if inc == "day":
		while tmp <= e_date:
			countMessages(f"{folder}/{tmp}.json")
			#the day isnt incrementing here for some reason
			tmp = tmp+relativedelta(day=+1)
			print(tmp)
			he = input()
			
	
	#elif inc = "week":
	#elif inc = "month":
	#else: