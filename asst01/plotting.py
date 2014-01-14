import numpy as np
import matplotlib.pyplot as plt
import sys

argument = sys.argv[1]

#Fancy things
str_arg = str(argument)
temp = str_arg.split('_')[1]
period = temp.split('.')[0]

def contains_date(myline):
    contains_slash = '/' in myline
    return contains_slash

def question_test(myline):
    is_question = 'Science' in myline
    return not is_question
	
def page_test(myline):
    is_page = 'Page' in myline
    return not is_page
	
	
def get_num_clicks_from_line(myline):
    num_clicks = myline.strip().split(',')[1].replace('"','')
    return int(num_clicks)

num_clicks = []
f = open(argument,'r')
for line in f:
    if contains_date(line) & question_test(line) & page_test(line):
		num_clicks.append(get_num_clicks_from_line(line))
f.close()

#print num_clicks

myarray = np.asarray(num_clicks)
plt.plot(myarray)
plt.xlabel('Days since start of term')
plt.ylabel('Number of clicks')
plt.title('In '+period+', total number of clicks: ' + str(np.sum(myarray)))
plt.show()