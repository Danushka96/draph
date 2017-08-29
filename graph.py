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

a=graph()
a.addvert(5)
a.addvert(2)
a.addvert(3)
a.addvert(8)
a.addedge(5,2)
a.addedge(5,3)
a.addedge(5,8)
a.addedge(2,5)
a.addedge(2,8)
a.addedge(3,2)
a.printme()