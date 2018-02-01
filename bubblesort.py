import random
import time
		
def bubbleSort(a):
	for i in range(0,len(a)):
		for j in range(i+1,len(a)):
			if(a[j] < a[i]):
				swap = a[i]
				a[i] = a[j]
				a[j] = swap

#normal sort
#B = [3,-1,2,5,6,-2,7,9,10,-5,-6,4,-5,-5,-5,-5,-5,-5]
B = []
for x in range(0,100000):
	B.append(random.randint(-100,100))
print("Im done creating random")
start = time.time()
bubbleSort(B)
#print(B)
end = time.time()
normalTime = end-start
print(normalTime)