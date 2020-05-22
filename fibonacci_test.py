def fibonacci(first, last):     # Function to calculate fibonacci sequence
    list = []
    n1, n2 = 0, 1
    count = 0
    if first < last:
        while count < last:
            list.append(n1) #keep to most-up-to-date-terms
            nth = n1 + n2   #upodate math
            n1 = n2         #update
            n2 = nth
            count += 1      #iterate
    return list[first: last]


print(fibonacci(2, 9))      # this will print out 2nd to 8th terms of fibonnaci sequence, in this case is 1,2,3,5,8,13,21 whereas 1st to 10th terms is 1,1,2,3,5,8,13,21,34,55
