is_it_palindrome = 'dog goat dad duck doodle never'

def check_palindrome(is_it_palindrome):
    for i in range(len(is_it_palindrome) / 2):
        if is_it_palindrome[i] != is_it_palindrome[-1 * (i + 1)]:
            return False
    return True

check_palindrome(is_it_palindrome)