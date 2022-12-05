def get_input(fn):
	f = open(fn,mode="r")
	x = f.read().splitlines()
	f.close()
	return x

	
#part 1
inp = get_input("day1_input.txt")
c=1
elves={}
elves[c]=[]
for v in inp:
	if v=='':
		c=c+1
		elves[c]=[]		
	else:
		elves[c].append(int(v))

maxcals=list(map(sum,elves.values()))
s = sorted(maxcals,reverse=True)
print(s[0])

#part2
top3 = s[0]+s[1]+s[2]
print(top3)





	