import sys

#takes a line, evaluates whether it is a question, returns boolean
def question_test(myline):
    is_question = 'Question' in myline
    return is_question

#extracts the average time from a line and turns it into an integer.
def get_time(myline):
    time = myline.split(',')[4].replace(':','')
    return int(time)

#extracts the question title from a line and strips the preamble
def get_question(myline):
    question = myline.split(',')[0].replace('/Science:Math_Exam_Resources/Courses/','')
    return question

#get stuff from command line
file_name=sys.argv[1]
	
#create empty dictionary
average_time = dict()

#open appropriate file and extract questions + times into dictionary
f = open(file_name,'r')
for line in f:
    if question_test(line):
        average_time[get_time(line)] = get_question(line)
f.close()

#sort greatest to least and print first n things
for key_val in sorted(average_time, reverse=True)[0:10]:
    time_print = str(key_val)
    print average_time[key_val] + '   ' + time_print[0]+':'+time_print[1:3]