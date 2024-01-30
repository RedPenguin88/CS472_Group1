import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.dates as mdates
from matplotlib.dates import MonthLocator
from collections import Counter
import matplotlib.cm as cm
import numpy as np
import itertools

# Read data
filename = 'data/authors_rootbeer.csv'
data = []

# Get data from csv
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader) # skip header
    for row in csvreader:
        data.append(row)

# Sort the data by frequency
filenames = [row[0] for row in data]
filename_counts = Counter(filenames)
sorted_filenames = [filename for filename, _ in filename_counts.most_common()]

# Create a mapping of filenames to integers
# This is so the x axis is represented by integers
sorted_data = sorted(data, key=lambda x: sorted_filenames.index(x[0]))
filename_to_int = {}
incr = 0
for filename in sorted_filenames:
    filename_to_int[filename] = incr
    incr+=1

# Get authors and associate unique colors with each author
authors = set([row[1] for row in data])
colors = iter(cm.Paired(np.linspace(0, 1, len(authors))))  # Generate colors for authors
author_colors = {}
for author in authors:
    author_colors[author] = next(colors)

# Finally, create the plot
fig, ax = plt.subplots()
for filename, author, timestamp in sorted_data:
    ax.scatter(filename_to_int[filename], datetime.strptime(timestamp, '%Y-%m-%d'), color=author_colors[author], label=author)

# Set labels and change tick settings
ax.set_xlabel('File')
ax.set_ylabel('Date')
ax.set_title('File Touches Over Time')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.yaxis.set_major_locator(MonthLocator(interval=3))
ax.yaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.show()
