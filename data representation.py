import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\Ishaan\\Downloads\\nutrients_csvfile.csv")
df2=df
del df2['Fiber']
del df2['Sat.Fat']
del df2['Grams']
df3=df2.head()
df3['Protein'] = df3['Protein'].astype('int')
colors = ["#F4811F","#EE2526","#008163"]
mine=sns.set_palette(sns.color_palette(colors))
fig, ax = plt.subplots(figsize=(18, 5))
sns.set_style(rc = {'axes.facecolor': '#F2F2F2'})
sns.barplot(x=df3['Protein'], y=df3['Food'], palette=colors)
plt.show()
