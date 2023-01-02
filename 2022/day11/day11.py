import sys

def get_input(fn):
    f=open(fn,"r")
    x=f.read().splitlines()
    f.close()
    return x

def parse_input(inp):
	for x in inp:
		if "Monkey" in x:
			ms,idx = x.replace(':','').split(' ')
			idx=int(idx)
		if "Starting items" in x:
			st,items_str=x.split(':')
			items = items_str.replace(" ","").split(",")
			items = list(map(int,items))
			monkeys[idx]=items
		if "Operation" in x:
			op=x.split(':')[1].replace(" ","").split("=")[1]
			operations[idx]=op
		if "Test" in x:
			tv = int(x.split(':')[1].split(' ')[-1])
			divisables[idx]=tv
		if "If true" in x:
			to_monkey_true[idx]= int(x.split(':')[1][-1])
		if "If false" in x:
			to_monkey_false[idx]= int(x.split(':')[1][-1])


def calc_part(part_num):
	if part_num==1:
		rounds=20
	else:
		rounds=10000
		
	for m in monkeys.keys():
		inspections[m]=0
		
	for r in range(rounds):
		for m,items in monkeys.items():
			for item_idx,old in enumerate(items):
				new = eval(operations[m])
				tm = to_monkey_false[m]
				if part_num==1:
					new = new // 3
				if new % divisables[m]==0:
					tm = to_monkey_true[m]
				monkeys[tm].append(new)
				monkeys[m][item_idx]=""
				inspections[m]+=1
				
		for m in monkeys.keys():        
			monkeys[m] = [x for x in monkeys[m] if x!=""]    


#part 1
new=0
monkeys={}
operations={}
divisables={}
to_monkey_true={}
to_monkey_false={}
inspections={}

inp = get_input(sys.argv[1])
parse_input(inp)
calc_part(1)

si = sorted(inspections.values())
res = si.pop()*si.pop()
print(res)

#part 2
monkeys={}
operations={}
divisables={}
to_monkey_true={}
to_monkey_false={}
inspections={}

inp = get_input(sys.argv[1])
parse_input(inp)
calc_part(2)

si = sorted(inspections.values())
res = si.pop()*si.pop()
print(res)