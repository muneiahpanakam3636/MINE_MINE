#the given list as take user index number that will taken
#Rotate x=[1,2,3,4,5,6,7,8], element=4,output:[4,5,6,7,8,1,2,3]


def rotate_elements(x,index):
    return x[index:]+ x[:index]

x = [1,2,3,4,5,6,7,8]
index = 3
print(x)
print(index)

result = rotate_elements(x,index)
print(result)