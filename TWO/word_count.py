#Write a Python program to count the occurrences of each word in a sentence.
def count_word_occurance(sentence):

    words = sentence.split()

    word_count = {}

    for word in words:
        word = word.strip(",.!?").lower()

        if word in word_count:
            word_count[word]+= 1
        else:
            word_count[word]=1
    return word_count
sentence = "hello how are you ,i'm fine how are you fine fine"
print(sentence)
resulte = count_word_occurance(sentence)
print(resulte)            