#To given list [1,2,3,4,5,6,7,8,9] as the elements pair sum is equal to the target number is 9

arr = [1,2,3,4,5,6,7,8,9]

target= 9

pairs = []

for i in range(len(arr)):
    for j in range(i+1,len(arr)):

        if arr[i]+arr[j] == target:
            pairs.append((arr[i],arr[j]))

print(pairs)            