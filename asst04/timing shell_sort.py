# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

##INSERTION_SORT
##input: list 
##output: sorted list
##with some help from Tyler's code.  :P

def insertion_sort(l):
    for i in range(len(l)):  #loop through list
        temp = l[i]  #choose ith element
        j = i-1  #choose previous element
        while j>=0 and l[j]>temp:  #as long as previous element is greater than ith element
            l[j+1] = l[j]  #swap "ith" and previous element
            j = j-1  #decrement counter
        l[j+1] = temp  #if loop breaks, put ith element in empty spot
    return l

# <codecell>

##SHELL_SORT, part 1
##sort a list in "shells" of a certain size
##input: positive list, a shell size
##output: list

def simple_shell_sort(l, num):
    for i in range(num):
        l[i:len(l):num] = insertion_sort(l[i:len(l):num])  #loops through sublist, doing insertion sort
    return l

# <codecell>

##SHELL_SORT, part 2
##sort a list based on a list of shells
##input: list to be sorted (all positive), list of shells
##which should be decreasing and have 1 as its last digit
##there is a check to make sure the last number is 1
##for decreasing, you're on your own.  

def shell_sort(l, shells):
    if shells[len(shells)-1] != 1:
        shells.append(1)
    for i in shells:
        l = simple_shell_sort(l,i)
    return l

# <codecell>

##GAP_SORT
##Basically Tyler's code
##input: list to be sorted, list of gap sizes
##output: sorted list

def gap_sort(l,gaps):
    for gap in gaps:
        for i in range(len(l))[gap:]:  #loop through list
            temp = l[i]  #choose ith element
            j = i-gap  #choose previous element
            while j>=0 and l[j]>temp:  #as long as previous element is greater than ith element
                l[j+gap] = l[j]  #swap "ith" and previous element
                j = j-gap  #decrement counter
            l[j+gap] = temp  #if loop breaks, put ith element in empty spot
    return l

gap_sort([234,35,326,7,8,3,47,57,2,745],[4,1])

# <codecell>

##AVERAGE_TIME,
##calculates average time to sort a set of lists based on
##input: set of lists to sort, desired shell-list
##ouput: average time to sort the list

import timeit

def average_time(L, shells):
    time = []
    for l in L:
        start = timeit.default_timer()
        shell_sort(l, shells)   ##can use gap_sort here instead
        end = timeit.default_timer()
        time.append(end-start)
    return sum(time)/len(time)

# <codecell>

##COMPARE_TIMES,
##makes lists of average sorting time for various shell-lists
##input: number of "trials" to average time over, list of shell-lists to compare, upper bound of list length, spacing of list length
##output: list of lengths tried, and times taken

from random import randint
import copy

def compare_times(num, shell_lists, upper_bound, spacing):
    ##create lists for plotting: length_list is x, time_list has a list of y-values for each shell
    length_list = []
    time_list = []
    for k in range(len(shell_lists)):
        time_list.append([])

    ##loop through list lengths
    for i in range(spacing,upper_bound+1,spacing):
        length_list.append(i)
        #make lists of lists to sort
        L = []
        for j in range(num):
            L.append([randint(1,1000) for num in range(i)]) #this needs to be random
        #loop through shells, testing time for each option
        for shell in shell_lists:
            DC = copy.deepcopy(L)
            time_list[shell_lists.index(shell)].append(average_time(DC,shell))
    return (length_list, time_list)
        
#compare_times(2,[[1],[5,2,1]],40)

# <codecell>

##PLOT_COMPARISONS
##plot the differing amounts of time
##input: same variables as compare_times
##output: null, displays line graph

import matplotlib.pyplot as plt
import numpy as np

def plot_comparisons(num, shells, upper, space):
    #run timing function
    values = compare_times(num, shells, upper, space)
    
    #plot points
    for i in range(len(shells)):
        plt.plot(values[0],values[1][i], label=shells[i], linewidth=1)
    #make legend
    plt.legend()
    
    plt.show()

plot_comparisons(3,[[10,5,1],[10,1],[10,7,5,1]], 200, 10)

# <codecell>


# <codecell>

 

# <codecell>


