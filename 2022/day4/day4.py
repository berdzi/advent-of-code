def getInput(fn):
    f=open(fn,"r")
    c=f.readlines()
    c=list(map(str.strip,c))
    f.close()
    return c

def getRange(pair):
    start,end = pair.split('-')
    return list(range(int(start),int(end)+1))

def decodeRow(row):
    out=[]
    firstPair,secondPair=row.split(',')
    firstRange = set(getRange(firstPair))
    secondRange = set(getRange(secondPair))
    return [firstRange,secondRange]

def checkSubsets(setsList):
    x = setsList[0].issubset(setsList[1])
    y = setsList[1].issubset(setsList[0])
    return int(x or y)

def checkOverlapping(setsLists):
    if setsLists[0].intersection(setsLists[1]):
        return 1
    return 0

inp = getInput("day4_input.txt")

ranges = list(map(decodeRow,inp))

#part 1
total = sum(list(map(checkSubsets,ranges)))
print(total)

#part 2
total = sum(list(map(checkOverlapping,ranges)))
print(total)
