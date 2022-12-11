#https://carboncoffee.hashnode.dev/implementing-general-tree-using-python
#https://stackoverflow.com/questions/39860090/find-element-by-id-in-tree-data-structure
import sys

sumDirs = 0
dirs = []

def get_input(fn):
	f=open(fn)
	x=f.read().splitlines()
	f.close()
	return x
	


class TreeNode:

	def __init__(self,fsunit):
		self.fsunit=fsunit
		self.parent=None
		self.children=[]

	def add_child(self,child):
		child.parent=self
		self.children.append(child)
	   
	def get_level(self):
		level = 0 
		p = self.parent
		while p :
			p = p.parent
			level += 1
		return level
	
	#sum children for each node
	#update current node and its parents
	def calculate_dir_sizes(self):
		for child in self.children:
			p=self.parent
			while p:			
				p.fsunit.size+=child.fsunit.size	
				p=p.parent				
				
			self.fsunit.size+=child.fsunit.size							
			child.calculate_dir_sizes()			
			
	def print_tree(self):
		print('  '*self.get_level() + '|__', end = '')
		print(self.fsunit)
		if self.children:
			for each in self.children:
				each.print_tree()		
		
   
   #made same mistake as this guy
	def find_node(self,name):
		if name=="/":
			return self
		elif name=="..":
			if (self.parent):
				return self.parent
			#else:
			#	return self
		else:			
			for node in self.children:	
				#print(list(map(print,self.children)))
				if node.fsunit.name==name:					
					return node
				else:
					found = node.find_node(name)
					if (found):
						return found
					

	#how not to use globals ????
	def find_dirs(self,maxsize):
		global dirs
		for node in self.children:
			if node.fsunit.type=="dir":
				if node.fsunit.size<=maxsize:
					dirs.append(node.fsunit.size)
				node.find_dirs(maxsize)	
		return dirs
	
		
	def __str__(self):
		return self.fsunit.type+' '+self.fsunit.name+' '+str(self.fsunit.size)
				
class FSunit:
	def __init__(self,type,name,size):
		self.type = type
		self.name = name
		self.size = size
		
	def __str__(self):
			return self.type+' '+self.name+' '+str(self.size)
			
		
if __name__ == '__main__':

	inp = get_input(sys.argv[1])
	#print(inp)
	
	rootDir = FSunit("dir","/",0)
	rootNode = TreeNode(rootDir)
	currentNode = rootNode
	
	for row in inp:
		#print("row: "+row)
		row_s = row.split(' ')
		if len(row_s)==3: #cd
			name = row_s[2]
			print("cd :"+name+"#")
			#print("currentNode PRE: "+str(currentNode))
			#if (name==".."):
			try:
				node = currentNode.find_node(name)
			except:
				print (currentNode)
			#else:
			#	node = rootNode.find_node(name)
			currentNode = node
			print("currentNode POST: "+str(currentNode)+" "+str(currentNode.parent))
			#print(currentNode)
		else:
			if (row_s[0].isnumeric()): #file
				file_size,file_name = row_s
				newFile = FSunit("file",file_name,int(file_size))
				print("create file: "+file_name+"#")
				newNode = TreeNode(newFile)
				currentNode.add_child(newNode)			
			if (row_s[0]=="dir"):
				dir_name = row_s[1]
				print("create dir: "+dir_name+"#")
				newDir = FSunit("dir",dir_name,0)
				newNode = TreeNode(newDir)
				#print(currentNode)
				currentNode.add_child(newNode)
		#node = currentNode.find_node(name)	
	
	rootNode.calculate_dir_sizes()
	dirs = rootNode.find_dirs(100000)
	rootNode.print_tree()
	print(sum(dirs))

	 