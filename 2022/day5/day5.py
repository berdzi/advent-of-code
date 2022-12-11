def getInput(fn):
	f = open(fn,"r")
	x = f.read().splitlines()
	f.close()
	return x

stack=[]
control=[]
colNums = None

def parseInput(inp):
		s=[]
		c=[]
		for line in inp:
			if '[' in line:
				s.append(line)
			elif 'move' in line:
				c.append(line)
		return [s,c]
				
		
				
def parseStack(stack):
	indexes = list(range(1,36,4)) #indexes of colums
	symbols = list(range(65,91)) # ascii codes of letters
	columns={} #add to columns by index in string
	out={}
	for line in stack:
		for idx in indexes:
			try:
				c=line[idx]
			except:
				continue
			if ord(c) in symbols:
				if idx not in columns.keys():
					columns[idx]=""
				columns[idx]=columns[idx]+c
				
	#turn into stacks
	newIdx=1
	for idx in sorted(columns):
		out[newIdx]=list(columns[idx][::-1])
		newIdx+=1
		
	return out
	
def execControlMoves(control,model):
	for cmd in control:
		execMove(cmd,model)
	
	
def execMove(moveCommand,model):
	moveCmdList=moveCommand.split(' ')
	cnt = int(moveCmdList[1])
	src = int(moveCmdList[3])
	dst = int(moveCmdList[5])
	if model==9000:
		move(src,dst,cnt)
	else:
		moveMulti(src,dst,cnt)
	
	
def move(src,dst,cnt):
	for i in range(cnt):
		crate = stacks[src].pop()
		stacks[dst].append(crate)

def moveMulti(src,dst,cnt):
	#take first cnt elements from the stack
	crates = stacks[src][-cnt:] 
	del stacks[src][-cnt:]
	#add to another stack
	stacks[dst].extend(crates)

def getTopElements(stacks):
	outStr=""
	for stack in stacks.values():
		top = stack[-1]
		outStr+=top
	return outStr

#part 1
inp = getInput("day5_input.txt")

stack,control = parseInput(inp)
stacks = parseStack(stack)

execControlMoves(control,9000)
print(getTopElements(stacks))

#part 2
stack,control = parseInput(inp)
stacks = parseStack(stack)

execControlMoves(control,9001)
print(getTopElements(stacks))