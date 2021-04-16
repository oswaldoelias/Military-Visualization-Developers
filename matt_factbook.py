import json

from FactbookAPI.FactbookApi import FactbookApi

api = FactbookApi()

# print(api.countries)
geo = api.getCountry('united_states').geo
print(geo)
with open('./us_geo_example.json', 'w') as f:
    json.dump(geo, f)