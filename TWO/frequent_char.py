#to remove all leading and trailing whitespaces from a 
# Write a Python program to find the most frequent character in a string.
from collections import Counter
def freq_char(string):

    string = "".join(string.split())

    frequency = Counter(string)

    most_freq = frequency.most_common(1)[0]

    return most_freq[0],most_freq[1]

string = "hello ,how are youe."
result = freq_char(string)
print(result)