import pandas as pandas
import numpy as numpy
import matplotlib
import seaborn as sns
import glob
import matplotlib.pyplot as plt

all_files = glob.glob("*.csv")

li = []

for filename in all_files:
    df = pandas.read_csv(filename, index_col=None, header=0)
    li.append(df)

us_census = pandas.concat(li, axis=0, ignore_index=True)

us_census['Hispanic'] = us_census['Hispanic'].str.extract(r'(.*)\%$', expand=False)
us_census['White'] = us_census['White'].str.extract(r'(.*)\%$', expand=False)
us_census['Black'] = us_census['Black'].str.extract(r'(.*)\%$', expand=False)
us_census['Native'] = us_census['Native'].str.extract(r'(.*)\%$', expand=False)
us_census['Asian'] = us_census['Asian'].str.extract(r'(.*)\%$', expand=False)
us_census['Pacific'] = us_census['Pacific'].str.extract(r'(.*)\%$', expand=False)

us_census['Hispanic'].fillna(us_census['Hispanic'].mean())
us_census['White'].fillna(us_census['White'].mean())
us_census['Black'].fillna(us_census['Black'].mean())
us_census['Native'].fillna(us_census['Native'].mean())
us_census['Asian'].fillna(us_census['Asian'].mean())
us_census['Pacific'].fillna(us_census['Pacific'].mean())

us_census.drop_duplicates()



extr = us_census['Income'].str.extract(r'^\$(.*)', expand=False)

TotalPop = us_census['TotalPop']
us_census = pandas.DataFrame(us_census.GenderPop.str.split('_',1).tolist(), columns = ['Men','Women'])

extr1 = us_census['Men'].str.extract(r'(.*)M$', expand=False)
extr2 = us_census['Women'].str.extract(r'(.*)F$', expand=False)

us_census['Men'] = pandas.to_numeric(extr1)
us_census['Women'] = pandas.to_numeric(extr2)
us_census['Income'] = pandas.to_numeric(extr)
us_census['TotalPop'] = TotalPop

us_census['Women'].fillna(us_census['TotalPop']-us_census['Men'])

us_census.drop_duplicates()

plt.scatter(us_census['Women'], us_census['Income'])
plt.savefig('myScatterPlot.png')





