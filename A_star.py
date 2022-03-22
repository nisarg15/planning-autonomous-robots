# Importing the libraries
import cv2, math
import numpy as np

# Defining the maze
maze = np.zeros((250,400,3))
maze[:, :] = (0, 0, 0)

# Variables
val = []

# Plotting the obstacles in the maze
# Drawing shapes

pts = np.array([[36,65],[115,40],[80,70],[105,150]],dtype=np.int32)
polygon = cv2.fillPoly(maze, [pts], [255,0,0])

# Drawing image 2
circle = cv2.circle(maze, (300,64), 40, [255,0,0],-1)

# Drawing image 3
pts2 = np.array([[200,115],[235,132.5],[235,167.5],[200,185],[165,167.5],[165,132.5]],dtype=np.int32)
hexagon = cv2.fillPoly(maze, [pts2], [255,0,0])
 
# Defining the obstacle space 
obstacle_space1 = np.argwhere(maze[:,:,0] == 255)
obstacle_space1 = np.flip(obstacle_space1)



# Getting the values from the users
print('Enter the start position...')
xs = int(input("Enter your value of X-Axis: "))
ys = int(input("Enter your value of Y-Axis: "))
print('Enter the goal position...')
xg = int(input("Enter your value of X-Axis: "))
yg = int(input("Enter your value of Y-Axis: "))
step = int(input("enter the step size "))

initial_coordinate = [xs,ys]
final_coordinate = [xg,yg]
final_goal = cv2.circle(maze, (xg,yg), 3, [1,1,1],-1)
step_size = step


goal_space1 = np.argwhere(final_goal[:,:,0] == 1)
goal_space1 = np.flip(goal_space1)

def obstacle_space(x):
    c = 0
    for i in obstacle_space1 :
        if i[0] == x[0] and i[1] == x[1] :
            c = 1
            
            if c == 1:
              break
    return c



def goal_space(x):
    c = 0
    for i in goal_space1 :
        if i[0] == x[0] and i[1] == x[1] :
            c = 1
            
            if c == 1:
              break
    return c
# possible Movenments
def m_0(cc,step_size):
    i,j=cc[0], cc[1]
    if j > 0 and j <=249 and i > 0 and i <=399:
     
     x = int(i + step_size*math.sin(math.radians(90)))
     y = int(j + step_size*math.cos(math.radians(90)))
     new_c = (x,y)

     return (new_c)


def m_30 (cc, step_size):
    i,j=cc[0], cc[1]
    if j > 0 and j <=249 and i > 0 and i <=399:
 
     x =  int(i + step_size*math.sin(math.radians(30)))
     y =  int(j + step_size*math.cos(math.radians(30))) 
     new_c = (x,y)

     return new_c


def m_60 (cc, step_size ):
    i,j=cc[0], cc[1]
    if j > 0 and j <=249 and i > 0 and i <=399:
 
     x = int(i + step_size*math.sin(math.radians(60)))
     y = int(j + step_size*math.cos(math.radians(60)))
     new_c = (x,y)
     return new_c   
 
def m_n_30 (cc, step_size ):
    i,j=cc[0], cc[1]
    if j > 0 and j <=249 and i > 0 and i <=399:
    
     x = int(i + step_size*math.cos(math.radians(330)))
     y  = int(((j + step_size*math.sin(math.radians(330)))))
     new_c = (x,y)
     return new_c

def m_n_60 (cc, step_size ):
    i,j=cc[0], cc[1]
    if j > 0 and j <=249 and i > 0 and i <=399:
    
     x = int(i + step_size*math.cos(math.radians(300)))
     y  = int(((j + step_size*math.sin(math.radians(300)))))
     new_c = (x,y)
     return new_c

# main function 
def main_function(start_coordinate):
 i = 0
 while i < 5 : 
  
   open_nodes = {(start_coordinate[0], start_coordinate[1]) : 0}
   open_nodes_cost = {(start_coordinate[0], start_coordinate[1]) : 0}
   close_nodes = set()
   currentNode = list(open_nodes_cost.keys())[0]
   currentCost = list(open_nodes_cost.values())[0]
   heuristicCost = list(open_nodes.values())[0]




   while len(open_nodes_cost) > 0:
        currentNode = list(open_nodes_cost.keys())[0]

        currentCost = list(open_nodes_cost.values())[0]

        del open_nodes_cost[currentNode]
        close_nodes.add(currentNode)
        

          
