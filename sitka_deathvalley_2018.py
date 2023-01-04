import csv
from datetime import datetime

# Create function to get data from CSV file
def get_csv_data(filename):

    # Open and load CSV file
    infile = open(filename,'r')
    csvfile = csv.reader(infile)

    # Get header row and first datarow
    header = next(csvfile)
    datarow1 = next(csvfile)

    # Get index number of required columns
    index_name = header.index('NAME')
    index_date = header.index('DATE')
    index_tmax = header.index('TMAX')
    index_tmin = header.index('TMIN')

    # Create list of X and Y axis variables
    # (not using list comprehension as csv.reader object is iterable once)
    tmax = []
    tmin = []
    date = []

    for row in csvfile:
        try:
            dt = datetime.strptime(row[index_date], "%Y-%m-%d")
            mx = int(row[index_tmax])
            mn = int(row[index_tmin])
        except ValueError:
            print(f'Missing data on {dt}')
        else:
            date.append(dt)
            tmax.append(mx)
            tmin.append(mn)
        
    return date, tmax, tmin, datarow1, index_name


# Get data from CSV files using the function
st = get_csv_data('sitka_weather_2018_simple.csv')
dv = get_csv_data('death_valley_2018_simple.csv')


# Plot X and Y axis variables using matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(st[0], st[1], c='red')
plt.plot(st[0], st[2], c='blue')
plt.fill_between(st[0], st[1], st[2], facecolor='blue', alpha=0.1)
plt.title(st[3][st[4]])

plt.subplot(2,1,2)
plt.plot(dv[0], dv[1], c='red')
plt.plot(dv[0], dv[2], c='blue')
plt.fill_between(dv[0], dv[1], dv[2], facecolor='blue', alpha=0.1)
plt.title(dv[3][dv[4]])

plt.suptitle(f'Temperature comparison between {st[3][st[4]]} and {dv[3][dv[4]]}, 2018')

fig.autofmt_xdate()

plt.show()