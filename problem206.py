from math import sqrt

def decnum(x):
    return str(1000000000+int(x)-1)[1:]

def makenum(z):
    return int("1"+z[0]+"2"+z[1]+"3"+z[2]+"4"+z[3]+"5"+z[4]+"6"+z[5]+"7"+z[6]+"8"+z[7]+"9"+z[8]+"0")

x="999999999"

while True:
	rt=sqrt(makenum(x))
	if rt-int(rt)==0:
		print("Solution:", rt)
		break
	x=decnum(x)