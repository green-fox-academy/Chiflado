
# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
need_to_contain = [4, 8, 12, 16]

def list_checking(need_to_contain):
    for i in range(len(list_of_numbers)):
        for j in range(len(need_to_contain)):
            if not need_to_contain[j] in list_of_numbers:
                return False
    return True

print(list_checking(need_to_contain))