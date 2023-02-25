# Unified Calculator
#adding values now
import plotly.graph_objects as go
import pandas as pd
mydf=pd.read_excel("C:\\Users\\Ishaan\\Documents\\testing1.xlsx")

xcar=xcal=xp=xf=0
while(True):
    m=input()
    if(m):
        xcal+=mydf[m].iloc[5]
        xf+=mydf[m].iloc[1]
        xcar+=mydf[m].iloc[0]
        xp+=mydf[m].iloc[2]
    else:
        break
        
figcal = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xcal,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': m+" Total Calories", 'font': {'size': 24}},
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

figcal.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

figcal.show()

figcar = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xcar,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Total Carbs", 'font': {'size': 24}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#008163"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 60], 'color': '#F4811F'},
            {'range': [60, 100], 'color': '#EE2526'}],
        'threshold': {
            'line': {'color': "Black", 'width': 4},
            'thickness': 0.75,
            'value': 90}}))

figcar.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

figcar.show()


figp = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xp,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Total Protein", 'font': {'size': 24}},
    gauge = {
        'axis': {'range': [None, 45], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#008163"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 30], 'color': '#F4811F'},
            {'range': [30, 45], 'color': '#EE2526'}],
        'threshold': {
            'line': {'color': "Black", 'width': 4},
            'thickness': 0.75,
            'value': 40}}))

figp.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

figp.show()


figf = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xf,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text':"Total Fat", 'font': {'size': 24}},
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

figf.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

figf.show()

