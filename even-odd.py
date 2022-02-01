my_ints = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_or_odd(my_ints):
    for num in my_ints:
        if ((num % 2) == 1):
            str(num)
            print(f"{num} odd")
        elif ((num % 2) == 0):
            print(f"{num} even")

even_or_odd(my_ints)
