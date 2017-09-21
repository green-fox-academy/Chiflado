# Given a string, compute recursively a new string where all the 'x' chars have been removed.

def remove_character(my_string, x):
    if my_string == '':
        return ''
    elif x == my_string[0]:
        return remove_character(my_string[1 : ], x)
    else:
        return my_string[0] + remove_character(my_string[1 : ], x)


print(remove_character('Sxomxetximexxs txruxtxh ixs xstxrangexr thxan ficxtioxn', 'x'))