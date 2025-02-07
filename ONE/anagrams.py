#Write a Python program to check if two strings are anagrams.

def anagrams(str1,str2):
    return sorted(str1)==sorted(str2)

str1 = input("enter the string:")
str2 = input("enter the string:")

if anagrams(str1,str2):
    print("these sre anagrams")
else:
    print("not anagrams")    