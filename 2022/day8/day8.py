import sys

def get_input(fn):
	f=open(fn,"r")
	x=f.read().splitlines()
	f.close()
	return x

#get element from list
#build list of these elements
#substract input row and list_of_elements
#if all elements on the left or right from checked<0 means it is visible
def is_visible(row,idx):
	if idx==0 or idx==len(row)-1:
		return True
	else:		
		el=row[idx]
		checked_list_row = [el]*len(row)
		check_list = [int(a-b) for a, b in zip(row, checked_list_row)]	
		is_visible = all(x<0 for x in check_list[:idx]) or all(x<0 for x in check_list[idx+1:])
						
	return is_visible
	

def calculate_max_view_distance(row,idx):
	el=row[idx]
	checked_list_row = [el]*len(row)
	check_list = [int(a-b) for a, b in zip(row, checked_list_row)]
	
	right = check_list[idx+1:]
	left = check_list[:idx][::-1]
		
	cnt_right = next((idx for idx,x in enumerate(right) if x>=0),len(right)-1)+1
	cnt_left = next((idx for idx,x in enumerate(left) if x>=0),len(left)-1)+1
	
	return cnt_left*cnt_right
	
	
	
def get_visible_trees_in_rows(matrix):
	out=[]
	for row in matrix:
		out_row=[]
		for i in range(len(row)):
			v=is_visible(row,i)
			out_row.append(v)
		out.append(out_row)
	return out
	
#check in rows but on transposed matrix :)
def get_visible_trees_in_cols(matrix):
	matrix_transposed = list(map(list,[*zip(*matrix)]))
	return get_visible_trees_in_rows(matrix_transposed)
	
	
def count_max_distance_rows(matrix):
	out=[]
	for row in matrix:
		out_row=[]
		for i in range(len(row)):
			v=calculate_max_view_distance(row,i)
			out_row.append(v)
		out.append(out_row)
	return out
	
	
#check in rows but on transposed matrix :)
def count_max_distance_cols(matrix):
	matrix_transposed = list(map(list,[*zip(*matrix)]))
	return count_max_distance_rows(matrix_transposed)
	

#compare elements from input matrix and trasnsposed
#if one of them true means the tree is visible
def count_visible_trees(visible_trees_in_rows,visible_trees_in_cols):
	out=[]
	l = len(visible_trees_in_rows[0])
	for x in range(l):
		for y in range(l):
			out.append(visible_trees_in_rows[x][y] or visible_trees_in_cols[y][x])
			 
	return sum(list(map(int,out)))
	
def count_distances(count_max_distance_rows,count_max_distance_cols):
	out=[]
	l = len(count_max_distance_rows[0])
	for x in range(l):
		for y in range(l):
			out.append(count_max_distance_rows[x][y]*count_max_distance_cols[y][x])
			 
	return max(out)
	
	
def get_matrix(inp):	
	matrix=[]
	for row in inp:
		rowx = list(map(int,list(row)))
		matrix.append(rowx)	
	return matrix
	
inp = get_input(sys.argv[1])
matrix = get_matrix(inp)

#part 1
trees_in_rows = get_visible_trees_in_rows(matrix)
trees_in_cols = get_visible_trees_in_cols(matrix)
count_visible_trees = count_visible_trees(trees_in_rows,trees_in_cols)

print(count_visible_trees)

#part 2
distance_rows = count_max_distance_rows(matrix)
distance_cols = count_max_distance_cols(matrix)
cd = count_distances(distance_rows,distance_cols)

print(cd)


	