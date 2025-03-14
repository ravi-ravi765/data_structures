# find the largest number in the given list
ls = [1,2,3,4,100]

def find_large_num(x):
    large_num = x[0]
    for i in x:
        if i > large_num:
            large_num = i
    return large_num
	

result = find_large_num(ls)
# print(result)

