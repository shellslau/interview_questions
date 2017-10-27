def findMin(dataSet):
    if not dataSet:
        return None
    
    if dataSet[0] == None:
        dataSet.remove(None)
        
    m = dataSet[0]
    for integer in dataSet:
        if integer and integer < m:
            m = integer
    return m
    
def findOverallMin(data1, data2, data3):
    mins = []
    mins.append(findMin(data1))
    mins.append(findMin(data2))
    mins.append(findMin(data3))
    return findMin(mins)

def findSum(dataSet):
    if not dataSet:
        return None
    
    sum = 0
    for integer in dataSet:
        sum += integer
    return sum, len(dataSet)

def findOverallMean(data1, data2, data3):
    sums = []
    sum1, size1 = findSum(data1)
    sums.append(sum1)
    sum2, size2 = findSum(data2)
    sums.append(sum2)
    sum3, size3 = findSum(data3)
    sums.append(sum3)
    
    totalSum = float(findSum(sums)[0])
    totalInts = size1 + size2 + size3
    return totalSum / totalInts

def findOverallMedian(data1, data2):
    data1.sort()
    data2.sort()
    median1 = data1[len(data1)/2]
    median2 = data2[len(data2)/2]
    if median1 > median2:
        if data1.index(median2):
            data1med = data1[data1.index(median2):data1.index(median1)]
        else:
            data1med = data1[:data1.index(median1)]
        if data2.index(median1):
            data2med = data2[data2.index(median2):data2.index(median1)]
        else:
            data2med = data2[data2.index(median2):]
    elif median1 < median2:
        if data1.index(median2):
            data1med = data1[data1.index(median1):data1.index(median2)]
        else:
            data1med = data1[data1.index(median1):]
        if data2.index(median1):
            data2med = data2[data2.index(median1):data2.index(median2)]
        else:
            data2med = data2[:data2.index(median2)]
    else:
        return median1
    medList = (data1med + data2med)
    medList.sort()
    return medList[len(medList)/2]