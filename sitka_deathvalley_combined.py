import csv
from datetime import datetime

# Open both CSV files
infile_st = open('sitka_weather_2018_simple.csv','r')
infile_dv = open('death_valley_2018_simple.csv','r')

# Read both CSV files
csvfile_st = csv.reader(infile_st)
csvfile_dv = csv.reader(infile_dv)

# Get header row and first data row
header_st = next(csvfile_st)
datarow1_st = next(csvfile_st)

header_dv = next(csvfile_dv)
datarow1_dv = next(csvfile_dv)

# Get index values for required columns
index_NAME_st = header_st.index('NAME')
index_DATE_st = header_st.index('DATE')
index_TMAX_st = header_st.index('TMAX')
index_TMIN_st = header_st.index('TMIN')

index_NAME_dv = header_dv.index('NAME')
index_DATE_dv = header_dv.index('DATE')
index_TMAX_dv = header_dv.index('TMAX')
index_TMIN_dv = header_dv.index('TMIN')

# List highs, lows and dates for Sitka
highs_st = []
lows_st = []
dates_st = []

for row in csvfile_st:
    try:
        date_st = datetime.strptime(row[index_DATE_st], "%Y-%m-%d")
        high_st = int(row[index_TMAX_st])
        low_st = int(row[index_TMIN_st])
    except ValueError:
        print(f'Missing data for {date_st}')
    else:
        highs_st.append(high_st)
        lows_st.append(low_st)
        dates_st.append(date_st)

# List highs, lows and dates for Death Valley
highs_dv = []
lows_dv = []
dates_dv = []

for row in csvfile_dv:
    try:
        date_dv = datetime.strptime(row[index_DATE_dv], "%Y-%m-%d")
        high_dv = int(row[index_TMAX_dv])
        low_dv = int(row[index_TMIN_dv])
    except ValueError:
        print(f'Missing data for {date_dv}')
    else:
        highs_dv.append(high_dv)
        lows_dv.append(low_dv)
        dates_dv.append(date_dv)

# Create the subplots
import matplotlib.pyplot as plot

fig = plot.figure()

plot.subplot(2,1,1)
plot.plot(dates_st, highs_st, c='red')
plot.plot(dates_st, lows_st, c='blue')
plot.fill_between(dates_st, highs_st, lows_st, facecolor='blue', alpha=0.1)
plot.title(datarow1_st[index_NAME_st])

plot.subplot(2,1,2)
plot.plot(dates_dv, highs_dv, c='red')
plot.plot(dates_dv, lows_dv, c='blue')
plot.fill_between(dates_dv, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
plot.title(datarow1_dv[index_NAME_dv])

plot.suptitle(f'Temperature comparison between {datarow1_st[index_NAME_st]} and {datarow1_dv[index_NAME_dv]} - 2018')

fig.autofmt_xdate()

plot.show()