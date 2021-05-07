#!/usr/bin/python3
def roman_to_int(roman_string):
	rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	integer = 0
	length = len(roman_string)
	for i in range(0, length):
		if i > 0 and rom_val[roman_string[i]] > rom_val[roman_string[i - 1]]:
			integer += rom_val[roman_string[i]] - 2 * rom_val[roman_string[i - 1]]
		else:
			integer += rom_val[roman_string[i]]
	return integer
