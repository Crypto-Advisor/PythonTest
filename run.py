import numpy as np

#This is a test program to run today in class!
# Cntrl + Shift + P   =>  type 'run'  and select 'Run script'
x = np.array([-1.2, 1.2])
np.absolute(x)
np.absolute(1.2 + 1j)

inputs = [-1337.1337, -10.5, -5.5, -1.5, -1, -0.3, -0.113, 0, 0.31, 0.76, 1.3, 1.99, 7.4, 160, 1337, 100, -100]

def squishA(val):
    if val > 100 or val < -100:
        return("Invalid number")
    else:
        calc = ((val*0.01)*0.5) + 0.5
        return(calc)


for x in range(len(inputs)):
    print("Input:", inputs[x], " Out:" , squishA(inputs[x]))