# Possible Movenment       
        nextNode = m_0(currentNode,step_size)
        if nextNode != None and nextNode not in close_nodes:
         if nextNode not in open_nodes_cost:
             if obstacle_space(nextNode)!=1:
              if nextNode[1] > 0 and nextNode[1] <=249 and nextNode[0] > 0 and nextNode[0] <=399:

               open_nodes[nextNode] = currentCost + step_size

               dis1 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1])))) 
               open_nodes_cost[nextNode] = heuristicCost + dis1
               cv2.arrowedLine(maze, currentNode, nextNode,
                                  (0, 0, 255), 1, tipLength = 0.2)
               cv2.imshow('Image', maze)
               cv2.waitKey(1)
       
        elif nextNode in open_nodes_cost:
                  if currentCost + step_size < open_nodes[nextNode]:
                      open_nodes[nextNode] = currentCost + step_size
                      dis1 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                      open_nodes_cost[nextNode] = heuristicCost + dis1
                    
        if goal_space(currentNode) == 1:
            break
            
            
        nextNode = m_30(currentNode,step_size)

        if nextNode != None and nextNode not in close_nodes:
         if nextNode not in open_nodes_cost:
             if obstacle_space(nextNode)!=1:
              if nextNode[1] > 0 and nextNode[1] <=249 and nextNode[0] > 0 and nextNode[0] <=399: 

                open_nodes[nextNode] = currentCost + step_size
                dis2 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                open_nodes_cost[nextNode] = heuristicCost + dis2
                cv2.arrowedLine(maze, currentNode, nextNode,
                                  (0, 0, 255), 1, tipLength = 0.2)
                cv2.imshow('Image', maze)
                cv2.waitKey(1)
      
        elif nextNode in open_nodes_cost:
                  if currentCost + step_size < open_nodes[nextNode]:
                      open_nodes[nextNode] = currentCost + step_size
                      dis2 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                      open_nodes_cost[nextNode] = heuristicCost + dis2
        if goal_space(currentNode) == 1:
            break
        nextNode = m_60(currentNode,step_size)
        if nextNode != None and nextNode not in close_nodes:
         if nextNode not in open_nodes_cost:
             if obstacle_space(nextNode)!=1:
              if nextNode[1] > 0 and nextNode[1] <=249 and nextNode[0] > 0 and nextNode[0] <=399:

                open_nodes[nextNode] = currentCost + step_size
                dis3 =int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                open_nodes_cost[nextNode] = heuristicCost + dis3
                cv2.arrowedLine(maze, currentNode, nextNode,
                                  (0, 0, 255), 1, tipLength = 0.2)
                cv2.imshow('Image', maze)
                cv2.waitKey(1)
       
        elif nextNode in open_nodes_cost:
                  if currentCost + step_size < open_nodes[nextNode]:
                      open_nodes[nextNode] = currentCost + step_size
                      dis3 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                      open_nodes_cost[nextNode] = heuristicCost + dis3
                                                
        if goal_space(currentNode) == 1:
            break
        nextNode = m_n_30(currentNode,step_size)
        if nextNode != None and nextNode not in close_nodes:
         if nextNode not in open_nodes_cost:
             if obstacle_space(nextNode)!=1:
              if nextNode[1] > 0 and nextNode[1] <=249 and nextNode[0] > 0 and nextNode[0] <=399:


               open_nodes[nextNode] = currentCost + step_size
               dis4 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
               open_nodes_cost[nextNode] = heuristicCost + dis4
               cv2.arrowedLine(maze, currentNode, nextNode,
                                  (0, 0, 255), 1, tipLength = 0.2)
               cv2.imshow('Image', maze)
               cv2.waitKey(1)
       
        elif nextNode in open_nodes_cost:
                  if currentCost + step_size < open_nodes[nextNode]:
                      open_nodes[nextNode] = currentCost + step_size
                      dis4 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                      open_nodes_cost[nextNode] = heuristicCost + dis4
        if goal_space(currentNode) == 1:
            break
        nextNode = m_n_60(currentNode,step_size)

        if nextNode != None and nextNode not in close_nodes:
         if nextNode not in open_nodes_cost:
             if obstacle_space(nextNode)!=1:
              if nextNode[1] > 0 and nextNode[1] <=249 and nextNode[0] > 0 and nextNode[0] <=399:

               open_nodes[nextNode] = currentCost + step_size

               dis5 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
               open_nodes_cost[nextNode] = heuristicCost + dis5

               cv2.arrowedLine(maze, currentNode, nextNode,
                                  (0, 0, 255), 1, tipLength = 0.2)
               cv2.imshow('Image', maze)
               cv2.waitKey(1)
       
        elif nextNode in open_nodes_cost:
                  if currentCost + step_size < open_nodes[nextNode]:
                      open_nodes[nextNode] = currentCost + step_size
                      dis5 = int((math.sqrt(((nextNode)[0] - final_coordinate[0]) * ((nextNode)[0] - final_coordinate[0]) + ((nextNode)[1] - final_coordinate[1]) * ((nextNode)[1] - final_coordinate[1]))))
                      open_nodes_cost[nextNode] = heuristicCost + dis5
            
        if goal_space(currentNode) == 1:
            break
        
# Backtracking
        open_nodes_cost = {k:v for k,v in sorted(open_nodes_cost.items(),key = lambda v : v[1])}
        res = list(open_nodes_cost.keys())[0]
        
 
        val.append(res)

   for i in val:
       cv2.circle(maze, i, 2, [0,255,0],-1)
       

   
   return None
   

      
# checking possiblities of start and initial psoitions                                             
if obstacle_space(initial_coordinate) == True or obstacle_space(final_coordinate) == True:
    print("Try again: The robot location is not possible")
else:    
    goal = main_function(initial_coordinate)

# Display the final result 
cv2.imshow('Image', maze)
cv2.waitKey(0)
cv2.destroyAllWindows()
