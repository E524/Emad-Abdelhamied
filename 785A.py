n=int(input())
dict={'Tetrahedron':4,'Cube':6,'Octahedron':8,'Dodecahedron':12,'Icosahedron':20}
Sum=0
while(n>0):
    x=input()
    Sum+=dict[x]
    n-=1
print(Sum)