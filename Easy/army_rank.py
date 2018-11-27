# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(ranks):
    # write your code in Python 3.6
    s = set([])
    count = 0
    for soldier in ranks:
        s.add(soldier)
    for soldier in ranks:
        if (soldier + 1) in s:
            count += 1
    return count
