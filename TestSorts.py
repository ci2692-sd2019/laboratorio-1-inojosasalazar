'''
Autores:
Alejandro Salazar 16-11080
Cristian Inojosa 17-10285
'''

import Sorts
import time
import sys
from random import randint

algorithm = str(sys.argv[1])
n = int(sys.argv[2])

A = [randint(-2*n, 2*n) for i in range(n)]

try:
	start = time.time()
	func = getattr(Sorts, algorithm)
	func(A, 0, len(A))
	end = time.time()

	try:
		assert all((A[i] <= A[i+1]) for i in range(0, len(A)-1))
		print('Prueba pasada')
	except:
		print('Prueba fallida')

	passedtime = (end-start)*1000
	print("Tiempo: {}".format(passedtime))

except AttributeError:
	print("{} function not found".format(algorithm))