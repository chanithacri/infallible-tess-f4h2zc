def validate_data(data):
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

def num_stops_per_bus(data):
    try:
        
    except Exception:
        ...

            if entry.get("bus_id") == 128:
                count_128 += 1
            elif entry.get("bus_id") == 256:
                count_256 += 1
            elif entry.get("bus_id") == 512:
                count_512 += 1