import pandas as pd
import plotly.express as px


data = {
    'student': ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10'],
    'mathematics': [78, 85, 67, 90, 73, 81, 69, 94, 76, 88]
}

df = pd.DataFrame(data)

fig = px.bar(
    df,
    x = 'student',
    y = 'mathematics',
    title='Mathematics marks of Students',
    labels={'mathematics':'marks','student':'student'},
    text='mathematics'
)

fig.show()