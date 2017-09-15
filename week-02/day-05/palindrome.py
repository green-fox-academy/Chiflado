want_to_be_a_palindrome = input('What want you make to a palindrome? ')

def palindrome_maker(want_to_be_a_palindrome):
    want_to_be_a_palindrome += want_to_be_a_palindrome[::-1]
    return want_to_be_a_palindrome

print(palindrome_maker(want_to_be_a_palindrome))