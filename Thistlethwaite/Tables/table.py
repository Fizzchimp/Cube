class Table():
    def __init__(self, file_name):
        # Read the input file and translate into a table object
        with open(file_name, "r") as file:
            lines = file.readlines()
            self.__table = [None for i in range(len(lines))]
            for i, line in enumerate(lines):
                key, value = line.strip("\n").split(" : ")
                value = value.split(" ")
                self.__table[i] = (key, value)




    def display(self):
        for key in self.__table.keys():
            print(key, ":", self.__table[key])


    def search_table(self, search_key):
        values = []
        for key, value in self.__table:
            if key == search_key:
                values.append(value)

        if len(values) == 0: return None
        elif len(values) == 1: return values[0]
        else: return values

    def __getitem__(self, item):
        return self.search_table(item)