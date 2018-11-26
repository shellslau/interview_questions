#
# Complete the 'textQueries' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY sentences
#  2. STRING_ARRAY queries
#

def textQueries(sentences, queries):
    wordSentences = []
    for i in range(len(sentences) - 1):
        sentences[i] = sentences[i].split()
    for query in queries:
        places = []
        words = query.split()
        for i in range(len(sentences)):
            flag = True
            sentence = sentences[i]
            for word in words:
                if word not in sentence:
                    flag = False
            if flag:
                places.append(i)
        if places:
            wordSentences.append(places)
        else:
            wordSentences.append([-1])

    for array in wordSentences:
        strArray = ''
        for item in array:
            strArray = strArray + str(item) + ' '
        print strArray
