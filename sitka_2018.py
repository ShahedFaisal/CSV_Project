import csv
from datetime import datetime

# Open and load CSV file
infile = open('sitka_weather_2018_simple.csv','r')
csvfile = csv.reader(infile)


# Get header row
header_row = next(csvfile)
print(header_row)


# Get index number of each column
for index,header in enumerate(header_row):
    print(index,header)


# Create list of X and Y axis variables
# (not using list comprehension as csv.reader object is iterable once)
date = []
tmax = []
tmin = []

for row in csvfile:
    date.append(datetime.strptime(row[2], '%Y-%m-%d'))
    tmax.append(int(row[5]))
    tmin.append(int(row[6]))


# Plot X and Y axis variables using matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(date, tmax, c='red')
plt.plot(date, tmin, c='blue')

plt.fill_between(date, tmax, tmin, facecolor='blue', alpha=0.1)
plt.title('Daily Max and Min Temperature in Sitka, 2018', fontsize=16)
plt.xlabel('', fontsize=12)
plt.ylabel('Temperature (F)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=10)

fig.autofmt_xdate()

plt.show()