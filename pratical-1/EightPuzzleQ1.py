# -*- coding: utf-8 -*-
"""
1. Add the simpleHillClimbing method to the Puzzle class in the code cell. 
This method will implement the simple hill climbing algorithm to find a path to the goal state.

2. Call this new method to test its implementation in main file.
"""
##-----------------------------------------------------------------------------
##setting up the puzzle
##----------------------------------------------------------------------------- 
class Puzzle:
    def __init__(self):
        self.StartNode=['1','2','3','5','6','8','4','0','7'] #default, h(n) = 8
        self.GoalNode=['1','2','3','4','5','6','7','8','0'] #default, h(n) = 0
        self.PreviousNode=[] #to store the expanded nodes
        self.Fringe=[] #to store the leaf nodes
        self.Parent = []#to store the child-parent pairs

    def shuffler(self):
        print ("test")
        while True:
            node=self.StartNode
            subNode=[]
            direct=random.randint(1,4) #generate a random number between 1 and 4
            getZeroLocation=node.index('0')+1   # index of "0"
            subNode.extend(node)
            boundary=self.boundaries(getZeroLocation)

            #if the empty tile is at the top 2 rows, move the tile down
            if getZeroLocation+3<=9 and direct==1:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')+3]
                subNode[node.index('0')+3]=temp
                self.StartNode=subNode
                return

            #if the empty tile is at the bottom 2 rows, move the tile up
            elif getZeroLocation-3>=1 and direct==2:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')-3]
                subNode[node.index('0')-3]=temp
                self.StartNode=subNode
                return

            #if the empty tile is at the last 2 columns, move the tile left
            elif getZeroLocation-1>=boundary[0] and direct==3:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')-1]
                subNode[node.index('0')-1]=temp
                self.StartNode=subNode
                return

            #if the empty tile is at the first 2 columns, move the tile right
            elif getZeroLocation+1<=boundary[1] and direct==4:
                temp=subNode[node.index('0')]
                subNode[node.index('0')]=subNode[node.index('0')+1]
                subNode[node.index('0')+1]=temp
                self.StartNode=subNode
                return

    def boundaries(self, zero_location):
        if zero_location in [1, 2, 3]:
            return (1, 3)
        elif zero_location in [4, 5, 6]:
            return (4, 6)
        elif zero_location in [7, 8, 9]:
            return (7, 9)

    def successor(self,node=[], search_type=None): #node is [] by default
        subNode=[]
        p = []
        c = []

        getZeroLocation=node.index('0') + 1 #get the location of the empty tile
        subNode.extend(node) #to join node list to the subNode
        boundary=self.boundaries(getZeroLocation)
        p.extend(subNode)

        if search_type != 'bfs':
            self.Fringe=[] #comment this line will turns this search to best first search
        #now generate the successor states
        if getZeroLocation + 3 <= 9: #if the empty tile is at the top 2 rows
            #move the empty tile DOWN
            c = []
            temp=subNode[node.index('0')]
            #swap the location of 2 tiles
            subNode[node.index('0')]=subNode[node.index('0')+3]
            subNode[node.index('0')+3]=temp
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            subNode=[]
            subNode.extend(node)
            cp = (tuple(c[:-1]), tuple(p))
            if(cp not in self.Parent):
                self.Parent.append(cp) #store the child-parent pair to self.Parent


        if getZeroLocation-3>=1: #if the empty tile is at the bottom 2 rows
            #move the empty tile UP
            c = []
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-3]
            subNode[node.index('0')-3]=temp
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            subNode=[]
            subNode.extend(node)
            cp = (tuple(c[:-1]), tuple(p))
            if(cp not in self.Parent):
                self.Parent.append(cp)

        if getZeroLocation-1>=boundary[0]: #if the empty tile is at the last 2 columns
            #move the empty tile LEFT
            c = []
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')-1]
            subNode[node.index('0')-1]=temp
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            subNode=[]
            subNode.extend(node)
            cp = (tuple(c[:-1]), tuple(p))
            if(cp not in self.Parent):
                self.Parent.append(cp)

        if getZeroLocation+1<=boundary[1]: #if the empty tile is at the first 2 columns
            #move the empty tile RIGHT
            c = []
            temp=subNode[node.index('0')]
            subNode[node.index('0')]=subNode[node.index('0')+1]
            subNode[node.index('0')+1]=temp
            c.extend(self.heuristic(subNode))
            self.Fringe.append(c)
            subNode=[]
            subNode.extend(node)
            cp = (tuple(c[:-1]), tuple(p))
            if(cp not in self.Parent):
                self.Parent.append(cp)

    def heuristic(self,node):
        misplacedTile=0

        for i in range(9): #check all 9 tiles (including the ‘0’)
            if node[i]!=self.GoalNode[i]: #compare the tile on Current and Goal Node
                misplacedTile +=1 #if the tile is misplaced, add one; else remained
        node_with_cost = list(node)
        node_with_cost.append(misplacedTile) #append the cost to the last place of node
        return node_with_cost

    def steepestAscentHillClimbing(self):
        #make the initial state as current state
        currentNode = self.heuristic(self.StartNode)
        goalNode = self.heuristic(self.GoalNode) #append goal node heuristic cost

        level = 0
        print("STEEPEST ASCENT HILL CLIMBING")
        print("____________________________________________________________\n")

        while currentNode[:-1] != goalNode[:-1]:
            print("---------\nLEVEL ", level, "\n---------")
            print("        CURRENT NODE: ", currentNode)
            self.successor(currentNode)
            print("        OPEN LIST: ", self.Fringe)

            nxNode = self.SAHC(currentNode[-1])

            if nxNode != [] and nxNode != currentNode:
                currentNode = nxNode
                print("selected: ", currentNode)
                level += 1
            else:
                print("there is no better move")
                break

        print("\n ------------------------------------------------------------")
        print("Initial State: ", self.heuristic(self.StartNode))
        print("Goal State: ", goalNode)

        if currentNode[:-1] == goalNode[:-1]:
            print("GOAL REACHED!")
        else:
            print("LOCAL MAXIMUM: There is no solution")

    def SAHC(self, hrCost):
        nxNode=[] #next node
        while True:
            for i in self.Fringe: #for each open node in the fringe list
                if(i[-1]<hrCost): #if the cost is better than the previous node
                    hrCost=i[-1] #update heuristic cost
                    nxNode=i #set the best node (without heuristic cost)

            #if the temporary node is already in the PreviousNode list
            if nxNode in self.PreviousNode and nxNode in self.Fringe:
                self.Fringe.remove(nxNode) #remove the temporary node

            #else if it is not in the PreviousNode list
            elif nxNode != []:
                self.PreviousNode.append(nxNode) #append nxNode to PreviousNode
                return nxNode #return the next node
            else:
                return nxNode

    def bestFirstSolve(self):
        currentNode = self.heuristic(self.StartNode)
        goalNode = self.heuristic(self.GoalNode)
        print("GREEDY BEST FIRST SEARCH")
        print("____________________________________________________________\n")
        step = 0

        while currentNode[:-1] != goalNode[:-1]:
            print("---------\nSTEP: ", step, "\n---------")
            print("        Current Node: ", currentNode)
            self.successor(currentNode,'bfs') # to generate next successor states
            print("        Open List: ", self.Fringe)
            nxNode=self.bestFirstSearch()

            if nxNode!=[] and nxNode!=goalNode and nxNode!=currentNode: #Goal test
                currentNode = nxNode
                step += 1
            else:
                break

        print("\n ------------------------------------------------------------")
        print("Initial State: ", self.heuristic(self.StartNode))
        print("Goal State: ", goalNode)

        if currentNode[:-1] == goalNode[:-1]:
            print("GOAL REACHED!")
        else:
            print("NO SOLUTION FOUND or LOCAL MAXIMUM REACHED")

    def bestFirstSearch(self):
        nxNode=[] #next node
        while True:
            hrCost=100000 #default value of heuristic cost

            for i in self.Fringe: #for each open node in the fringe list
                if(i[-1]<hrCost): #the heuristic cost is the last member
                    hrCost=i[-1] #update heuristic cost
                    nxNode=i #set the best node to temporary node

            #if the temporary node is already in the PreviousNode list
            if nxNode in self.PreviousNode and nxNode in self.Fringe:
                self.Fringe.remove(nxNode) #remove the node from the open list

            #else if it is not in the PreviousNode list
            elif nxNode != []:
                self.PreviousNode.append(nxNode) #add the node to PreviousNode list
                return nxNode #return the next node
            else:
                return nxNode


    def simpleHillClimbing(self):
        currentNode = self.heuristic(self.StartNode)
        goalNode = self.heuristic(self.GoalNode)
        level = 0
        path = [currentNode]
        print("SIMPLE HILL CLIMBING")
        print("____________________________________________________________\n")

        while currentNode[:-1] != goalNode[:-1]:
            print("---------\nLEVEL ", level, "\n---------")
            print("        CURRENT NODE: ", currentNode)
            self.successor(currentNode)
            print("        OPEN LIST: ", self.Fringe)

            best_successor = None
            min_heuristic = float('inf')

            for successor_node in self.Fringe:
                if successor_node[-1] < min_heuristic and successor_node not in self.PreviousNode:
                    min_heuristic = successor_node[-1]
                    best_successor = successor_node

            if best_successor and best_successor[-1] < currentNode[-1]:
                currentNode = best_successor
                path.append(currentNode)
                self.PreviousNode.append(currentNode)
                print("selected: ", currentNode)
                level += 1
                self.Fringe = [] # Clear fringe for simple hill climbing
            else:
                print("there is no better move or already visited")
                break

        print("\n ------------------------------------------------------------")
        print("Initial State: ", self.heuristic(self.StartNode))
        print("Goal State: ", goalNode)
        print("Path: ", path)

        if currentNode[:-1] == goalNode[:-1]:
            print("GOAL REACHED!")
        else:
            print("LOCAL MAXIMUM: There is no solution")
