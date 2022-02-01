for num in range(3, 101):
    for x in range(2, num):
        if (num % x) == 0:
            break
    else:
        print(num)        
