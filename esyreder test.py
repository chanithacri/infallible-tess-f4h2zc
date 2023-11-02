import json
import re
from collections import defaultdict


class EasyRider:
    def __init__(self, data):
        self.data = data

    def validate_data(self):
        data = self.data
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        error_counts = {
            "stop_name": 0,
            "stop_type": 0,
            "a_time": 0
        }

        for entry in data:
            stop_name_val = entry.get("stop_name")
            stop_type_val = entry.get("stop_type")
            a_time_val = entry.get("a_time")

            if not isinstance(stop_name_val, str) or not re.fullmatch(r'[A-Z][a-z]+( [A-Z][a-z]+)* (Street|Avenue|Boulevard|Road)', stop_name_val):
                error_counts["stop_name"] += 1
            if not isinstance(stop_type_val, str) or stop_type_val not in ["", "S", "O", "F"]:
                error_counts["stop_type"] += 1
            if not isinstance(a_time_val, str) or not re.fullmatch(r'([01][0-9]|2[0-3]):[0-5][0-9]', a_time_val):
                error_counts["a_time"] += 1

        total_errors = sum(error_counts.values())
        print("Format validation: {} errors".format(total_errors))
        for field, count in error_counts.items():
            print("{}: {}".format(field, count))

    @staticmethod
    def num_stops_per_bus(data):
        dict_ = dict()
        for id_info in data:
            dict_.setdefault(id_info["bus_id"], 0)
            dict_[id_info["bus_id"]] += 1

        print("Line names and number of stops")
        for key, value in dict_.items():
            print("bus_id: {}, stops: {}".format(key, value))

    def validate_and_analyze_data(self):
        bus_data = json.loads(self.data)
        bus_lines = defaultdict(dict)
        first_stops = defaultdict(str)
        stop_types = defaultdict(set)

        for stop_info in bus_data:
            bus_id = stop_info['bus_id']
            stop_name = stop_info['stop_name']
            stop_type = stop_info['stop_type']

            if bus_id not in first_stops:
                first_stops[bus_id] = stop_name
                
            if stop_type in ['S', 'F']:
                if stop_type in bus_lines[bus_id] and bus_lines[bus_id][stop_type] != stop_name:
                    print(f'There are many start or end stops for the line: {bus_id}.')
                    return
                bus_lines[bus_id][stop_type] = stop_name
            stop_types[stop_type].add(stop_name)

        for bus_id in bus_lines:
            if 'S' not in bus_lines[bus_id]:
                print(f'There is no start stop for the line: {bus_id}.')
            if 'F' not in bus_lines[bus_id]:
                print(f'There is no end stop for the line: {bus_id}.')

        for bus_id, stop_name in first_stops.items():
            if bus_lines[bus_id].get('S') is None:
                stop_types['S'].add(stop_name)

        start_stops = sorted(stop_types['S'])
        transfer_stops = sorted(stop_types[''])
        finish_stops = sorted(stop_types['F'])

        print(f"Start stops: {len(start_stops)} {start_stops}")
        print(f"Transfer stops: {len(transfer_stops)} {transfer_stops}")
        print(f"Finish stops: {len(finish_stops)} {finish_stops}")


input_data = input()
bus_info = EasyRider(input_data)
bus_info.validate_and_analyze_data()
