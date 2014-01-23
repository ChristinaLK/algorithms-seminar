##merge sort for the command line

import sys

##merge two lists into one
def merge_lists(A, B):
    C = []
    while A or B: #or j < len(B)):
        if not A:
            C.append(B.pop(0))
        elif not B:
            C.append(A.pop(0))
        elif A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
    return C

##loops through a list of lists (L), 
##merging 2 sublists at a time, via merge_lists (above)
##outputs a new list (M) of the just merged sublists
def merge_loop(L):
    M = []
    length = len(L)
    bound = length/2
    for i in range(bound):
        M.append(merge_lists(L[2*i],L[2*i+1]))
    if length%2 == 1:
        M.append(L.pop(length-1))
    del L
    return M
	
##recursive function that runs merge_loop until all sublists are combined	
def merge_recurse(L):
    if len(L) == 1:
        return L
    else:
        M = merge_loop(L)
        return merge_recurse(M)

##makes the nested list I need to start sorting
def list_maker(L):
	K = []
	for i in L:
		K.append([i])
	return K

##tests whether the list is the right kind or not
def list_test(L):
    if type(L[0])== type(list()):
        return True
    else:
        return False

def merge_function(L):
    M = []
    if not list_test(L):
        M = list_maker(L)
    else:
        M = L
    K = merge_recurse(M)
    return K[0]

##list_1 = [3,6,0,12,345,2,56,21,45,7,23,7,124,8,53,546]
##print merge_function(list_1)

##input list
list_to_merge = []

##get values from file
input_file=sys.argv[1]
f = open(input_file,'r')
for line in f:
    list_to_merge.append(int(line))
f.close()

##merge and output to file
output_file = sys.argv[2]
f = open(output_file, 'w')
f.write(str(merge_function(list_to_merge)))
f.close()

##merge and print
#print merge_function(list_to_merge)