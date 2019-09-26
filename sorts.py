'''
Autores:
Alejandro Salazar 16-11080
Cristian Inojosa 17-10285
'''

''' INSERTON SORT '''

def insertion_sort(array:[int]):
	N = len(array)

	for i in range(1, N):
		current = array[i]
		j = i-1
		while(j >= 0 and current < array[j]):
			array[j+1] = array[j]
			j -= 1
		array[j+1] = current

''' MERGE SORT '''

def merge_sort(A:[int], p:int, r:int):
	if r-p < 2:
		return A[p]

	q = (p + r) // 2

	merge_sort(A, p, q)
	merge_sort(A, q, r)

	merge(A, p, q, r)
