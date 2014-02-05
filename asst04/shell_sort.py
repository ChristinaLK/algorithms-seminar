##INSERTION_SORT
##input: list 
##output: sorted list

def insertion_sort(l):
    for i in range(0,len(l)): #loop "n" times through list
        temp = l.pop(i) #pop ith element
        for j in range(i+1):   #compare with up to previous k elements
            if j == i:  #if we're at the end of k elements (biggest number so far), insert in kth position
                l.insert(j,temp)
                break
            elif temp<=l[j]:  #otherwise (normal statement), insert in order
                l.insert(j,temp)
                break 
    return l

##SHELL_SORT, part 1
##sort a list in "shells" of a certain size
##input: positive list, a shell size
##output: list, with sublists of index equiv mod(num) sorted in ascending order

def simple_shell_sort(l, num):
    for i in range(num):  #shell "size" (multiples of num)
        l[i:len(l):num] = insertion_sort(l[i:len(l):num])  #loops through sublist, doing insertion sort
    return l
	
##SHELL_SORT, part 2
##sort a list based on a list of shells
##input: list to be sorted, list of shells
##output: sorted list

def shell_sort(l, shells):
    #if shells[len(shells)-1] != 1:
    #    shells.append(1)
    for i in shells:
        l = simple_shell_sort(l,i)
    return l

##AVERAGE_TIME,
##calculates average time to sort a set of lists based on
##input: set of lists to sort, desired shell-list
##ouput: average time to sort the list

import timeit

def average_time(L, shells):
    time = []
    for l in L:
        start = timeit.default_timer()
        shell_sort(l, shells)
        end = timeit.default_timer()
        time.append(end-start)
    return sum(time)/len(time)

##COMPARE_TIMES,
##makes lists of average sorting time for various shell-lists
##input: number of "trials" to average time over, list of shell-lists to compare, upper bound of list length
##output: list of lengths tried, and times taken

from random import randint

def compare_times(num, shell_lists, upper_bound):
    ##create lists for plotting: length_list is x, time_list has a list of y-values for each shell
    length_list = []
    time_list = []
    for k in range(len(shell_lists)):
        time_list.append([])

    ##loop through list lengths
    for i in range(10,upper_bound+1,10):
        length_list.append(i)
        #make lists of lists to sort
        L = []
        for j in range(num):
            L.append([randint(1,1000) for num in range(i)]) #this needs to be random
        #loop through shells, testing time for each option
        for shell in shell_lists:
            time_list[shell_lists.index(shell)].append(average_time(L,shell))
    
    return (length_list, time_list)

##PLOT_COMPARISONS
##plot the differing amounts of time
##input: same variables as compare_times
##output: null, displays line graph

import matplotlib.pyplot as plt
import numpy as np

def plot_comparisons(num, shells, u):
    #run timing function
    values = compare_times(num, shells, u)
    
    #plot points
    for i in range(len(shells)):
        plt.plot(values[0],values[1][i], label=shells[i], linewidth=1)
    #make legend
    plt.legend()
    
    plt.show()