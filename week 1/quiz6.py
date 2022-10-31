import collections
print("Enter a sentence : .")
sentence = list(map(str, input().split()))
sc = collections.Counter( sentence)
common_word = sc.most_common()[0][0]
max_char = ""
for s in  sentence:
    if len(max_char) < len(s):
        max_char = s
print("\nMost frequent text and the word which has the maximum number of letters.")
print(common_word, max_char)