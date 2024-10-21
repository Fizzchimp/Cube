def translate_table(lines):
    moves = []
    for line in lines:
        moves = line[:28]
        print(moves + "|")
        



def make_table():
    with open("phase_4_input.txt", "r") as file:
        lines = file.readlines()
        
with open("phase_4_input.txt", "r") as file:
    lines = file.readlines()
    translate_table(lines)