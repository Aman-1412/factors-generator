number=int(raw_input("Enter your number:"))			#Used abs() to convert -ve nums to +ve
# factors=[]
# for factor in range(1,(number+2)/2):
    # if number%factor==0:
        # factors.append(factor)
# factors.append(number)
# print factors
# print "Num of factors is:",len(factors)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# def factors(number):
	# return [i for i in range(1, (number+2)/2) if not number%i] + [number]		#if not n%i      is equivalent to   if n%i==0

# print factors(number)

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#Factors are always in pairs..ex:36..factors are 6*6,9*4,12*3,18*2,36*1
#And the smaller(of the pair) factor is always less than sqrt(number)
from math import sqrt

def factorsof(number):
	factors = set()				#set is a list with all elements being unique..adding duplicate elements has no effect on it.
	for factor in range(1, int(sqrt(number))+1):
		if number%factor == 0:
			factors.add(factor)					#use add for set instead of append
			factors.add(number/factor)
	return sorted(factors)
	
if __name__ == '__main__':
	print factorsof(number)
