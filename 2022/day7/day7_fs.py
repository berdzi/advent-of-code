#file system based solution
#not proud of it
import sys
import os

def get_input(fn):
	f=open(fn)
	x=f.read().splitlines()
	f.close()
	return x
	

def create_file(fn,size):
	bytes = size*"#"
	f=open(fn,"w")
	f.write(bytes)
	f.close()

#https://www.thepythoncode.com/article/get-directory-size-in-bytes-using-python
def get_directory_size(directory):
    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                try:
                    total += get_directory_size(entry.path)
                except FileNotFoundError:
                    pass
    except NotADirectoryError:
        return os.path.getsize(directory)
    except PermissionError:
        return 0
    return total
	
		
if __name__ == '__main__':

	inp = get_input(sys.argv[1])
	
	#part 1

	#create filesystem
	path=os.getcwd()+'\\'
	rootPath = path

	try:
		os.mkdir(path+"root")
	except:
		pass
	os.chdir(path+"root")
	
	for row in inp:		
		row_s = row.split(' ')
		if len(row_s)==3: #cd
			name = row_s[2]
			if name=="/":
				os.chdir(rootPath+"root")
			else:
				os.chdir(path+name)
			path = os.getcwd()+"\\"
		else:
			if (row_s[0].isnumeric()): #create file
				file_size,file_name = row_s
				try:
					create_file(path+file_name,int(file_size))
				except:
					pass
			if (row_s[0]=="dir"):	#create dir
				dir_name = row_s[1]
				try:
					os.mkdir(path+dir_name)
				except:
					pass
			

	# calculate directories and sum	
	solution_part1 = 0
	
	dirs_sizes = []
	for (root,dirs,files) in os.walk(rootPath, topdown=True):
		size = 0
		for d in dirs:
			dp = os.path.join(root,d)		
			ds = get_directory_size(dp)
			dirs_sizes.append(ds)
			if (ds<100000):
				solution_part1+=ds

	print(solution_part1)
	
	#part 2
	dirs_sizes_sorted = sorted(dirs_sizes)

	max_hdd_space = 70000000
	required_space = 30000000
	unused_space = max_hdd_space - dirs_sizes_sorted[-1]
	space_to_free_up = required_space - unused_space
	
	
	for ds in dirs_sizes_sorted:
			if ds>=space_to_free_up:
				print(ds)	
				break