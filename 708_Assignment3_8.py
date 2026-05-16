def permute_of_strings(s, ans=" "):
    if s == "":
        print(ans)
        return
    for i in range(len(s)):
        permute_of_strings(s[:i] + s[i+1:], ans + s[i])

s = input("Enter a string: ")
permute_of_strings(s)