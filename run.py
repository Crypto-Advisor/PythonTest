import numpy as np

#This is a test program to run today in class!
# Cntrl + Shift + P   =>  type 'run'  and select 'Run script'
x = np.array([-1.2, 1.2])
np.absolute(x)
np.absolute(1.2 + 1j)

inputs = [0, 0.000027535691114583473, 0.004070137715896128, 0.18242552380635635, 0.2689414213699951, 0.425557483188341, 0.47178002201963243, 0.5, 0.5768852611320463, 0.6813537337890256, 0.8797431375322491, 0.9993891206405656, 3, 1337]

def squishA(val):
    if val > 100 or val < -100:
        return("Invalid number")
    else:
        calc = ((val*0.01)*0.5) + 0.5
        return(calc)

def squishB(val):
    if val <= 0:
        return 0
    else:
        return val

def closeToBoundaryB(val):
    if val > 1:
        return 0
    elif val <= 0.5:
        return val
    else:
        calc = 0.5 - np.power(0.5, (0.5/(val-0.5)))
        return calc

for x in range(len(inputs)):
    print("Input:", inputs[x], " Out:" , closeToBoundaryB(squishB(inputs[x])))
