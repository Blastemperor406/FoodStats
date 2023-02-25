#adding values now
print("Carbs Calculator")
xr=0
while(True):
    m=input()
    if(m):
        xr+=mydf[m].iloc[0]
    else:
        break
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = xr,
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

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "black", 'family': "Arial"})

fig.show()