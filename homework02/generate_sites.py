import json
import random

data = {}
data['sites'] = []

for i in range(5):
    latitude = random.uniform(16.0, 18.0)
    longitude = random.uniform(82.0, 84.0)
    composition = random.choice(["stony", "iron", "stony-iron"])
    
    data['sites'].append( {'site_id': i + 1,
                           'latitude': latitude,
                           'longitude': longitude,
                           'composition': composition
                          }
                        ) 

with open('sites.json', 'w') as out:
    json.dump(data, out, indent = 2)
