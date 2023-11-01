        count_128 = 0
        count_256 = 0
        count_512 = 0
        count_1024 = 0
        data = self.data
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format")
        
        for entry in data:
            if entry.get("bus_id") == 128:
                count_128 += 1
            elif entry.get("bus_id") == 256:
                count_256 += 1
            elif entry.get("bus_id") == 512:
                count_512 += 1
            elif entry.get("bus_id") == 1024:
                count_1024 += 1        
        print(f"""
Line names and number of stops:
bus_id: 128, stops: {count_128}
bus_id: 256, stops: {count_256}
bus_id: 512, stops: {count_512}
bus_id: 1024, stops: {count_1024}
        """)
    