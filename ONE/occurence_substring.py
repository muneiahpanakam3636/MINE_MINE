#Write a Python program to count the number of occurrences of a specific substring in a string.

def occurences_of_substring(string,substring):

    return string.count(substring)

string = input("hello how are you??, hello im fine.")
substring =input("hello")

occurences = occurences_of_substring(string,substring)
print("the substring occurnces:",occurences)