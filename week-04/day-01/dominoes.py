from domino import Domino
import random

def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 1))
    return dominoes

dominoes = initialize_dominoes()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...

print(dominoes)

def order_to_snake(dominoes):
    snake = []
    snake.append(random.sample(dominoes, 1)[0])
    while len(snake) < len(dominoes):
        for i in dominoes:
            if len(snake) == len(dominoes):
                pass
            elif i.values[0] == snake[len(snake)-1].values[1]:
                snake.append(i)
    return snake


print(order_to_snake(dominoes))