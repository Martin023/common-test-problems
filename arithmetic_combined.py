import math

def rem(a,b,n):
    res = round((a/b),1)
    calc = (res - math.floor(res))*10
    if n%calc == 0:
        print (True)
    else:
        print (False)
    

rem(10,3,2)