def getMountainIndex(array, target):
    return -1


def findPeakIndex(array):
    midIndex = len(array)/2
    mid = array[midIndex]

    if len(array) == 1:
        return array[0]

    elif len(array) == 2:
        if array[0] > array[1]:
            return 0
        elif array[1] > array[0]:
            return 1
    
    elif array[midIndex - 1] < mid and array[midIndex + 1] < mid:
        return midIndex

    elif array[midIndex - 1] < array[midIndex + 1]:
        return findPeakIndex(array[(midIndex + 1):])

    elif array[midIndex + 1] < array[midIndex - 1]:
        return findPeakIndex(array[:midIndex])

    else:
        raise InputError('Bad Input')



print findPeakIndex(['1', '3', '6', '8', '9', '17', '20', '23', '25', '18', '11', '2'])