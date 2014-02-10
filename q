[1mdiff --git a/asst04/random work.ipynb b/asst04/random work.ipynb[m
[1mindex a6b1542..c8e7329 100644[m
[1m--- a/asst04/random work.ipynb[m	
[1m+++ b/asst04/random work.ipynb[m	
[36m@@ -250,6 +250,43 @@[m
      "language": "python",[m
      "metadata": {},[m
      "outputs": [][m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "cell_type": "code",[m
[32m+[m[32m     "collapsed": false,[m
[32m+[m[32m     "input": [[m
[32m+[m[32m      "def selection_sort(l):\n",[m
[32m+[m[32m      "    for i in range(len(l)):\n",[m
[32m+[m[32m      "        temp = l[i]\n",[m
[32m+[m[32m      "        j = i-1\n",[m
[32m+[m[32m      "        while j>=0 and l[j]>temp:\n",[m
[32m+[m[32m      "            l[j+1] = l[j]\n",[m
[32m+[m[32m      "            j = j-1\n",[m
[32m+[m[32m      "        l[j+1] = temp\n",[m
[32m+[m[32m      "    return l\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "selection_sort([23,345,543,1235,45,23,5445,3,6,6,3,7])"[m
[32m+[m[32m     ],[m
[32m+[m[32m     "language": "python",[m
[32m+[m[32m     "metadata": {},[m
[32m+[m[32m     "outputs": [[m
[32m+[m[32m      {[m
[32m+[m[32m       "output_type": "pyout",[m
[32m+[m[32m       "prompt_number": 3,[m
[32m+[m[32m       "text": [[m
[32m+[m[32m        "[3, 3, 6, 6, 7, 23, 23, 45, 345, 543, 1235, 5445]"[m
[32m+[m[32m       ][m
[32m+[m[32m      }[m
[32m+[m[32m     ],[m
[32m+[m[32m     "prompt_number": 3[m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "cell_type": "code",[m
[32m+[m[32m     "collapsed": false,[m
[32m+[m[32m     "input": [],[m
[32m+[m[32m     "language": "python",[m
[32m+[m[32m     "metadata": {},[m
[32m+[m[32m     "outputs": [][m
     }[m
    ],[m
    "metadata": {}[m
[1mdiff --git a/asst04/shell sort.ipynb b/asst04/shell sort.ipynb[m
[1mindex de99006..daf506e 100644[m
[1m--- a/asst04/shell sort.ipynb[m	
[1m+++ b/asst04/shell sort.ipynb[m	
[36m@@ -14,17 +14,17 @@[m
       "##INSERTION_SORT\n",[m
       "##input: list \n",[m
       "##output: sorted list\n",[m
[32m+[m[32m      "##with some help from Tyler's code.  :P\n",[m
       "\n",[m
       "def insertion_sort(l):\n",[m
[31m-      "    new_list = [l[0]]  #list to \"insert\" into\n",[m
[31m-      "    for i in l[1:len(l)]:  #loop through elements of original list\n",[m
[31m-      "        for j in range(0, len(new_list)):  #run through all spaces in list so far\n",[m
[31m-      "            if i <= new_list[j]:      # once you find a place where the next number is bigger\n",[m
[31m-      "                new_list.insert(j,i)  #insert your current value + break\n",[m
[31m-      "                break\n",[m
[31m-      "            elif j==(len(new_list)-1):\n",[m
[31m-      "                new_list.append(i)\n",[m
[31m-      "    return new_list\n",[m
[32m+[m[32m      "    for i in range(len(l)):  #loop through list\n",[m
[32m+[m[32m      "        temp = l[i]  #choose ith element\n",[m
[32m+[m[32m      "        j = i-1  #choose previous element\n",[m
[32m+[m[32m      "        while j>=0 and l[j]>temp:  #as long as previous element is greater than ith element\n",[m
[32m+[m[32m      "            l[j+1] = l[j]  #swap \"ith\" and previous element\n",[m
[32m+[m[32m      "            j = j-1  #decrement counter\n",[m
[32m+[m[32m      "        l[j+1] = temp  #if loop breaks, put ith element in empty spot\n",[m
[32m+[m[32m      "    return l\n",[m
       "\n",[m
       "##SHELL_SORT, part 1\n",[m
       "##sort a list in \"shells\" of a certain size\n",[m
[36m@@ -68,7 +68,7 @@[m
        ][m
       }[m
      ],[m
[31m-     "prompt_number": 2[m
[32m+[m[32m     "prompt_number": 1[m
     },[m
     {[m
      "cell_type": "code",[m
[36m@@ -139,7 +139,7 @@[m
        ][m
       }[m
      ],[m
[31m-     "prompt_number": 35[m
[32m+[m[32m     "prompt_number": 2[m
     },[m
     {[m
      "cell_type": "code",[m
[1mdiff --git a/asst04/timing shell_sort.ipynb b/asst04/timing shell_sort.ipynb[m
[1mindex 4591d3e..66e2380 100644[m
[1m--- a/asst04/timing shell_sort.ipynb[m	
[1m+++ b/asst04/timing shell_sort.ipynb[m	
[36m@@ -14,18 +14,17 @@[m
       "##INSERTION_SORT\n",[m
       "##input: list \n",[m
       "##output: sorted list\n",[m
[32m+[m[32m      "##with some help from Tyler's code.  :P\n",[m
       "\n",[m
       "def insertion_sort(l):\n",[m
[31m-      "    for i in range(0,len(l)): #loop \"n\" times through list\n",[m
[31m-      "        temp = l.pop(i) #pop ith element\n",[m
[31m-      "        for j in range(i+1):   #compare with up to previous k elements\n",[m
[31m-      "            if j == i:  #if we're at the end of k elements (biggest number so far), insert in kth position\n",[m
[31m-      "                l.insert(j,temp)\n",[m
[31m-      "                break\n",[m
[31m-      "            elif temp<=l[j]:  #otherwise (normal statement), insert in order\n",[m
[31m-      "                l.insert(j,temp)\n",[m
[31m-      "                break \n",[m
[31m-      "    return l\n"[m
[32m+[m[32m      "    for i in range(len(l)):  #loop through list\n",[m
[32m+[m[32m      "        temp = l[i]  #choose ith element\n",[m
[32m+[m[32m      "        j = i-1  #choose previous element\n",[m
[32m+[m[32m      "        while j>=0 and l[j]>temp:  #as long as previous element is greater than ith element\n",[m
[32m+[m[32m      "            l[j+1] = l[j]  #swap \"ith\" and previous element\n",[m
[32m+[m[32m      "            j = j-1  #decrement counter\n",[m
[32m+[m[32m      "        l[j+1] = temp  #if loop breaks, put ith element in empty spot\n",[m
[32m+[m[32m      "    return l"[m
      ],[m
      "language": "python",[m
      "metadata": {},[m
[36m@@ -39,10 +38,10 @@[m
       "##SHELL_SORT, part 1\n",[m
       "##sort a list in \"shells\" of a certain size\n",[m
       "##input: positive list, a shell size\n",[m
[31m-      "##output: list, with sublists of index equiv mod(num) sorted in ascending order\n",[m
[32m+[m[32m      "##output: list\n",[m
       "\n",[m
       "def simple_shell_sort(l, num):\n",[m
[31m-      "    for i in range(num):  #shell \"size\" (multiples of num)\n",[m
[32m+[m[32m      "    for i in range(num):\n",[m
       "        l[i:len(l):num] = insertion_sort(l[i:len(l):num])  #loops through sublist, doing insertion sort\n",[m
       "    return l"[m
      ],[m
[36m@@ -57,12 +56,14 @@[m
      "input": [[m
       "##SHELL_SORT, part 2\n",[m
       "##sort a list based on a list of shells\n",[m
[31m-      "##input: list to be sorted, list of shells\n",[m
[31m-      "##output: sorted list\n",[m
[32m+[m[32m      "##input: list to be sorted (all positive), list of shells\n",[m
[32m+[m[32m      "##which should be decreasing and have 1 as its last digit\n",[m
[32m+[m[32m      "##there is a check to make sure the last number is 1\n",[m
[32m+[m[32m      "##for decreasing, you're on your own.  \n",[m
       "\n",[m
       "def shell_sort(l, shells):\n",[m
[31m-      "    #if shells[len(shells)-1] != 1:\n",[m
[31m-      "    #    shells.append(1)\n",[m
[32m+[m[32m      "    if shells[len(shells)-1] != 1:\n",[m
[32m+[m[32m      "        shells.append(1)\n",[m
       "    for i in shells:\n",[m
       "        l = simple_shell_sort(l,i)\n",[m
       "    return l"[m
[36m@@ -76,6 +77,41 @@[m
      "cell_type": "code",[m
      "collapsed": false,[m
      "input": [[m
[32m+[m[32m      "##GAP_SORT\n",[m
[32m+[m[32m      "##Basically Tyler's code\n",[m
[32m+[m[32m      "##input: list to be sorted, list of gap sizes\n",[m
[32m+[m[32m      "##output: sorted list\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "def gap_sort(l,gaps):\n",[m
[32m+[m[32m      "    for gap in gaps:\n",[m
[32m+[m[32m      "        for i in range(len(l))[gap:]:  #loop through list\n",[m
[32m+[m[32m      "            temp = l[i]  #choose ith element\n",[m
[32m+[m[32m      "            j = i-gap  #choose previous element\n",[m
[32m+[m[32m      "            while j>=0 and l[j]>temp:  #as long as previous element is greater than ith element\n",[m
[32m+[m[32m      "                l[j+gap] = l[j]  #swap \"ith\" and previous element\n",[m
[32m+[m[32m      "                j = j-gap  #decrement counter\n",[m
[32m+[m[32m      "            l[j+gap] = temp  #if loop breaks, put ith element in empty spot\n",[m
[32m+[m[32m      "    return l\n",[m
[32m+[m[32m      "\n",[m
[32m+[m[32m      "gap_sort([234,35,326,7,8,3,47,57,2,745],[4,1])"[m
[32m+[m[32m     ],[m
[32m+[m[32m     "language": "python",[m
[32m+[m[32m     "metadata": {},[m
[32m+[m[32m     "outputs": [[m
[32m+[m[32m      {[m
[32m+[m[32m       "output_type": "pyout",[m
[32m+[m[32m       "prompt_number": 10,[m
[32m+[m[32m       "text": [[m
[32m+[m[32m        "[2, 3, 7, 8, 35, 47, 57, 234, 326, 745]"[m
[32m+[m[32m       ][m
[32m+[m[32m      }[m
[32m+[m[32m     ],[m
[32m+[m[32m     "prompt_number": 10[m
[32m+[m[32m    },[m
[32m+[m[32m    {[m
[32m+[m[32m     "cell_type": "code",[m
[32m+[m[32m     "collapsed": false,[m
[32m+[m[32m     "input": [[m
       "##AVERAGE_TIME,\n",[m
       "##calculates average time to sort a set of lists based on\n",[m
       "##input: set of lists to sort, desired shell-list\n",[m
[36m@@ -87,7 +123,7 @@[m
       "    time = []\n",[m
       "    for l in L:\n",[m
       "        start = timeit.default_timer()\n",[m
[31m-      "        shell_sort(l, shells)\n",[m
[32m+[m[32m      "        shell_sort(l, shells)   ##can use gap_sort here instead\n",[m
       "        end = timeit.default_timer()\n",[m
       "        time.append(end-start)\n",[m
       "    return sum(time)/len(time)"[m
[36m@@ -95,7 +131,7 @@[m
      "language": "python",[m
      "metadata": {},[m
      "outputs": [],[m
[31m-     "prompt_number": 5[m
[32m+[m[32m     "prompt_number": 39[m
     },[m
     {[m
      "cell_type": "code",[m
[36m@@ -103,12 +139,13 @@[m
      "input": [[m
       "##COMPARE_TIMES,\n",[m
       "##makes lists of average sorting time for various shell-lists\n",[m
[31m-      "##input: number of \"trials\" to average time over, list of shell-lists to compare, upper bound of list length\n",[m
[32m+[m[32m      "##input: number of \"trials\" to average time over, list of shell-lists to compare, upper bound of list length, spacing of list length\n",[m
       "##output: list of lengths tried, and times taken\n",[m
       "\n",[m
       "from random import randint\n",[m
[32m+[m[32m      "import copy\n",[m
       "\n",[m
[31m-      "def compare_times(num, shell_lists, upper_bound):\n",[m
[32m+[m[32m      "def compare_times(num, shell_lists, upper_bound, spacing):\n",[m
       "    ##create lists for plotting: length_list is x, time_list has a list of y-values for each shell\n",[m
       "    length_list = []\n",[m
       "    time_list = []\n",[m
[36m@@ -116,7 +153,7 @@[m
       "        time_list.append([])\n",[m
       "\n",[m
       "    ##loop through list lengths\n",[m
[31m-      "    for i in range(10,upper_bound+1,10):\n",[m
[32m+[m[32m      "    for i in range(spacing,upper_bound+1,spacing):\n",[m
       "        length_list.append(i)\n",[m
       "        #make lists of lists to sort\n",[m
       "        L = []\n",[m
[36m@@ -124,16 +161,16 @@[m
       "            L.append([randint(1,1000) for num in range(i)]) #this needs to be random\n",[m
       "        #loop through shells, testing time for each option\n",[m
       "        for shell in shell_lists:\n",[m
[31m-      "            time_list[shell_lists.index(shell)].append(average_time(L,shell))\n",[m
[31m-      "    \n",[m
[32m+[m[32m      "            DC = copy.deepcopy(L)\n",[m
[32m+[m[32m      "            time_list[shell_lists.index(shell)].append(average_time(DC,shell))\n",[m
       "    return (length_list, time_list)\n",[m
       "        \n",[m
[31m-      "#compare_times(2,[[5,2,1],[1]],50)\n"[m
[32m+[m[32m      "#compare_times(2,[[1],[5,2,1]],40)\n"[m
      ],[m
      "language": "python",[m
      "metadata": {},[m
      "outputs": [],[m
[31m-     "prompt_number": 6[m
[32m+[m[32m     "prompt_number": 40[m
     },[m
     {[m
      "cell_type": "code",[m
[36m@@ -147,9 +184,9 @@[m
       "import matplotlib.pyplot as plt\n",[m
       "import numpy as np\n",[m
       "\n",[m
[31m-      "def plot_comparisons(num, shells, u):\n",[m
[32m+[m[32m      "def plot_comparisons(num, shells, upper, space):\n",[m
       "    #run timing function\n",[m
[31m-      "    values = compare_times(num, shells, u)\n",[m
[32m+[m[32m      "    values = compare_times(num, shells, upper, space)\n",[m
       "    \n",[m
       "    #plot points\n",[m
       "    for i in range(len(shells)):\n",[m
[36m@@ -159,23 +196,17 @@[m
       "    \n",[m
       "    plt.show()\n",[m
       "\n",[m
[31m-      "plot_comparisons(3,[[200,100,1],[1]], 300)"[m
[32m+[m[32m      "plot_comparisons(3,[[10,5,1],[10,1],[10,7,5,1]], 200, 10)"[m
      ],[m
      "language": "python",[m
      "metadata": {},[m
      "outputs": [],[m
[31m-     "prompt_number": 7[m
[32m+[m[32m     "prompt_number": 43[m
     },[m
     {[m
      "cell_type": "code",[m
      "collapsed": false,[m
[31m-     "input": [[m
[31m-      "s = [9,8,7,6,5,4,3,2,1]\n",[m
[31m-      "sample = [6,2,4,7,8,2,3,6,7,3,4,9]\n",[m
[31m-      "\n",[m
[31m-      "print shell_sort(s,[3,1])\n",[m
[31m-      "print shell_sort(sample,[5,3,1])"[m
[31m-     ],[m
[32m+[m[32m     "input": [],[m
      "language": "python",[m
      "metadata": {},[m
      "outputs": [[m
