
# Getting coordinate points from the user
num_pts = int(input("Enter the number of polygon points: "))
print(" ")
print("Enter the x and y coordinates for polygon points ... ")

Coords = []

for i in range(0,num_pts):
	Coords.append([])
for i in range(0,num_pts):
	for j in range(0,2):
            Coords[i].append(j)
            Coords[i][j] = 0
for i in range(0,num_pts):
    for j in range(0,2):
        print('Point:',i+1,'  Enter x then y:')
        Coords[i][j] = int(input())
print (Coords)

print(" ")
print(f"{'Point':3} {'x':>7} {'y':>9}")
print("-" * 30)

for i in range(0,num_pts):    
    print(f"{i+1:3} {i:10.2f} {j:10.2f}")

# Calculating area of the polygon
while n<=N:
    Coordinates=str(Xs[num_pts-1])+' '+ str(Ys[num_pts-1])
    CD+=Coordinates+'\n'
    if n>1:
        SumA+=(Xs[n-1]+Xs[n-2])*(Ys[n-1]-Ys[n-2])
    n+=1
Ax=SumA/2