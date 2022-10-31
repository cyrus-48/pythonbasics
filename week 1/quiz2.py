string_words = input("Enter string  :")

word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]
print(word_freq)
print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))
