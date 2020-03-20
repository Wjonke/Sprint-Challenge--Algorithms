'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
word = "thisthing"
i = 0
occurrences = 0

def count_th(word):
    global i, occurrences

    if i + 2 > len(word):
        x = occurrences
        occurrences = 0
        i = 0
        return x

    if word[i : i + 2] == "th" :
        occurrences += 1
    i +=1

    return count_th(word)


#non-recursive method :)
# def count_th(word):
#     check = "th"
#     count = word.count(check)
#     print(count)
#     return count
print(count_th(word))
count_th(word)