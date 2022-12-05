from functools import reduce

def mul(l):
	return reduce((lambda x,y: x*y),l)

def get_input(fn):
	f = open(fn,mode="r")	
	x=f.read().splitlines()
	f.close()
	return x
	

def calculatePaperSize(data):
	l,w,h = list(map(int,data.split('x')))
	rects = [l*w,w*h,h*l]
	size = sum(rects)*2+min(rects)
	return size
	

def calculateRibbon(data):
	lwh = list(map(int,data.split('x')))
	s1,s2,s3 = sorted(lwh)
	bow = mul(lwh)
	return 2*s1+2*s2+bow
	
	


inp = get_input("day2_input.txt")
#part 1
totalPaper = sum(list(map(calculatePaperSize,inp)))
print(totalPaper)

#part 2
totalRibbon = sum(list(map(calculateRibbon,inp)))
print(totalRibbon)
	
	