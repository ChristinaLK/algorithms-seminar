#Combining plotting.py + top_questions.py

import numpy as np
import matplotlib.pyplot as plt
import sys

##functions
#tests whether a line contains slashes (is a date or url)
def contains_date(myline):
    contains_slash = '/' in myline
    return contains_slash

#tests whether a line has the word "page" to get rid of the one annoying line exception w/ a slash
def page_test(myline):
    is_page = 'Page' in myline
    return not is_page

#takes a line, evaluates whether it is a question url
def question_test(myline):
    is_question = 'Question' in myline
    return not is_question
	
#removes number of clicks from a click-line
def get_num_clicks_from_line(myline):
    num_clicks = myline.strip().split(',')[1].replace('"','')
    return int(num_clicks)
	
#extracts the average time from a line and turns it into an integer.
def get_time(myline):
    time = myline.split(',')[4].replace(':','')
    return int(time)

#extracts the question title from a line and strips the preamble
def get_question(myline):
    question = myline.split(',')[0].replace('/Science:Math_Exam_Resources/Courses/','')
    return question

##program
#get stuff from command line
file_name=sys.argv[1]

#fancy things - take off the season/year of the file name and use it in the plot later
str_arg = str(file_name)
temp = str_arg.split('_')[1]
period = temp.split('.')[0]

#create empty dictionary
average_time = {}

#open appropriate file and extract questions + times into dictionary
f = open(file_name,'r')
for line in f:
    if not question_test(line):
        average_time[get_time(line)] = get_question(line)
f.close()

#sort greatest to least and print first 10 things
for key_val in sorted(average_time, reverse=True)[0:10]:
    time_print = str(key_val)
    print average_time[key_val] + '   ' + time_print[0]+':'+time_print[1:3]
	
#create empty list
num_clicks = []

#extract number of clicks into list
f = open(file_name,'r')
for line in f:
    if contains_date(line) & question_test(line) & page_test(line):
		num_clicks.append(get_num_clicks_from_line(line))
f.close()

#plot list
myarray = np.asarray(num_clicks)
plt.plot(myarray)
plt.xlabel('Days since start of term')
plt.ylabel('Number of clicks')
plt.title('In '+period+', total number of clicks: ' + str(np.sum(myarray)))
plt.show()