'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    added = 0
    if len(word) < 2:
        return 0
    if word[0:2] == "th":
        added = 1
    return added + count_th(word[1:])
