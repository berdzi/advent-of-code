import sys

def get_input(fn):
	f=open(fn,"r")
	x=f.read().splitlines()
	x=list(map(list,x))
	f.close()
	return x
	
def decodeLetter(l):
	if l=="S":
		c=97 #small a
	elif l=="E":
		c=122 #small z
	else:
		c=ord(l)	
	return c
	
def checkNeighbour(el,direction,distances,inp,visited):
	x,y=el
	v=inp[y][x]
	next_x,next_y = x+direction[0],y+direction[1]
	c = decodeLetter(v)
	
	if next_x==xlen or next_x<0 or next_y==ylen or next_y<0:
		return False
	
	next_el = [next_x,next_y]
	
	if str(next_el) in visited:
		return False
	
	v_next=inp[next_y][next_x]
	distances[str(next_el)]=distances[str(el)]+1
	c_next = decodeLetter(v_next)
	
	if c_next-c>1:
		return False
	else:
		return [next_x,next_y]
	

def bfs(matrix,start,end,distances):
	#start node in queue
	q=[start]

	#visited nodes
	# as list - 4.4s
	# as set - 0.08s
	visited=set()

	#distance of start point = 0
	distances[str(start)] = 0
	#"right","left","up","down"
	directions = [[1,0],[-1,0],[0,-1],[0,1]]

	#BFS algo
	while q:
		#get fist element from queue
		el=q.pop(0)
			
		#check neighbours of the element
		#if we can move on add to the queue
		for dr in directions:
			neighbour = checkNeighbour(el,dr,distances,matrix,visited)
			if neighbour and neighbour not in q:
					q.append(neighbour)
			
			#add the node to visited
			visited.add(str(el))	
				
	return distances[str(end)]



inp = get_input(sys.argv[1])

xlen=len(inp[0])
ylen=len(inp)
distances = {}

#part 1
for y in range(ylen):
	for x in range(xlen):
		if inp[y][x]=="S":
			start=[x,y]
		if inp[y][x]=="E":
			end=[x,y]
		distances[str([x,y])]=sys.maxsize

shortestDistance = bfs(inp,start,end,distances)
print(shortestDistance)

#part 2
startPoints=[]
pathLengths=[shortestDistance]

#search all starting points
for y in range(ylen):
	for x in range(xlen):
		if inp[y][x]=='a':
			startPoints.append([x,y])

for sp in startPoints:
	for y in range(ylen):
		for x in range(xlen):
			distances[str([x,y])]=sys.maxsize
			
	pl = bfs(inp,sp,end,distances)
	if pl<sys.maxsize:
		pathLengths.append(pl)

print(min(pathLengths))
