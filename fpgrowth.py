from fpgrowth_py import fpgrowth
import pandas as pd

df = pd.read_csv('toronto_accidents_trimmed.csv')
print(df.head())
list = []

# selects the lines for fpgrowth
for index, row in df.iterrows():
    # list.append([ row['LIGHT'], row['LOCCOORD'], row['NEIGHBOURHOOD_158'], row['RDSFCOND'], row['INJURY'], row['ACCLASS'], row['VEHTYPE']])
    list.append([row['NEIGHBOURHOOD_158'], row['INJURY'] ])

# fpgrowth
freq, rules = fpgrowth(list, minSupRatio = 0.01, minConf = 0.2)
for i in rules:
    print(i)