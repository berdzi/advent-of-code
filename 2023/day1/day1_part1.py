import re 
import sys

def get_input(fn):
	f = open(fn,mode="r")
	x = f.read().splitlines()
	f.close()
	return x

def extract_numbers(input_string):
    pattern = re.compile(r'\D+')  # \D matches any non-digit character
    numbers = ''.join(pattern.split(input_string))
    return numbers

inp = get_input(sys.argv[1])

#Part1
summ=0
for row in inp:
	number = extract_numbers(row)
	number=number[0]+number[-1]
	summ=summ+int(number)

print(summ)