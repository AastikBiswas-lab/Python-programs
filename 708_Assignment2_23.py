n = int(input("Enter the number of words: "))
words = []
print("Enter the words:")
for i in range(n):
    word = input()
    words.append(word)
anagram_dict = {}
for word in words:
    key = "".join(sorted(word))
    if key in anagram_dict:
        anagram_dict[key].append(word)
    else:
        anagram_dict[key] = [word]
for group in anagram_dict.values():
    print(group)
    