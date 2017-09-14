#Author : Danushka Herath
#Profile: https://github.com/danushka96

#This is the Implementation of Graph Data Structure using Two Linked Lists

# Node Implementation
# Class node for edges
import time

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
			found=False
			ftemp=self.head
			while (ftemp!=None):
				if(ftemp.data==value):
					found=True
				ftemp=ftemp.bottom
			if (not found):
				temp=self.head
				while (temp.bottom!=None): #find for a node where next one is free for enter
					temp=temp.bottom
				temp.bottom=new 	#Add the created new node to the free space
				self.count+=1
			else:
				print("The Entered Vertex is already exist in the graph")

	#Add a New Edge
	def addedge(self,fromm,to):
		vfound=True
		efound=True
		cfound=False
		if (self.head==None):
			print("The Graph is Empty! Enter some Nodes") #If there exist no vertex in the graph show this error
		else:
			temp=self.head
			while (temp.data!=fromm):
				temp=temp.bottom
				if (temp==None):
					print("The vertex was not found in the graph") #If Entered vertex is not found display this
					vfound=False
					break
			etemp=self.head
			while (etemp.data!=to):
				etemp=etemp.bottom
				if (etemp==None):
					print("Can't Establish a connection with target node! Try Again")
					efound=False
					break

			if (vfound and efound):
				edge=edgenode(to)
				if (temp.next==None):
					temp.next=edge
				else:
					tempedge=temp
					while (tempedge.next!=None): #Find the node which next one is empty
						tempedge=tempedge.next
						if (tempedge.data==to):
							cfound=True
					if (not cfound):
						tempedge.next=edge
					else:
						print("The Connection is Already Exist in this Graph")

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
		print("The Number of Indegrees for node ",node," is ",count-1)

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

	def counter(self):
		print("The Number of Vertexes in this Graph is ",self.count+1)

	def deletenode(self,value):
		print()
		print("Searching, Please wait ........")
		time.sleep(1)
		temp=self.head
		if (temp.data==value):
			print()
			print("Hah haaa, I Found it, Deleting......")
			time.sleep(1)
			self.head=temp.bottom
			temp.bottom=None
			print("Done")
			time.sleep(1)

		while (temp!=None):
			edge=temp.next
			while(edge!=None):
				if (edge.next!=None):
					if (edge.next.data==value) and (edge.next.next!=None):
						print()
						print("Connection Found at node",temp.data,", Deleting....")
						time.sleep(1)
						edge.next=edge.next.next
						print("Done")
						time.sleep(1)
					elif (edge.next.data==value) and (edge.next.next==None):
						print()
						print("Connection Found at node",temp.data,", Deleting....")
						time.sleep(1)
						edge.next=None
						print("Done")
						time.sleep(1)
				else:
					if edge.data==value:
						print()
						print("Connection Found at node",temp.data,", Deleting....")
						time.sleep(1)
						temp.next=None
						print("Done")
						time.sleep(1)

				edge=edge.next
			if (temp.bottom.data==value) and (temp.bottom!=None):
				print()
				print("Hah haaa, I Found it, Deleting......")
				temp.bottom=temp.bottom.bottom
				time.sleep(1)
				print("Done")
				time.sleep(1)
			temp=temp.bottom


#End of the Class graph

def addvertlooper():
	d=input("Enter vertex: ")
	a.addvert(d)
	print()
	ans=input("Do you want to input another vertex?(Y/N) ")
	if (ans.upper()=="Y"):
		addvertlooper()
	elif (ans.upper()=="N"):
		menu()
	else:
		print("Invalied Input Try Again!")
		menu()

def addedgelooper():
	d=input("Enter Vertex From: ")
	e=input("Enter Vertex To: ")
	a.addedge(d,e)
	print()
	ans=input("Do you want to input another edge?(Y/N) ")
	if (ans.upper()=="Y"):
		addedgelooper()
	elif (ans.upper()=="N"):
		menu()
	else:
		print("Invalied Input Try Again!")
		menu()

def reset():
	global a
	a=graph()

def deleteme():
	j=input("Enter the Node you want to delete: ")
	a.deletenode(j)

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
	print()
	print("Select the Command and enter the number of the Command")
	print()
	print("//////////////////////////////////////////////////////////////////////////////////////////////")
	print("// 1.Enter new Vertex \t 2.Delete Vertex \t 3.Enter new Edge \t 4.number of vertex //")
	print("// 5.Indegree \t \t 6.Outdegree \t \t 7.Print Linked List \t 8.Exit \t    //")
	print("//////////////////////////////////////////////////////////////////////////////////////////////")
	x=int(input("Enter the Command Number: "))

	if (x==2):
		deleteme()
		menu()
	elif (x==1):
		addvertlooper()
		menu()
	elif (x==3):
		addedgelooper()
		menu()
	elif (x==4):
		a.counter()
		menu()
	elif (x==5):
		y=input("Enter the Node you want to find the Number of indegrees: ")
		a.indegree(y)
		menu()
	elif (x==6):
		y=input("Enter the Node you want to find the Number of outdegrees: ")
		a.outdegree(y)
		menu()
	elif (x==7):
		a.printme()
		menu()
	elif (x==8):
		print("Thanks for using this Programme! Bye!")
		exit()
	else:
		print("The Input is Not valied! Please try again.")
		menu()

def start():
	interface()
	menu()

a=graph()
start()