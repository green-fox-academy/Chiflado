# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def replace_character(my_string, x, y):
    if my_string == '':
        return ''
    elif my_string[0] == x:
        return y + replace_character(my_string[1 : ], x, y)
    else: 
        return my_string[0] + replace_character(my_string[1 : ], x, y)


print(replace_character('Somxwhxrx high in thx dxsxrt nxar a curtain of a blux', 'x', 'e'))