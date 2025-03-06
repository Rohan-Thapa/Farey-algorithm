import math
from typing import Union

def fraction(number: float, precision: int) -> Union[str, None]:
    pnts: float
    num: float
    pnts, num = math.modf(number)
    
    round_to: int = len(str(number).split('.')[1])
    pnts = round(pnts, round_to)
    
    a1: int = 1
    a2: int = 1
    b1: int = 0
    b2: int = 1
    
    numerator: int = a1 + b1
    denominator: int = a2 + b2
    
    while precision >= (math.ceil(math.log(denominator, 10))):
        median: float = numerator / denominator
        
        if median > pnts:
            a1 = numerator
            a2 = denominator
        elif median < pnts:
            b1 = numerator
            b2 = denominator
        else:
            return str((int(num) * denominator) + numerator) + " / " + str(denominator)
            
        numerator, denominator = a1 + b1, a2 + b2
        
    temp1: float = (a1 / a2) - pnts
    temp2: float = pnts - (b1 / b2)
    
    if (temp1 - temp2) > 0:
        return str((int(num) * b2) + b1) + " / " + str(b2)
    elif (temp1 - temp2) < 0:
        return str((int(num) * a2) + a1) + " / " + str(a2)
    else:
        return "An Error occurred while calculating!"

print(fraction(126.58215, 0))
