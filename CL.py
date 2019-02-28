import math
a =int(input("Please input the first coeffient:"))
b =int(input("Please input the second coeffient:"))
c =int(input("Please input the third coeffient:"))
def quad(a,b,c):
    delta=(b*b)-(4*a*c)
    if delta <0:
        delta=-1*delta
        delta=math.sqrt((delta))
        delta=complex(0, delta)
    else:
        delta=math.sqrt(delta)
    firstsolution=(-b+delta)/(2*a)
    secondsolution=(-b-delta)/(2*a)

    print("The first solution is {0}, and the second solution is {1}".format(firstsolution,secondsolution))
   
quad(a,b,c)
