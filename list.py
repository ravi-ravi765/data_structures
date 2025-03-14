# find the largest number in the given list
ls = [1,2,3,4,100]

def find_large_num(x):
	large_value = x[0]
	for i in x:
	    if i > large_value:
	        large_value = i
	return large_value

result = find_large_num(ls)
# print(result)

