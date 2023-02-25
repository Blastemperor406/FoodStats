
#adding values now
import plotly.graph_objects as go
import pandas as pd
mydf=pd.read_excel("C:\\Users\\Ishaan\\Documents\\testing1.xlsx")
print("calories calculator")
xr=0
while(True):
    m=input()
    if(m):
        xr+=mydf[m].iloc[5]
    else:
        break

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xr,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': m+" Total Calories", 'font': {'size': 24}},
    delta = {'reference': 600, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 600], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#008163"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 350], 'color': '#F4811F'},
            {'range': [350, 600], 'color': '#EE2526'}],
        'threshold': {
            'line': {'color': "Black", 'width': 4},
            'thickness': 0.75,
            'value': 500}}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "black", 'family': "Arial"})

fig.show()