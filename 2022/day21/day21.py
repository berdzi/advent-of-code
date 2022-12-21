import sys

def get_input(fn):
	out={}
	f=open(fn,"r")
	x=f.read().splitlines()
	for a in x:
		name,val = a.replace(" ","").split(":")
		out[name]=val
	f.close()	
	return out



def get_ints(vars):
	ints={}
	for name,val in vars.items():
		if val.isnumeric():
			ints[name]=val
	
	return ints
			

def replace_vars(vars,ints):
	for k,v in ints.items():
		if k in used_int:
			continue
		for x,y in vars.items():
			if x in calculated_vars:
				continue
			if k in y:
				vars[x]=y.replace(k,ints[k])
				used_int.add(k)
				break		
	return vars
	

def calc_vars(vars,ints):
	for x,y in vars.items():
		if x in calculated_vars:
			continue
		try:
			calc = int(eval(y))
			ints[x]=str(calc)
			calculated_vars.add(x)
		except:
			pass
			
	return ints


def search(el):
	for k,v in vars.items():
		if k==el:
			if not v.isnumeric():
				left,right = v[:4],v[5:]
				to_calc.add(left)
				to_calc.add(right)
				search(left)
				search(right)

to_calc=set()

#part 1
#sets to check if the vars and ints already been calculated / used
used_int=set()
calculated_vars=set()

vars = get_input(sys.argv[1])
ints = get_ints(vars)

first,second=vars['root'].split('+')

while 'root' not in calculated_vars:
	vars = replace_vars(vars,ints)
	ints = calc_vars(vars,ints)


print(ints['root'])


#part 2
second_element_value = ints[second]

vars = get_input(sys.argv[1])
vars_copy=vars.copy()
ints = get_ints(vars)
ints_copy=ints.copy()

#optimization
#search only vars needed to calculate the first number 
to_calc.add(first)
search(first)

outvars={}
for k in vars:
	if k in to_calc:
		outvars[k]=vars[k]

ints = get_ints(outvars)
ints_copy=ints.copy()
vars = outvars.copy()
vars_copy = vars.copy()

#bruteforcing humn value - works for test , never ending for real input
#didn't solved second part
#in fact we need only find the first value the second does not depend on the humn

humn = 0

while True:
	used_int=set()
	calculated_vars=set()
	
	vars = vars_copy.copy()
	ints = ints_copy.copy()
	ints['humn']=str(humn)
	
	while True:
		vars = replace_vars(vars,ints)
		ints = calc_vars(vars,ints)
		if first in calculated_vars: #and second in calculated_vars:
			break
			
	if ints[first]==second_element_value:
		break

	humn+=1

print(humn)