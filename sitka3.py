import csv
from datetime import datetime

infile = open('sitka_weather_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

for index,column_header in enumerate(header_row):
    print(index,column_header)

dates = []
highs = []
lows = []

for row in csvfile:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    highs.append(int(row[5]))
    lows.append(int(row[6]))

import matplotlib.pyplot as plot

fig = plot.figure()

plot.plot(dates, highs, c='red')
plot.plot(dates, lows, c='blue')

plot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plot.title('Daily High and Low Temperatures - 2018\nSitka', fontsize=16)
plot.xlabel('', fontsize=12)
plot.ylabel('Temperature (F)', fontsize=12)
plot.tick_params(axis='both', which = 'major', labelsize=10)

fig.autofmt_xdate()

plot.show()