from math import sqrt;
######################
# Generate Prime Numbers
######################
def isPrime(candidate):
    isP = True;
    if candidate < 1:
	    return False;
    if candidate <= 3:
        return True;
    for x in range(2, int( sqrt(candidate) + 1)):        
        if candidate % x == 0:
            return False;
    return isP;


print(" ".join(map(str, filter(isPrime, [x for x in range(2, int(input()))]))));