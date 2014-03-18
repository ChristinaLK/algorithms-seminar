def compare(upper_row, lower_row):
    output = [0]*len(upper_row)
    for i in range(len(upper_row)):
        if upper_row[i] + lower_row[i] > upper_row[i]+lower_row[i+1]:
            output[i] = (upper_row[i]+lower_row[i])
        else:
            output[i] =(upper_row[i]+lower_row[i+1])
    return output
	