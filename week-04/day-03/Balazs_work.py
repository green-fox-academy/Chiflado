class Apple(object):

    def get_apple(self):
        return 'apple'

    def get_sum(self, my_list):
        return sum(my_list)

    def get_anagram(self, string1, string2):
        self.sorted_first = sorted(string1)
        self.sorted_second = sorted(string2)
        if self.sorted_first == self.sorted_second:
            return True
        else:
            return False

    def letter_counter(self, my_string):
        my_dictionary = {}
        for letter in my_string:
            if letter in my_dictionary:
                my_dictionary[letter] += 1
            else:
                my_dictionary[letter] = 1
        return my_dictionary

summa = Apple()