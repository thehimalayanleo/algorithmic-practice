#!/usr/bin/env python3

def solution(inputString):
	start = 0 
	end = len(inputString) - 1
	if start == end: # if both are 0 then empty string
		return True 
	while start < end: # as long as the start is below
	# the end
		if inputString[start] == inputString[end]: # if elements are equal increment by one
			start += 1
			end -= 1
		else: # otherwise not a palindrome
			return False 
	return True 
	
				
			
