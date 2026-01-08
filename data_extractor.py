import json
import pandas as pd

df = pd.read_excel('OGHIST_2025_10_07.xlsx','Country Analytical History')
s = df.set_index('Name').to_json(orient='index')
print(s)
# Copy the printed string into index.html