import sys

def get_input(fn):
	f = open(fn,mode="r")
	x = f.read().splitlines()
	f.close()
	return x


inp = get_input(sys.argv[1])


maxcubes={"red":12,"green":13,"blue":14}
ids=[]
sumids=0

for row in inp:
	row=row.strip()
	game_id,games_string=row.split(":")
	s,id=game_id.split(" ")
	rounds=games_string.split(";")
	isGameOk=True
	for roundrow in rounds:
		rounds = [x.strip() for x in roundrow.split(",")]
		for cube in rounds:	
			cube_number,cube_color=cube.split(" ")		
			if not (int(cube_number)<=maxcubes[cube_color]):
				isGameOk=False
				break
	if isGameOk:
		sumids+=int(id)

print(sumids)