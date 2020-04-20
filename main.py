import json
import os

from datetime import *
from dateutil.parser import *

from loadconfig import GetConfig 

#declare dict
msg_data = {}
 
def countMessages(path):
	count = 0
	try:
		with open(path, encoding="utf8") as json_file:
			data = json.load(json_file)
		count = len([1 for message in data if message["type"]=="message"])
	except:
		count = 0
	return count

#class DataGetter(object):
#	def __init__(self):
#		

cfg = GetConfig()
cfg.readJson()

start = cfg.getStart()
end = cfg.getEnd()
inc = cfg.getIncrement()
cont = cfg.getCont()
path = cfg.getPath()
channels = cfg.getChannels()

#init dict
for item in channels:
	msg_data[item] = []

for item in channels:
	folder = f"{path}/{item}"
	
	start_date = parse(start)
	tmp = start_date.date()
	
	end_date = parse(end)
	e_date = end_date.date()
	
	if inc == "day":
		while tmp <= e_date:
			cnt = countMessages(f"{folder}/{tmp}.json")
			tmp += timedelta(days=+1)
			msg_data[item].append((f"{tmp}",cnt))
	elif inc == "week":
		while tmp <= e_date:
			cnt = 0
			one_week = [(tmp + timedelta(days=+i)) for i in range(0,7)]
			tmp = one_week[-1] + timedelta(days=+1)
			for day in one_week:
				if day<=e_date or cont:
					cnt += countMessages(f"{folder}/{day}.json")
			msg_data[item].append((f"{one_week[0]}",cnt))
	elif inc == "month":
		while tmp <= e_date:
			cnt = 0
			one_mon = [(tmp + timedelta(days=+i)) for i in range(0,30)]
			tmp = one_mon[-1] + timedelta(days=+1)
			for day in one_mon:
				if day<=e_date or cont:
					cnt += countMessages(f"{folder}/{day}.json")
			msg_data[item].append((f"{one_mon[0]}",cnt))


#TODO seperate graphing into seperate file, make it look better also
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.plot(*zip(*msg_data["real-good-gamers"]), c='b', marker="s", label='#real-good-gamers')
plt.plot(*zip(*msg_data["video-games"]), c='r', marker="o", label='#video-games')
plt.legend(loc='upper left');



plt.show()



























