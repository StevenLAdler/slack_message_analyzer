# slack_message_analyzer
* Generate chart to see message quantity trends
* Start and end dates along with backup path and channel list are set in config.json

JSON parameters:
"start" 	: start date for data to be used
"end"		: end date for data to be used
"increment"	: increment of each data point to be displayed
"cont"		: finish the final week/month even if it goes past end date
"path"		: path of base folder of slack export
"channels"	: list of channels to be compared
