class Table():
    def __init__(self, file_name):
        # Read the input file and translate into a table object
        with open(file_name, "r") as file:
            lines = file.readlines()
            # Create a list to put entries in
            self.__table = [None for i in range(len(lines))]
            for i, line in enumerate(lines):

                # Identify the key and the set of values
                key, value = line.strip("\n").split(" : ")

                # Split the values into seperate strings
                values = value.split(" ")

                # Enter the key and the values into the table
                self.__table[i] = (key, values)


    # Search the table for any keys that match and return values
    def search_table(self, search_key):
        # List of returned values
        values = []

        for key, value in self.__table:
            if key == search_key: # Matching key found
                values.append(value)

        # If no matching keys found, return None
        if len(values) == 0: return None

        # If just one matching keys found, return the value
        elif len(values) == 1: return values[0]

        # If multiple matching keys found, return all values
        else: return values


    def __getitem__(self, item):
        return self.search_table(item)