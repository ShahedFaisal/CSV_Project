import csv
from datetime import datetime

infile = open('death_valley_2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

for index,column_header in enumerate(header_row):
    print(index,column_header)

dates = []
highs = []
lows = []

for row in csvfile:
    try:
        date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f'Missing data for {date}')
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

import matplotlib.pyplot as plot

fig = plot.figure()

plot.plot(dates, highs, c='red')
plot.plot(dates, lows, c='blue')

plot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plot.title('Daily High and Low Temperatures - 2018\nDeath Valley', fontsize=16)
plot.xlabel('', fontsize=14)
plot.ylabel('Temperature (F)', fontsize=14)
plot.tick_params(axis='both', which = 'major', labelsize=12)

fig.autofmt_xdate()

plot.show()