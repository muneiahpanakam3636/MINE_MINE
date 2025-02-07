#Adding Two List Elements Together

def add_lists(list1,list2):


    if len(list1)==len(list2):
        result = [list1[i]+list2[i] for i in range(len(list2))]
    else:
        "lists must have same length"     

    return result
list1 = [12,24,52,36,5]
list2 =[5,52,63,25,32]
result = add_lists(list1,list2)

print("Result:",result)
