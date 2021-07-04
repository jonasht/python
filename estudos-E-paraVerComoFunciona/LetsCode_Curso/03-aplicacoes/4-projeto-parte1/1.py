from typing import ItemsView
import requests as r


url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)

print(resp.status_code)

raw_data = resp.json()

print(raw_data[0])

for k, v in raw_data[0].items():
    print(f'{k}: {v}')