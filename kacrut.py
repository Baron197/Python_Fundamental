import math

n = int(input('n = '))

t = 0
op = True

while(n > 0) :
    if(op) :
        t += n % 10
    else :
        t -= n % 10
    
    op = not(op)
    n = math.floor(n/10)

print(t)
if(t % 11 == 0) :
    print('yes')
else : 
    print('no')