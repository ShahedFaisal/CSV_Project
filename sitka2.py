import csv
from datetime import datetime

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

#print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)

dates = []
highs = []

for row in csvfile:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    highs.append(int(row[5]))

import matplotlib.pyplot as plot

fig = plot.figure()

plot.plot(dates, highs, c='red')
plot.title('Daily High Temperatures - July 2018\nSitka', fontsize=16)
plot.xlabel('', fontsize=12)
plot.ylabel('Temperature (F)', fontsize=12)
plot.tick_params(axis='both', which = 'major', labelsize=10)

fig.autofmt_xdate()

plot.show()