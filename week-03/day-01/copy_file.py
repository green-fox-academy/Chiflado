# Write a function that copies a file to an other
# It should take the filenames as parameters
# It should return a boolean that shows if the copy was successful


def copy_a_file():
    first_file = open('my-file.txt', 'r')
    file_content = first_file.read()
    second_file = open('copy-of-my-file.txt', 'w+')
    second_file.write(file_content)
    copied_content = second_file.read()
    first_file.close()
    second_file.close()        
    if file_content == copied_content:
        return True

copy_a_file()