import collections


# Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The
# first one is the word which occurs most frequently in the text. The second one is the word which has the maximum
# number of letters. 

def sentenceCount(sentence: str) -> None:
    sentence = list(map(str, sentence.split()))
    sc = collections.Counter(sentence)
    common_word = sc.most_common()[0][0]
    max_char = ""
    for s in sentence:
        if len(max_char) < len(s):
            max_char = s
    print("\nMost frequent word and the word which has the maximum number of characters.")
    print(common_word, max_char)


sentence: str = input("Enter a sentence : ")
print("Enter a sentence : ."+sentence)

sentenceCount(sentence)
