#
# Complete the 'closest' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def closest(s, queries):
    spots = []
    for query in queries:
        char = s[query]
        i = 1
        flag = False
        while (query - i >= 0) or (query + i < len(s)) and (i < len(s)):
            if (query - i >= 0) and (s[query - i] == char):
                spots.append(query - i)
                flag = True
                break
            elif (query + i < len(s)) and (s[query + i] == char):
                spots.append(query + i)
                flag = True
                break
            i += 1
        if not flag:
            spots.append(-1)
    return spots


def rightest(s, query, right, left):
    string = s[left:right]
    if (s[query] not in string):
        return None
    elif (s[right] == s[query]):
        return right
    else:
        mid = ((right - left)/2) + left
        test = rightest(s, query, right, mid)
        if (test):
            return test
        else:
            return rightest(s, query, mid, left)

def leftest(s, query, right, left):
    string = s[left:right]
    if (s[query] not in string):
        return None
    elif (s[left] == s[query]):
        return left
    else:
        mid = ((right - left)/2) + left
        test = leftest(s, query, mid, left)
        if (test):
            return test
        else:
            return leftest(s, query, right, mid)


def closest(s, queries):
    spots = []
    for query in queries:
        right = leftest(s, query, query+1, len(s))
        left = rightest(s, query, 0, query)
        if (not right and not left):
            spots.append(-1)
        elif (query - left < right - query):
            spots.append(left)
        elif (right - query < query - left):
            spots.append(right)
