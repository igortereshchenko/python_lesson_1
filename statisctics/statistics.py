import plotly.graph_objects as go
from filehandler.csvimport import importHumans as ih

data = ih('../data')

dataset = dict()

# IBIS: 34
# HILTON: 12

for human in data.values():
    for row in human.toList():

        if row[4] in dataset:
            dataset[row[4]]+=1
        else:
            dataset[row[4]]=1

print(dataset)



#
fig = go.Figure(go.Bar(x = list(dataset.keys()), y= list(dataset.values())))
fig.write_html('resuly.html', auto_open= True)



