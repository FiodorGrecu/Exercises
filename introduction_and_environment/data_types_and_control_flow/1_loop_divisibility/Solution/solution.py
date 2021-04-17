
data=[]
for x in range( 51 ):
    if (x % 5 == 0 ) and ( x % 7 == 0):
        data.append(str(x))
print (','.join(data))