import sys

##INSERTION_SORT
##input: list (all positive integers, due to annoying hack)
##output: sorted list

def insertion_sort(l):
    new_list = [0]  #list to "insert" into
    for i in l:  #loop through elements of original list
        if i > new_list[len(new_list)-1]:  #if object is larger than end of list, append
            new_list.append(i)
        else:                               #else, must insert elsewhere in the list
            for j in range(0, len(new_list)):  #run through all spaces in list so far
                if i <= new_list[j]:      # once you find a place where the next number is bigger
                    new_list.insert(j,i)  #insert your current value + break
                    break
    return new_list[1:len(new_list)]

##SHELL_SORT, part 1
##sort a list in "shells" of a certain size
##input: positive list, a shell size
##output: list

def simple_shell_sort(l, num):
    for i in range(num):
        l[i:len(l):num] = insertion_sort(l[i:len(l):num])  #loops through sublist, doing insertion sort
    return l

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
	
input_list = list(sys.argv[1])
shell_list = list(sys.argv[2])

shell_sort(input_list, shell_list)