import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

csv_readerOnline = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
csv_readerLocal = pd.read_csv('iris.csv')
fig, ax = plt.subplots()
especies=np.unique(csv_readerOnline['species'])
colors=['r','b','g']
for i in range(0,len(especies)):
    a=ax.scatter(csv_readerOnline[csv_readerOnline['species']==especies[i]].sepal_length,
                 csv_readerOnline[csv_readerOnline['species']==especies[i]].sepal_width,
                 s=10,c=colors[i],label=especies[i])
plt.legend()
plt.show()
fig.savefig("iris_scatter.pdf", bbox_inches='tight')
#sns.scatterplot(x=csv_readerOnline['sepal_length'],y=csv_readerOnline['sepal_width'],hue=csv_readerLocal['species'])
