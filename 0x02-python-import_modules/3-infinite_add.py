#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	sum = 0
	length = len(argv)
	if length >= 3:
		for i in range(1, length):
			sum += int(argv[i])
		print("{}".format(sum))
	elif length == 1:
		print("0")