def key(self):
    all_keys = [] # this is where we will be storing our keys in a list
    # I want us to loop through the length of the data_map checking for keys
    for i in range(len(self.data_map)):
        # if a certain data map in the loop is not none, we need to pick its keys
        if self.data_map[i] is not None:
            # for us to pick keys from that specific data map we need to loop through its Key-Value pairs
            for j in range(len(self.data_map[i])):
                # we pick and append the keys in our list
                all_keys.append(self.data_map[i][j][0])
    return all_keys