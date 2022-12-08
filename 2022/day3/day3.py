import sys

def getInput(fn):
    f=open(fn)
    x=f.read().splitlines()    
    f.close()
    return x

def findCommon(row):
    l=len(row)
    half=l//2
    left=row[:half]
    right=row[half:]
    s1=set(left)
    s2=set(right)
    return ''.join(s1.intersection(s2))


def calcVal(code):
    acode = ord(code)
    if acode<=90:
        acode=acode-38
    else:
        acode=acode-96
    return acode

def chunkList(rows,chunk_size):
    c=0
    chunk=[]
    out=[]
    for i in rows:
        chunk.append(set(i))
        c=c+1
        if c%chunk_size==0:
            out.append(chunk)
            chunk=[]
    return out

def findBadge(chunk):
    return ''.join(set.intersection(*chunk))


#part 1
inp = getInput(sys.argv[1])
commons=list(map(findCommon,inp))
commonValues=list(map(calcVal,commons))
total=sum(commonValues)
print(total)

#part 2
chunkedListSet=chunkList(inp,3)
badges=list(map(findBadge,chunkedListSet))
badgesValues=list(map(calcVal,badges))
print(sum(badgesValues))
