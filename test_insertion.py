from insertion import insertion_sort

numbers = []

with open('./numbers.txt', 'r') as file:
	numbers = file.read().split('\n')
	for index, number in enumerate(numbers):
		numbers[index] = int(number)

	print('Array original:\n', numbers)

insertion_sort(numbers)

print('Array ordenado:\n', numbers)

try:
	assert all((numbers[i] <= numbers[i+1]) for i in range(0, len(numbers)-1))
	print('Todo bien')
except:
	print('Algo salió mal')