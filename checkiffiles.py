# Reading an id and a date from a filename. Checking if there are files for specific ids between the time period.
# File format id_ddmmyyyy.txt i.e. 1_01012018.txt
import os
import re
from datetime import date, timedelta

files = os.listdir('test_data')
stores = {}

#today = date.today()
today = date(2018, 1, 14)
#two_weeks_ago = today - timedelta(days=14)
two_weeks_ago = date(2018, 1, 1)

for file in files:
	dates = []
	parts = re.split('\W+|_', file)
	if parts[0] not in stores:
		stores[parts[0]] = [parts[1]]
	else:
		stores[parts[0]].append(parts[1])

for store_id, dates in stores.items():
	files_exist = False
	for d in dates:
		day = int(d[0:2])
		month = int(d[2:4])
		year = int(d[4:8])
		this_date = date(year, month, day) 
		if(this_date < today and this_date > two_weeks_ago):
			files_exist = True
	if files_exist:
		print('\n' + store_id + '\tTRUE')
	else:
		print('\n' + store_id + '\tFALSE')