import sys
sys.set_int_max_str_digits(100000)
state = (1 << 127) | 1

#while True:
for i in range(400):
	print(state & 1, end = '')
	newbit = (state ^ (state >> 1) ^ (state >> 2) ^ (state >> 7))
	state = (state >> 1) | (newbit << 127)
	output = str(state)
	with open("output.txt", "wb") as f:
		f.write(output.encode())

