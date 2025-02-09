#Write a Python program to find the length of the last word in a sentence.
def len_of_last_word(sentence):

    words = sentence.split()

    if not words:
        return 0
    
    return len(words[-1])

sentence = input("write the sentence:")
print(sentence)

result =len_of_last_word(sentence)
print(result)