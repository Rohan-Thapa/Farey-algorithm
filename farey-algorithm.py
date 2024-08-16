import math

def fraction(number, precision):
    pnts, num = math.modf(number)
    round_to = len(str(number).split('.')[1])
    pnts = round(pnts, round_to)
    a1, a2, b1, b2 = 1, 1, 0, 1
    numerator, denominator = a1 + b1, a2 + b2
    
    while precision >= (math.ceil(math.log(denominator, 10))):
        median = numerator / denominator
        
        if median > pnts:
            a1 = numerator
            a2 = denominator
        elif median < pnts:
            b1 = numerator
            b2 = denominator
        else:
            return (str((int(num) * denominator) + numerator) + " / " + str(denominator))
            
        numerator, denominator = a1 + b1, a2 + b2
        
    # the condition for the value is a1/a2 > pnts > b1/b2
    temp1, temp2 = (a1/a2) - pnts, pnts - (b1/b2)
    
    if (temp1 - temp2) > 0:
        return (str((int(num) * b2) + b1)) +" / "+ str(b2)
    elif (temp1 - temp2) < 0:
        return (str((int(num) * a2) + a1)) +" / "+ str(a2)
    else:
        return "An Error had occured while calculating!"
        
print(fraction(126.58215, 3))
