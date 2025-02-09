#the given list as even number as "a",then odd number as "b to print range 20 elements

numbers = list(range(1,21))

even_numbers = []
odd_numbers = []

for i in numbers:
    if i%2 ==0:
        print("a")
    else:
        print("b")    