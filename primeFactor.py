import math
def PrimeFactor(n):
	primeBool=[True for i in range(n+1)]
	primeBool[0]=False
	primeBool[1]=False
	primeBool[2]=True
	for i in range(2,int(math.sqrt(n))+1):
    		if primeBool[i]:
        		for j in range(2,int(n/i)+1):
            			primeBool[i*j]=False
	prime_num=[i for i in range(len(primeBool)) if primeBool[i] is True]
	prime_factor=[]
	i=0
	while(n>1):
    		if n%prime_num[i]==0:
        		n/=prime_num[i]
        		prime_factor.append(prime_num[i])
    		else:
        		i+=1
	return max(prime_factor)
