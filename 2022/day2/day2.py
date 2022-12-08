import sys
#AX - rock
#BY - paper
#CZ - scissors


#X - lose
#Y - draw
#Z - win

def getInput(fn):
    f=open(fn,"r")
    x = f.readlines()
    x = list(map(str.strip,x))
    f.close()
    return x

def findMoves(row):
    results = {'Z': ['CX','AY','BZ'],'X':['BX','CY','AZ'],'Y':['AX','BY','CZ']}

    op,result = row.split(' ')
    mymoves = results[result]
    for x in mymoves:
        if x[0]==op:
            return op+' '+x[1]
    

def calc(row):
    points = {'A':1,'B':2,'C':3,'X':1,'Y':2,'Z':3}
    wins=['CX','AY','BZ']
    op,me = row.split(' ')

    pts = 0

    if op+me in wins:
        pts=pts+6
    elif points[op]==points[me]:
        pts=pts+3

    pts=pts+points[me]
    return pts

inp = getInput(sys.argv[1])

#part 1
total = sum(list(map(calc,inp)))
print(total)


#part 2
moves = list(map(findMoves,inp))
total = sum(list(map(calc,moves)))
print(total)
