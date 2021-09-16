import pandas as pd
df = pd.read_csv (r'C:\Users\Hira- Personal\Desktop\data.csv')
index=df.index
numberofrows=len(index)
print('First Printed Answer:\nTotal Number of rows are=',numberofrows)

adf=df[pd.to_numeric(df['Profit (in millions)'], errors='coerce').notnull()]
index=adf.index
numberofrows=len(index)

adf.to_json (r'C:\Users\Hira- Personal\Desktop\data2.json')
print('\nSecond Printed Answer:\nTotal Number of rows after removing\nnon-numeric values from profit coloums are=',numberofrows)

print('\nThird Printed Answer:\nlist of First 20 vlaues by Max profit')
sd=adf.sort_values('Profit (in millions)', ascending=False).head(20)
print(sd)
