# math 
# find the factorial

def find_factorial(n):
    result = 1
    for i in range(1,n+1):
        if n == 0:
            print("0 factorial is 1")
        else:
            result *= i
    return result

# find the number of digits prsent in the given n

# let's break it step by step
# step 1 : check if the digit present in the n
# step 2 : remove the last element num in the n
# step 3 : take new variable to store the count, for each removal count increment by 1
# step 4 : reperat the steps still n becomes 0

def count_digit(n):
    count = 0

    while n > 0:
        n = n//10
        count += 1
    
    return count

# find the trailing zeros given a n factorial "n!"
def trailing_zeros(n):
    result = 0
    powerof = 5

    while (n >= powerof):
        result += (n//powerof)
        powerof *= 5
    return result

def main():
    n = 0
    res = find_factorial(n)
    res1 = count_digit(12345)
    res2 = trailing_zeros(10)
    print(res)
    print(res1)
    print(res2)



if __name__ == "__main__": # if you want you run your program in script mode then you can use this condition
    main()



