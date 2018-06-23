# Han Gao / hangao

# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.offline as offline
import plotly.graph_objs as go
import csv

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

# Open noun data file from part 1 with "umsi" and "15" as user input for "username" and "num_tweets"
x = []
y = []
with open("noun_data.csv", "r", encoding='utf8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        x.append(row["Noun"])
        y.append(int(row["Number"]))
# print(x, y)
data = [go.Bar(
            x=x,
            y=y)]

# py.plot(data, filename='basic-bar')

#plot offline w/o having to authenticate with Plotly API
#image file in png with be downloaded to the root folder
offline.plot(data, filename='part4_viz_image.html', image='png', image_filename='part4_viz_image')