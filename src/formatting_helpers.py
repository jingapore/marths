import numpy as np
from itertools import product

def chunker(seq, size):
	return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def npMatrix_to_latex(matrix):

	latex_str = r'\begin{bmatrix}'
	
	shape = matrix.shape
	
	row_num = [i for i in range(0, shape[0])]
	col_num = [i for i in range(0, shape[1])]
	col_size = shape[1]

	tuple_indices = list(product(row_num, col_num))

	# for count, matrix_idx in enumerate(tuple_indices, start=1):
	# 	latex_str += r'{}\\'.format(matrix.item(idx))

	for row in chunker(np.asarray(matrix).flatten(), col_size):
		for item in row:
			latex_str += r'{}&'.format(item)
		latex_str = latex_str[:-1] + r'\\'

	latex_str += r'\end{bmatrix}'

	return latex_str