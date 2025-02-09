#the given list as 5 divisible number as "a",then 
# 2 divisible by number as "b to print range 20 elements

def find_numbers(a,b):

 

 numbers = []
 for i in range(1,20):
        if i%a ==0:
            numbers.append(f'{i} divisible by {a}')
        elif i%b == 0:
            numbers.append(f'{i} divisible by {b}')

    
 for num in numbers:
        print(num)
a = 5
b = 2    
find_numbers(a,b)
 