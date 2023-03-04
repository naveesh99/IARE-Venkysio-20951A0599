def reverse_word(word):
    if len(word) == 0 or len(word) == 1:
        return word
    else:
        return reverse_word(word[1:]) + word[0]
#s[-1]+reverse_string_recursive(s[:-1])
paragraph = input().split()
a=""
for i in range(len(paragraph)):
    if i== len(paragraph)-1:
        a+=reverse_word(paragraph[i])
    else:
        a+=reverse_word(paragraph[i])+" "
print(a)
