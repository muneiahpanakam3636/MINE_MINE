#Write a Python program to check if a string contains only unique characters.

def string_unique_characters(string):

    return len(string)== len(set(string))# convert to set format,set automatically remove duplicates,and compare length


string = input("enter the string:")
print(string)

if string_unique_characters(string):
    print("string has unique characters")
else:
    print("hasn't unique characters")    