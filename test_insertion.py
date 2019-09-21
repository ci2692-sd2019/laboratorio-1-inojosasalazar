'''
Autores:
Alejandro Salazar 16-11080
Cristian Inojosa 17-10285
'''

from insertion import insertion_sort

numbers = []

with open('./numbers.txt', 'r') as file:
	numbers = list(map(int, file.readlines()))

print('Array original:\n', numbers)

insertion_sort(numbers)

print('Array ordenado:\n', numbers)

try:
	assert all((numbers[i] <= numbers[i+1]) for i in range(0, len(numbers)-1))
	print('Prueba pasada')
except:
	print('Prueba fallida')