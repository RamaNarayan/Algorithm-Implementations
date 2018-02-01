#partition is based on a[i] < x, =x, >x. Therefore two indices are returned

import random
import time
def partition(a,p,r):
	#a = [8,2,5,4,6,3,4,7,9,10,44,88,4,9,1,2,4]
	i = p-1
	x = a[r]
	#print("p " + str(p))
	#print("r "+ str(r))
	#print("pivot "+str(x))
	#print(x)
	for j in range(p, r):
		#print("number is"+str(a[j]))
		if(a[j]<=x):
			i = i+1
			swap = a[j]
			#print(swap)
			a[j] = a[i]
			a[i] = swap
		#print(a)
	if(a[i+1]>a[r]):
		swap = a[i+1]
		a[i+1] = a[r]
		a[r] = swap
	k= p-1
	for j in range(p, i+1):
		#print("iteration number is"+str(a[j]))
		if(a[j]<x):
			k = k+1
			swap = a[j]
			a[j] = a[k]
			a[k] = swap

	#print(a)
	#print(i+1)
	#print(k+1)
	indexArray = [k+1,i+1]
	return indexArray
	
#A = [-1,4,3,5,3,4,-2,4]
#partition(A,0,len(A)-1)


def quicksort(A,p,r,count):
	if p<r:
		count = count + 1;
		indexArray = partition(A,p,r)
		q = indexArray[0]
		t = indexArray[1]
		#print(A)
		#print(q)
		#print("quicksort "+str(p)+str(q-1))
		quicksort(A,p,q-1,count)
		#print("quicksort "+str(t+1)+str(r))
		quicksort(A,t+1,r,count)

#A = [5,1,4,-3,-5,3,4]

A = []
for x in range(0,100000):
	A.append(random.randint(-100,100))
print("Im done creating random")
count = 0;
start = time.time()
quicksort(A,0,len(A)-1,count)
print(A)
end = time.time()
quickTime = end-start
print(quickTime)
print(count)


