class Table():
    def __init__(self, file_name):
        with open(file_name, "r") as file:
            lines = file.readlines()
            self.__table = dict()
            for i, line in enumerate(lines):
                key, value = line.strip("\n").split(" : ")
                value = value.split(" ")
                self.__table[key] = value




    def display(self):
        for key in self.__table.keys():
            print(key, ":", self.__table[key])


    def search_table(self, item):
        try: return self.__table[item]
        except KeyError: return None

    def __getitem__(self, item):
        return self.search_table(item)