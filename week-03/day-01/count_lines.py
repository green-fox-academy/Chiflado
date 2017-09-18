# Write a function that takes a filename as string,
# then returns the number of lines the file contains.
# It should return zero if it can't open the file, and
# should not raise any error.

def line_counter():
    user_file = input('In which file want you count the lines? ')
    try:    
        with open(user_file) as myfile:
            count = sum(1 for line in myfile)
            print(str(count) + ' line(s) is/are in the file')
    except Exception:
        return 0

line_counter()