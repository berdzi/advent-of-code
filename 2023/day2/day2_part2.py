import sys

def get_input(fn):
	f = open(fn,mode="r")
	x = f.read().splitlines()
	f.close()
	return x


inp = get_input(sys.argv[1])


ids=[]
summ=0
for row in inp:
	row=row.strip()
	game_id,games_string=row.split(":")
	s,id=game_id.split(" ")
	rounds=games_string.split(";")
	cubes={"red":[],"green":[],"blue":[]}
	for roundrow in rounds:
		rounds = [x.strip() for x in roundrow.split(",")]
		for cube in rounds:	
			cube_number,cube_color=cube.split(" ")		
			cubes[cube_color].append(int(cube_number))
	mul=1
	for numbers in cubes.values():
		mul*=max(numbers)
	summ+=mul
		
print(summ)