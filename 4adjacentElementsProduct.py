#!/usr/bin/env python3

def solution(inputArray):
	# set maximum product to negative infinity
	len_arr = len(inputArray)
	max_prod = -float('inf')
	
	# compute adjacnet products and find the 
	# ones which are maximum by simple sliding
	for indx in range(len_arr - 1):
		A1, A2 = inputArray[indx], inputArray[indx + 1]
		new_prod = A1 * A2 
		if max_prod < new_prod:
			max_prod = new_prod 
			
	return max_prod