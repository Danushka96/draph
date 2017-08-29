#Author : Danushka Herath
#Profile: https://github.com/danushka96

#This is the Implementation of Graph Data Structure using Two Linked Lists

# Node Implementation
#Class node for edges
class edgenode:
	def __init__(self,data):
		self.data=data
		self.next=None

#class node for Vertexes
class vertnode:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.bottom=None

#main class for graph

class graph:
	def __init__(self):
		self.head=None
		self.count=0

	#Add a New Vertex
	def addvert(self,value):
		new=vertnode(value)
		if (self.head==None):
			self.head=new
		else:
			temp=self.head
			while (temp.bottom!=None): #find for a node where next one is free for enter
				temp=temp.bottom
			temp.bottom=new 	#Add the created new node to the free space
		self.count+=1

	#Add a New Edge
	def addedge(self,fromm,to):
		if (self.head==None):
			print("The Graph is Empty! Enter some Nodes") #If there exist no vertex in the graph show this error
		else:
			temp=self.head
			while (temp.data!=fromm):
				temp=temp.bottom
				if (temp.data==None):
					print("The vertex not found in the graph") #If Entered vertex is not found display this
					break
			edge=edgenode(to)
			if (temp.next==None):
				temp.next=edge
			else:
				tempedge=temp
				while (tempedge.next!=None): #Find the node which next one is empty
					tempedge=tempedge.next
				tempedge.next=edge

	#Print the Whole Graph
	def printme(self):
		temp=self.head
		while (temp!=None):
			print(temp.data, end="")
			print("\t","-->","\t", end="")
			hr=temp.next
			while (hr!=None):
				print(hr.data,",", end="")
				hr=hr.next
			temp=temp.bottom
			print()

	#Print the Number of Indegrees to a selected Node
	def indegree(self,node):
		temp=self.head
		count=0
		while(temp!=None):
			hr=temp
			while(hr!=None):
				if (hr.data==node):
					count+=1
				hr=hr.next
			temp=temp.bottom
		print("The Number of Indegrees for node ",node," is ",count)

	#Print the Number of Indegrees to a selected Node
	def outdegree(self,node):
		temp=self.head
		count=0
		while (temp.data!=node):
			temp=temp.bottom
		temp=temp.next
		while (temp!=None):
			count+=1
			temp=temp.next
		print("The Number of Outdegrees for node ",node," is ",count)
#End of the Class graph

def addvertlooper():
	d=input("Enter vertex")
	addvert(d)
	print()
	ans=input("Do you want to input another vertex?(Y/N)")
	if (ans.upper()=="Y"):
		addvertlooper()
	elif (ans.upper()=="N"):
		menu()
	else:
		print("Invalied Input Try Again!")
		menu()

def addedgelooper():
	d=input("Enter Vertex From")
	e=input("Enter Vertex To")
	addedge(d,e)
	print()
	ans=input("Do you want to input another edge?(Y/N)")
	if (ans.upper()=="Y"):
		addvertlooper()
	elif (ans.upper()=="N"):
		menu()
	else:
		print("Invalied Input Try Again!")
		menu()

def interface():
	print("_____________________________________________________________________________________________________________UCSC_____")
	print("  ________                        .__      .____     .__          __                .___ .____     .__           __   ")
	print(" /  _____/_______ _____   ______  |  |__   |    |    |__|  ____  |  | __  ____    __| _/ |    |    |__|  _______/  |_ ")
	print("/   \  ___\_  __ \\\_   \  \____ \ |  |  \  |    |    |  | /    \ |  |/ /_/ __ \  / __ |  |    |    |  | /  ___/\   __\\")
	print("\    \_\  \|  | \/ / __ \_|  |_> >|   Y  \ |    |___ |  ||   |  \|    < \  ___/ / /_/ |  |    |___ |  | \___ \  |  |  ")
	print(" \______  /|__|   (____  /|   __/ |___|  / |_______ \|__||___|  /|__|_ \ \___  >\____ |  |_______ \|__|/____  > |__|  ")
	print("        \/             \/ |__|         \/          \/         \/      \/     \/      \/          \/         \/        ")
	print("______________________________________________________________________________________________________________________")
	print()
	print("This programme is based on Basic Graph Operations")

def menu():
	print("Select the Command and enter the number of the Command")
	print()
	print("//////////////////////////////////////////////////////////////////////////////////////////////")
	print("// 1.Create graph \t 2.Enter new Vertex \t 3.Enter new Edge \t 4.number of vertex //")
	print("// 5.Indegree \t \t 6.Outdegree \t \t 7.Print Linked List \t 8.Exit \t    //")
	print("//////////////////////////////////////////////////////////////////////////////////////////////")
	x=int(input("Enter the Command Number: "))

	if (x==1):
		print("The new Graph created Successfully")
	elif (x==2):
		addvertlooper()
	elif (x==3):
		addedgelooper()
	elif (x==4):
		
a=graph()
