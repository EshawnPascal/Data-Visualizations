import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Get dates, daily high and low temperatures from file
filename = 'Ny_Nov_2016.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, means, lows = [], [], [], []
    for row in reader:
        # dates recorded
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        # high temperatures
        high = float(row[1])
        highs.append(high)
        # mean temperatures
        mean = float(row[2])
        means.append(mean)
        # low temperatures
        low = float(row[3])
        lows.append(low)

# Plot data
fig = plt.figure(dpi=90, figsize=(6, 6))
daily_high,=plt.plot(dates, highs, c='red', alpha=0.9)
daily_averages,=plt.plot(dates, means, c='blue', alpha=0.9)
daily_low,=plt.plot(dates, lows, c='black', alpha=0.9)
plt.fill_between(dates, highs, means, facecolor='green', alpha=0.3)
plt.fill_between(dates, means, lows, facecolor='orange', alpha=0.3)
plt.legend([daily_high, daily_averages, daily_low], ["Daily Highs", "Daily Averages", "Daily Lows"])

# Format data
plt.title('Daily Temperatures - Nov 2016 - New York, NY', fontsize=18)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.grid()

plt.show()
