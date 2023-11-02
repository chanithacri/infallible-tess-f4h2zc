    def num_stops_per_bus(self):
        buses = json.loads(str(input()))
        dict_ = dict()
        for data in buses:
            dict_.setdefault(data["bus_id"], 0)
            dict_[data["bus_id"]] += 1

        print("Line names and number of stops")
        for key, value in dict_.items():
            print("bus_id: {}, stops: {}".format(key, value))
