#adding values now
import plotly.graph_objects as go
import pandas as pd
mydf=pd.read_excel("C:\\Users\\Ishaan\\Documents\\testing1.xlsx")
print("Fat Calculator")
xr=0
while(True):
    m=input()
    if(m):
        xr+=mydf[m].iloc[1]
    else:
        break


fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xr,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text':"Total Fat", 'font': {'size': 24}},
    delta = {'reference': 600, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 10], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#008163"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 5], 'color': '#F4811F'},
            {'range': [5, 10], 'color': '#EE2526'}],
        'threshold': {
            'line': {'color': "Black", 'width': 4},
            'thickness': 0.75,
            'value': 9}}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "black", 'family': "Arial"})

fig.show()