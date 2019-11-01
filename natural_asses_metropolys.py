import sys as sys
from random import *
from math import sqrt
from numpy import std

#Pour le 3: 10000, 3 Pour le 4: 1, 10000 

# 1 2 3 4 5 6 7 8 9
square_prob_local =  [1/6, 1/6, 1/6, 1/9, 1/9, 1.9, 1/18, 1/18, 1/18]
#transition prob (in order:) from point 1, 2, 3, 4....

#square_transition_prob = [
#    [1/4, 1/4, 1/2], [1/4, 1/4, 1/4, 1/4], [1/4, 1/4, 1/2], # transition prob line 1 (1, 2 ,3)
#    [1/4, 1/4, 1/2], [1/4, 1/4, 1/4, 1/4], [1/4, 1/4, 1/4, 1/4], #line 2 (4, 5, 6)
#    [1/4, 1/4, 1/2], [1/4, 1/4, 1/4, 1/4], [1/4, 1/4, 1/2] #line 3 (7, 8, 9)
#]

#direction_square_transition_prob = [
#    [4, 2, 1], [1, 2, 3, 5], [2, 6, 3],
#    [1, 4, 5, 7], [2, 4, 6, 8], [3, 5, 6, 9],
#    [4, 8, 7], [5, 7, 8, 9], [6, 8, 9]
#]

square_transition_prob = [
    [1/4, 1/4, 1/2], [1/4, 1/4, 1/4, 1/4], [1/4, 1/4, 1/2], # transition prob line 1 (1, 2 ,3)
    [1/8, 1/4, 1/4, 3/8], [1/8, 1/8, 1/4, 1/4, 1/4], [1/8, 1/4, 1/4, 3/8], #line 2 (4, 5, 6)
    [1/6, 1/4, 7/12], [1/6, 1/4, 1/4, 1/3], [1/6, 1/4, 7/12] #line 3 (7, 8, 9)
]

direction_square_transition_prob = [
    [4, 2, 1], [1, 2, 3, 5], [2, 6, 3],
    [1, 5, 7, 4], [5, 2, 4, 6, 8], [3, 5, 9, 6],
    [4, 8, 7], [5, 7, 9, 8], [6, 8, 9]
]

transition_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def modify_current_state(state):
    if (int(state) < 0 or int(state > 8)):
        print("WTF WRONG CURRENT STATE")
        exit(0)
    current_state = state
    #print(current_state + 1)

def add_counter(state):
    transition_counter[state] += 1

def tower_sampling(current):
    rdm = random()
    index = 0
    transition_sum = 0
    for prob in square_transition_prob[current]:
        old = transition_sum
        transition_sum += prob
        if old < rdm and transition_sum >=  rdm :
            return (direction_square_transition_prob[current][index] - 1)
        index += 1
    return (direction_square_transition_prob[current][index - 1] - 1)

def calc_standart(population):
    size = len(population)
    summ = 0
    for i in population:
        summ += i
    moyenne = summ / size

    sum_diff_minus_moy = 0
    for yes in population:
        diff = yes - moyenne
        carre = diff * diff
        sum_diff_minus_moy += carre
    standat = sqrt(sum_diff_minus_moy)

    print("Size population:")
    print(size)
    print("Summ population:")
    print(summ)
    print("Moyenne:")
    print(moyenne)
    print("Standart deviation:")
    print(std(population))
    print(standat)


def estimated_prob(rep_n, steps_m):
    print("Counters: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
    print(transition_counter)
    print("Estimated probs:")
    index = 1
    array_for_standart_dev = []
    for i in transition_counter:
        print("Pi(", end="")
        print(index, end="")
        print(") = ", end="")
        print(i / rep_n)
        array_for_standart_dev.append(i / rep_n)
        index +=1
    calc_standart(array_for_standart_dev)

def steady_state_alg(rep_n, steps_m, with_starting_at_0_each_loop):
    n = 0
    m = 0
    current_state = 0# si la tortue démarre pour tous les 3 steps en 1
    for n in range(rep_n):
        if (with_starting_at_0_each_loop == True):
            current_state = 0
        for m in range(steps_m):
            current_state = tower_sampling(current_state)
        add_counter(current_state)
    estimated_prob(rep_n, steps_m)

def main():
    #steady_state_alg(10000, 3, True) #task 3
    steady_state_alg(10000, 3, False)
    #steady_state_alg(1, 10000) #task 3    

if __name__ == "__main__":
    main()