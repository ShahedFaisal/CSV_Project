import csv
from datetime import datetime

# Open and load CSV file
infile = open('death_valley_2018_simple.csv','r')
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
    try:
        dt = datetime.strptime(row[2], "%Y-%m-%d")
        mx = int(row[4])
        mn = int(row[5])
    # To handle missing values
    except ValueError:
        print(f'Missing data on {dt}')
    else:
        date.append(dt)
        tmax.append(mx)
        tmin.append(mn)


# Plot X and Y axis variables using matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(date, tmax, c='red')
plt.plot(date, tmin, c='blue')

plt.fill_between(date, tmax, tmin, facecolor='blue', alpha=0.1)
plt.title('Daily Max and Min Temperatures in Death Valley, 2018', fontsize=16)
plt.xlabel('', fontsize=14)
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which = 'major', labelsize=12)

fig.autofmt_xdate()

plt.show()