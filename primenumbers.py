
def primenumbercheck(x):
    modulus = []
    for i in range(2,x):
        modulus.append(x % i)
    if 0 not in modu:
        return(x)

def primenumbersinrange(y):
    primenumbers = []
    for j in range(2,y):
        pn = primenumbercheck(j)
        if pn is not None:
            primenumbers.append(pn)
    print(primenumbers)
    
primenumbersinrange(100) # this will print all print numbers in the range of 100.
