#!/usr/bin/env python3

def solution(year):
	
	# if exactly dividisible by 100 
	# then
	remainder = year % 100
	if remainder == 0: # exactly divided
		century = year // 100
	else: 
		century = year // 100 + 1
		
	return century
