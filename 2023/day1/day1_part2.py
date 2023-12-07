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
	
summ=0
overlaps={}

dg={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
#Create overlaps dictionary
for x in dg.keys():
	for y in dg.keys():
		if x[-1]==y[0]:
			overlaps[x+y[1:]] = x+y

#correct overlaps
for row in inp:
	for x in overlaps.keys():
		row=row.replace(x,overlaps[x])
#replace digits
	for k in dg.keys():
		row=row.replace(k,str(dg[k]))
	number = extract_numbers(row)
	number=number[0]+number[-1]
	summ=summ+int(number)
		
print(summ)