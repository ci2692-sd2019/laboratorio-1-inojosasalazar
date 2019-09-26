'''
Autores:
Alejandro Salazar 16-11080
Cristian Inojosa 17-10285
'''

def insertion_sort(array:[int]):
	N = len(array)

	for i in range(1, N):
		current = array[i]
		j = i-1
		while(j >= 0 and current < array[j]):
			array[j+1] = array[j]
			j -= 1
		array[j+1] = current
