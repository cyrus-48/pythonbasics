#Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies. 
def wordsCount(words: str) -> None:
    word_list = words.split()
    word_freq = [word_list.count(n) for n in word_list]
    print(word_freq)
    print("String:\n {} \n".format(words))
    print("List:\n {} \n".format(str(word_list)))
    print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))


words: str = input("Enter string  :")
wordsCount(words)
