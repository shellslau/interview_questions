# String interpolation - Ruby
# C - "Hello world: %d", 100
# 
# Ruby: "Hello world: #{100 + 100}" -> "Hello world: 200"
#  "Hello world: #{'abc' + 'def'}" -> "Hello world: abcdef"

def string_interpolation(string):
    startIndex = -1
    endIndex = -1
    for i in range(len(string)):
        if string[i] == '#' and i != (len(string) - 1):
            if string[i + 1] == '{':
                startIndex = i
        
        if string[i] == '}' and startIndex != -1 and endIndex == -1:
            endIndex = i
    
    if endIndex == -1 or startIndex == -1:
        return string
    
    function = string[(startIndex + 2):(endIndex)]
    
    args = function.split('+')
    
    if "'" in args[0]:
        inputString = ''
        for arg in args:
            arg = arg.strip().strip("'")
            inputString = inputString + arg
    
    else:
        inputString = 0
        for arg in args:
            inputString = inputString + int(arg.strip())
        inputString = str(inputString)
    
    string  = string[:(startIndex)] + inputString + string[(endIndex + 1):]
    return string

#won't work if given an empty function