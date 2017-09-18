# Create a function that takes 3 parameters: a path, a word and a number,
# than it should write to a file.
# The path parameter should be a string, that describes the location of the file.
# The word parameter should be a string, that will be written to the file as lines
# The number paramter should describe how many lines the file should have.
# So if the word is "apple" and the number is 5, than it should write 5 lines
# to the file and each line should be "apple"
# The function should not raise any error if it could not write the file.


def write_lines():
    file_path = open('my-file.txt', 'w')
    file_content = input('What will be in the file? ')
    file_lines = int(input('How many lines will be in the file? '))
    try:
        f = open (file_path, "w")
        for line in range(file_lines):
            f.write(file_content)
    except:
        pass


write_lines()