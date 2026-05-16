def count(s, ch):
    if s == " ":
        return 0
    if s[0] == ch:
        return 1 + count(s[1:], ch)
    return count(s[1:], ch)

s = input("Enter string: ")
ch = input("Enter character: ")
print("Count:", count(s, ch))