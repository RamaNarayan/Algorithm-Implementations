import random
import time
def partition(a,p,r):
	i = p-1
	x = a[r]
	#print("p " + str(p))
	#print("r "+ str(r))
	#print("pivot "+str(x))
	k = r
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
	return i + 1

def quicksort(A,p,r,count):
	if p<r:
		#count = 
		count+1
		q = partition(A,p,r)
		#print(A)
		#print(q)
		#print("quicksort "+str(p)+str(q-1))
		quicksort(A,p,q-1,count)
		#print("quicksort "+str(q+1)+str(r))
		quicksort(A,q+1,r,count)

#A = [3,-1,2,5,6,-2,7,9,10,-5,-6,4,-5,-5,-5,-5,-5,-5]
#A = [5,1,4,-3,-5,3,4]
count = 0;
A = []
for x in range(0,100000):
	A.append(random.randint(-100,100))
print("Im done creating random")
start = time.time()
quicksort(A,0,len(A)-1,count)
print(A)
end = time.time()
quickTime = end-start
print(quickTime)
print(count)