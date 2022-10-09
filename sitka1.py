import csv

infile = open('sitka_weather_07-2018_simple.csv','r')

csvfile = csv.reader(infile)

header_row = next(csvfile)

for index,column_header in enumerate(header_row):
    print(index,column_header)

highs = []

for row in csvfile:
    highs.append(int(row[5]))

import matplotlib.pyplot as plot

plot.plot(highs, c='red')
plot.title('Daily High Temperatures - July 2018\nSitka', fontsize=16)
plot.xlabel('July 2018', fontsize=12)
plot.ylabel('Temperature (F)', fontsize=12)
plot.tick_params(axis='both', which = 'major', labelsize=10)

plot.show()