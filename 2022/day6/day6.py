import sys

def getInput(fn):
	f=open(fn,"r")
	x=f.readline()
	f.close()
	return x
	
def isUniq(chunk):
	return len(list(chunk))==len(set(chunk))


def findMarkerPosition(inp,markerLen):
	l = len(inp)
	for i in range(0,l):
		chunk=inp[i:i+markerLen]	
		if len(chunk)==markerLen:
			if isUniq(chunk):
				return i+markerLen
	
inp = getInput("day6_input.txt")
markerSignalPosition = findMarkerPosition(inp,4)
print(markerSignalPosition)
markerMessagePosition = findMarkerPosition(inp,14)
print(markerMessagePosition)