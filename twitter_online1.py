# Complete the braces function below.
def braces(values):
    info = []
    for value in values:
        value_prev = ''
        while value and (value_prev != value):
            value = value.replace('()', '')
            value = value.replace('{}', '')
            value = value.replace('[]', '')
        if value:
            info.append('NO')
        else:
            info.append('YES')
    return info

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
