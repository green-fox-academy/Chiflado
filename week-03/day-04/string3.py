# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def separate_characters(my_string):
    if my_string == '':
        return ''
    elif len(my_string) == 1:
        return my_string[0]
    else:
        temp = my_string[0] + '*'
        return temp + separate_characters(my_string[1 : ])


print(separate_characters('valami baromsag'))