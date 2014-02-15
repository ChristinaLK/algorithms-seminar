# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

##nodes for use in a linked list
##two attributes: a value and a pointer
##get/set functions for each attribute
##print_method that prints out a node

class node:
    def __init__(self, value, next_node = None):
        self.val = value
        self.ptr = None
        if next_node is not None:
            self.ptr = next_node
            
    def get_val(self):
        return self.val
    def get_ptr(self):
        return self.ptr
    def set_val(self, value):
        self.val = value
    def set_ptr(self, other_node):
        self.ptr = other_node

    def print_method(self):
        print "Node value is: "+str(self.val)
        print "Pointer value is:"+str(self.ptr)

# <codecell>

##linked_list class
##three attributes: head for first node, tail for last node, length counter

class linked_list:
    
    def __init__(self, L):
        self.length = 0
        self.TAIL = node(L.pop())  #create tail, with pointer nowhere
        self.length+=1
        set_node = self.TAIL  #this is the "post" node
        while L:  #range through list
            new_node = node(L.pop(), set_node)  #creating a node with that value
            set_node = new_node  #reset "post" node for next creation
            self.length+=1
        self.HEAD = set_node #final node is head

    def find(self,val):  ##find a value in the list, returns (0) the previous node and (1) the relevant node
        ifexist = False  #tests whether we found something or not
        prev_node = self.HEAD
        test_node = self.HEAD
        for i in range(self.length): #loops through list length
            if test_node.get_val() == val:  #if we find something, break
                ifexist = True
                break
            else:  #otherwise, move the node to be tested forward one
                prev_node = test_node
                test_node = test_node.get_ptr()
        if ifexist:
            return prev_node, test_node
        else:
            print "Value not found"
            return ifexist, test_node
    
    def insert(self, loc_val, insert_val): ##inserts the second argument after the first argument
        insert_after = self.find(loc_val)[1]  #gives the node with the value (via find)
        if self.find(loc_val)[0]:  #if non-empty carry on
            new_node = node(insert_val, insert_after.get_ptr()) #create new node, leading to prev node's old link
            insert_after.set_ptr(new_node) #set previous node to new node
            self.length +=1  #increment counter
            if insert_after == self.TAIL:  #if this was added at the end, reset the tail
                self.TAIL = new_node
            
    def remove(self,val): ##removes a value
        to_remove = self.find(val)[1] 
        prev = self.find(val)[0]
        if prev: #if we found the value
            if to_remove == self.HEAD:  #if head node
                self.HEAD = to_remove.get_ptr() #reset head to next node
                self.length-=1 #decrement counter
            elif to_remove == self.TAIL: #if tail node
                prev.set_ptr(None) #change previous pointer to none
                self.TAIL = prev #reset tail to previous
                self.length-=1 #decrement counter
            else: #any other case
                prev.set_ptr(to_remove.get_ptr()) #set prev. pointer to removed nodes pointer
                self.length-=1 #decrement counter

    def print_list(self):
        print_node = self.HEAD
        while True:
            print print_node.get_val()
            if print_node.get_ptr() == None:
                break
            else:
                print_node = print_node.get_ptr()

# <codecell>


# <codecell>


