import sys as sys
from random import *
from math import sqrt
from numpy import std, mean

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

def modify_current_state(state):
    if (int(state) < 0 or int(state > 8)):
        print("WTF WRONG CURRENT STATE")
        exit(0)
    current_state = state
    #print(current_state + 1)

def add_counter(transition_counter,  state):
    transition_counter[state] += 1
    return transition_counter

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


def estimated_prob(transition_counter, rep_n, steps_m, print_bool):
    if (print_bool == True):
        print("Counters: [1, 2, 3, 4, 5, 6, 7, 8, 9]")
        print(transition_counter)
        print("Estimated probs:")
    index = 1
    array_for_standart_dev = []
    for i in transition_counter:
        if (print_bool == True):
            print("Pi(", end="")
            print(index, end="")
            print(") = ", end="")
            print(i / rep_n)
        array_for_standart_dev.append(i / rep_n)
        index +=1
    if (print_bool == True):
        calc_standart(array_for_standart_dev)
    return array_for_standart_dev

def steady_state_alg(rep_n, steps_m, with_starting_at_0_each_loop, print_bool):
    transition_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    n = 0
    m = 0
    current_state = 0# si la tortue démarre pour tous les 3 steps en 1
    for n in range(rep_n):
        if (with_starting_at_0_each_loop == True):
            current_state = 0
        for m in range(steps_m):
            current_state = tower_sampling(current_state)
        transition_counter = add_counter(transition_counter, current_state)
    esti_prob = estimated_prob(transition_counter, rep_n, steps_m, print_bool)
    return esti_prob

def main():
    nbr_it_algo = 1000
    all_estimated_prob = [[],[],[],[],[],[],[],[],[]]
    for i in range(nbr_it_algo):
        temp = steady_state_alg(10000, 1, False, False) #task 3
        all_estimated_prob[0].append(temp[0])
        all_estimated_prob[1].append(temp[1])
        all_estimated_prob[2].append(temp[2])
        all_estimated_prob[3].append(temp[3])
        all_estimated_prob[4].append(temp[4])
        all_estimated_prob[5].append(temp[5])
        all_estimated_prob[6].append(temp[6])
        all_estimated_prob[7].append(temp[7])
        all_estimated_prob[8].append(temp[8])
        #only for case 1, 3, 9. add the other one to test
    print('Mean Case 1: ', end="")
    print(mean(all_estimated_prob[0]), end="\t Standard dev, 100 algo Case 1: ")
    print(std(all_estimated_prob[0]))

    print('Mean Case 3: ', end="")
    print(mean(all_estimated_prob[2]), end="\t Standard dev, 100 algo Case 3: ")
    print(std(all_estimated_prob[2]))

    print('Mean Case 9: ', end="")
    print(mean(all_estimated_prob[8]), end="\t Standard dev, 100 algo Case 9: ")
    print(std(all_estimated_prob[8]))
    #steady_state_alg(10000, 3, False) #task 4!!
    #steady_state_alg(1, 10000) #task 3    

if __name__ == "__main__":
    main()