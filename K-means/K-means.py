import math

#Calculate the distance between two points
def distance(p1,p2):
	 return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

def getClusters(points,centroid):
	clusters={}
	for p in points:
		d_old=-1
		for c in centroid:
			d_new=distance(p,centroid[c])
			if d_new<d_old or d_old==-1:
				clusters[p]=c
			d_old=d_new
	return clusters

#Initiation
points=[];clusters={};centroid={};result={}
n_p=int(input("Enter number of points in the data set : "))

for i in range (0,n_p):
	points.append(tuple(float(i) for i in input("Enter coordinates of point "+str(i+1)+" : ").split()))
n_c=len(points)+1

while(n_c>len(points)):
	n_c=int(input("Enter number of clusters to be created (<"+str(len(points))+"): "))
	if n_c > len(points):
		print("Sorry.The maximum number of clusters that can be made is ",len(points))

for i in range(0,n_c):
	centroid[i]=points[i]
clusters=getClusters(points,centroid)

c_old={}
while c_old != clusters:
	c_old=clusters
	for i in range(0,n_c):
		x=0;y=0;count=0
		for p in points:
			if clusters[p]==i:
				x+=p[0];y+=p[1];count+=1
		x/=count;y/=count
		centroid[i]=(x,y)
	clusters=getClusters(points,centroid)	

for key, value in sorted(clusters.items()):
    result.setdefault(value, []).append(key)

for i in result:
	print("\nCluster ",i+1," -> ",result[i], "with Centroid = ",centroid[i])