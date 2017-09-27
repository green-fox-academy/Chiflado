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


summa = Apple()