import sys

def get_input(fn):
    f=open(fn,"r")
    x=f.read().splitlines()
    f.close()
    return x



inp=get_input(sys.argv[1])

#part 1
x=1
cycles=0
out={}

cycles2check=[20]
cycles2check.extend(range(60,221,40))

for row in inp:
    r_list=row.split(' ')
    if r_list[0]=='addx':
        x=x+int(r_list[1])
        cycles+=2
    else:
        cycles+=1

    out[cycles]=x

max_key=max(out.keys())

v=1
for x in range(1,max_key+1):
    if x in out.keys():
        v=out[x]
    else:
        out[x]=v

total=0
for i in cycles2check:
    total+=out[i-1]*i

print(total)

#part 2
out = dict(sorted(out.items()))

s="#"
for c,x in out.items():
	if c%40==0 and c<max_key:
		s+="\n"
	if c%40 in range(x-1,x+2):
		s+="#"
	else:
		s+="."
		
print(s)