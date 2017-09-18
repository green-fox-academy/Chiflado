# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.


def write_into_a_file():
    file_path = input('Give me the file name: ')
    file_content = input('Give me the word: ')
    file_lines = int(input('How many lines will be in the file? '))
    try:
        my_file = open(file_path, "w")
        for i in range(1, file_lines + 1):
            my_file.write(file_content + " \n")
    except FileNotFoundError: 
        return 0

write_into_a_file()