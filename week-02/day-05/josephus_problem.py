how_many_people_in_circle = int(input('How manyi people are in the circle? '))

def josephus(how_many_people_in_circle):
        which_neighbour_has_to_die = 2
        r = 0
        for i in range(1, how_many_people_in_circle + 1):
            r = (r + which_neighbour_has_to_die) % i
        r = r + 1
        return 'The number of winnig seat is: %d' %r
 
print(josephus(how_many_people_in_circle))