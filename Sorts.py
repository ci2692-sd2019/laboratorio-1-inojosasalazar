'''
Autores:
Alejandro Salazar 16-11080
Cristian Inojosa 17-10285
'''

''' INSERTON SORT '''

def InsertionSort(array:[int], p:int, r:int):
	N = len(array)

	for i in range(1, N):
		current = array[i]
		j = i-1
		while(j >= 0 and current < array[j]):
			array[j+1] = array[j]
			j -= 1
		array[j+1] = current

''' MERGE SORT '''

def MergeSort(A:[int], p:int, r:int):
	if r-p >= 2:
		q = (p + r) // 2

		MergeSort(A, p, q)
		MergeSort(A, q, r)

		Merge(A, p, q, r)

def Merge( A: [int], p: int, q: int , r: int):
	
	Left, Right, n , m = [], [], q-p, r-q

	for i in range (n):
		Left.append( A[p+i])

	for i in range (m):
		Right.append( A[q+i])

	Left.append( float("inf") )
	Right.append( float("inf") )
	i, j = 0, 0

	for k in range(p, r):
		if (Left[i] <= Right[j]):
			A[k]= Left[i]
			i+=1
		else:
			A[k]=Right[j]
			j+=1
