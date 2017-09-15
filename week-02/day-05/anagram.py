first_string = input('Your first word: ')
sorted_first = sorted(first_string)
second_string = input('Aaaaand your second word: ')
sorted_second = sorted(second_string)

def anagram_finder(sorted_first, sorted_second):
    if sorted_first == sorted_second:
        return 'There are anagrams!'
    else:
        return 'There aren\'t anagrams!'

print(anagram_finder(sorted_first, sorted_second))