#!/usr/bin/env python3

def solution(n):
	# the increment is 1, 5, 13, 25, 
	# 4, 8, 12, 16 is the difference
	if n == 1:
		return 1
	elif n == 2:
		return 5 
	else:
		# 1 + (4 + 8 + 12 + 16 + ...) = 
		# second term = (4 + 8 + 12 + 16 + ...)
		# = 4 (1 + 2 + 3 + 4 + ...)
		# = 4 (1 + ... + n-1)
		# = 4 (n-1) (n-2) / 2
		return 1 + (4 * (n-1) * (n)) / 2
	