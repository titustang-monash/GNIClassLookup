import json
import pandas as pd

df = pd.read_excel('OGHIST_2025_10_07.xlsx','Country Analytical History')
s = df.set_index('Name').to_json(orient='index')
# print(s)
with open('data_as_json.json','w') as f:
    f.write(s)
# Copy the printed string into index.html in between backticks (``) just before json.parse()