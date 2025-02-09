#the given list two half equal list divid ,[1,2,3,4,5,6,7,8].

def half_list(list):
    mid = len(list)//2

    first_half=[]
    second_half=[]

    for i in range(mid):

        first_half.append(list[i])
    for j in range(mid,len(list)):
        second_half.append(list[j])

    return first_half,second_half

list = [1,2,3,4,5,6,7,8]        

result = half_list(list)

print(result)
