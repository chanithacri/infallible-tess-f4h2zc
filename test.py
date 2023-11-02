import json
from collections import defaultdict
data = json.loads(input())
streets_buses = defaultdict(set)
buses_types = defaultdict(set)

for element in data:
    for k, v in element.items():
        if k == 'bus_id' and element['stop_name']:
            streets_buses[element['stop_name']] |= {v}
            buses_types[element[k]] |= {element['stop_type']}
