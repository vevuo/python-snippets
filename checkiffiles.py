# Reading an id and a date from a filename. Checking if there are files for specific ids between the time period in predetermined order.
# File format i.e. 3_20181109101623.csv
import os
import re
from datetime import date, timedelta, datetime

files = os.listdir('test_data')
store_id_order = [14,6,3,7,1,2,4,8,10,11,12,15,16,18,22,5,19,13,20,24,21,23]
stores = {}
today = date.today()
two_weeks_ago = today - timedelta(days=14)

# Splitting file names to a dictionary i.e. { '3': ['20181109101623', '20181104101321'], '14': [...
for file in files:
	parts = re.split('\W+|_', file)
	if parts[0] not in stores:
		stores[parts[0]] = [parts[1]]
	else:
		stores[parts[0]].append(parts[1])

'''
Comparing the ids in "store_list_order" list to the ids in "stores" dict,
converting the string i.e. "20181109101623" to an actual date and
comparing if the date is between the last two weeks.
'''
for store_id in store_id_order:
	files_exist = False
	for s_id, s_date_list in stores.items():
		if int(store_id) == int(s_id):
			for s_date in s_date_list:
				year = int(s_date[0:4])
				month = int(s_date[4:6])
				day = int(s_date[6:8])
				parsed_date = date(year, month, day)
				if(parsed_date <= today and parsed_date >= two_weeks_ago):
					files_exist = True
	if files_exist:
		print('\n' + str(store_id) + '\tTRUE')
	else:
		print('\n' + str(store_id) + '\tFALSE')
