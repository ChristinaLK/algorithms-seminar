
def compare(upper_row, lower_row):
	'''compares two rows, returning the maximum path to each
	value in the upper row based on the values in the lower row'''
    output = [0]*len(upper_row)
    for i in range(len(upper_row)):
        if upper_row[i] + lower_row[i] > upper_row[i]+lower_row[i+1]:
            output[i] = (upper_row[i]+lower_row[i])
        else:
            output[i] =(upper_row[i]+lower_row[i+1])
    return output

def iter_compare(row_list):
	'''compares a list of "rows", progressing up the list one row at a time'''
    end = len(row_list)
    print end
    output = row_list[-1]
    for i in range(2,end+1):
        output = compare(row_list[-i], output)
    return output

#process input file, place it in variable triangle_list
input_file = open("triangle.txt", "r")
triangle_list = []
for counter,line in enumerate(input_file):
    temp = line.split()
    triangle_list.append([int(x) for x in temp])

#run iter_compare with input list to get answer
print iter_compare(triangle_list)

#triangle = [[1],[4,5],[2,4,7],[1,7,8,2]]
# assert [8, 12] == compare(triangle[1],triangle[2])
# assert [9,12,15] == compare(triangle[2],triangle[3])
#assert [21] == iter_compare(triangle)



