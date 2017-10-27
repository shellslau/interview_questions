# "3x-y-2=2y+x-12" 
# x = 1 

# solve for the value of y 

# +, -, no * or / operators 
# implicit multiplication between coefficient and the variable "3x" "40y" 
# only single variable terms - so no "3xy" 
# assume that everything is well formed - no "3-+x2"
import string

# # 

#
#  3 -> [x, y, +, -, #] 333 
#
#

# "3y+2y+4y+7y+12y-3y=x"
# "3y+12-3+4-123

# "3x-4z+5w-2b=y"

# sum of y coefficients for each side 
# sum of the x terms * x 
# 
def solvey(eq, valuesOfVars):
    yside = 0
    xside = 0
    sides = eq.split('=')
    for i in range(2):
        ycoeff = 0
        otherterms = 0
        s = ''
        print "-------------------"
        print "Processing side %s" % sides[i]
        for char in sides[i]:
            if char in ['+', '-', '=']:
                newOther, newY = getTerm(s, valuesOfVars)
                otherterms += newOther
                ycoeff += newY
                s = char
            else:
                s += char
        newOther, newY = getTerm(s, valuesOfVars)
        otherterms += newOther
        ycoeff += newY
        print "ycoeff is %s" % ycoeff
        print "otherterms is %s" % otherterms
        print "-------------------"
        if i == 0:
            yside = ycoeff
            xside = -otherterms
        else:
            yside -= ycoeff
            xside += otherterms
    return xside/yside


def getTerm(s, valuesOfVars):
    if s[-1] in valuesOfVars.keys():
        coeff = s[:-1] # might be a number, might just be "-" or "+"
        if coeff in ['-', '+']:
            coeff += '1'
        term = int(coeff) * valuesOfVars[s[-1]]
        return term, 0
    elif s[-1] == 'y':
        coeff = s[:-1] # might be a number, might just be "-" or "+"
        if coeff in ['-', '+']:
            coeff += '1'
        term = int(coeff)
        return 0, term
    else:
        return int(s), 0
    
    
print solvey('2y+1x=9', {'x':1})
print solvey('8x+8x+5+3=4y', {'x': 2})
print solvey('1y=4-1',{'x': 1})
print solvey('2x-b+y=9c', {'x':1,'b':2,'c':1})
