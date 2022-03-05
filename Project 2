# Importing the libraries
import cv2, math
import numpy as np

# Defining the maze
maze = np.zeros((250,400,3))
maze[:, :] = (0, 0, 0)

# Variables
c1 = 1.0
c2 = 1.4
nn = []

# Plotting the obstacles in the maze
# Drawing shapes

clearence_point = np.array([[25,63],[125,32],[87,75],[110,160]],dtype=np.int32)
polygon2 = cv2.fillPoly(maze, [clearence_point], [1,1,1],1)

pts = np.array([[36,65],[115,40],[80,70],[105,150]],dtype=np.int32)
polygon = cv2.fillPoly(maze, [pts], [255,0,0])

# Drawing image 2
circle2 = cv2.circle(maze, (300,64), 45, [1,1,1],-1)
circle = cv2.circle(maze, (300,64), 40, [255,0,0],-1)

# Drawing image 3
clearence_point2 = np.array([[200,110],[240,132.5],[240,167.5],[200,190],[160,167.5],[160,132.5]],dtype=np.int32)
hexagon2 = cv2.fillPoly(maze,[clearence_point2] , [1,1,1])
pts2 = np.array([[200,115],[235,132.5],[235,167.5],[200,185],[165,167.5],[165,132.5]],dtype=np.int32)
hexagon = cv2.fillPoly(maze, [pts2], [255,0,0])

obstacle_space1 = np.argwhere(circle2)
obstacle_space2 = np.argwhere(polygon2)
obstacle_space3 = np.argwhere(hexagon2)

def obstacle_space(x):
    c=0
    for i in obstacle_space1 :
        if i[0] == x[0] and i[1] == x[1] :
            c = 1
    for i in obstacle_space2 :
            if i[0] == x[0] and i[1] == x[1] :
                c = 1
    for i in obstacle_space3 :
            if i[0] == x[0] and i[1] == x[1] :
                c = 1
    return c

# Start and end point
print('Enter the start position...')
xs = int(input("Enter your value of X-Axis: "))
ys = int(input("Enter your value of Y-Axis: "))
print('Enter the goal position...')
xg = int(input("Enter your value of X-Axis: "))
yg = int(input("Enter your value of Y-Axis: "))

initial_coordinate = [xs,ys]
final_coordinate = [xg,yg]
 
# possible points for movenment
all_points = []
for i in range(0, 250):
  for j in range(0, 400):
      d = math.sqrt(((i, j)[0] - initial_coordinate[0]) * ((i, j)[0] - initial_coordinate[0]) + ((i, j)[1] - initial_coordinate[1]) * ((i, j)[1] - initial_coordinate[1]))
      if d <=1 :
          all_points.append((i, j))
                   
# Functions for movements    
def up(cc):
    i,j=cc[0], cc[1]
    if i > 0 and i <= 249:
        x = i-1
        y = j
        new_c = (x,y)
        return new_c
    
def down(cc):
    i,j=cc[0], cc[1]
    if i >= 0 and i < 249:
        x = i+1
        y = j
        new_c = (x, y)
        return new_c
    
def left(cc):
    i,j=cc[0], cc[1]
    if j > 0 and j <= 399:
        x = i
        y = j-1
        new_c = (x, y)
        return new_c
    
def right(cc):
    i,j=cc[0], cc[1]
    if j >= 0 and j < 399:
        x= i
        y= j+1
        new_c = (x,y)
        return new_c
    
def up_left(cc):
    i,j=cc[0], cc[1]
    if i > 0 and i <=249 and j > 0 and j <=399:
        x= i-1
        y= j-1
        new_c = (x,y)
        return new_c
    
def up_right(cc):
    i,j=cc[0], cc[1]
    if i > 0 and i <=249 and j >= 0 and j < 399:
        x= i-1
        y= j+1
        new_c = (x,y)
        return new_c
    
def down_left(cc):
    i,j=cc[0], cc[1]
    if i >= 0 and i < 299 and  j > 0 and j <= 399:
        x= i+1
        y= j-1
        new_c = (x,y)
        return new_c
    
def down_right(cc):
    i,j=cc[0], cc[1]
    if i >= 0 and i < 249 and j >= 0 and j < 399 :        
        x= i+1
        y= j+1
        new_c = (x,y)
        return new_c
    


# main function 
class Node():
    def __init__(self, coordinate):
        self.config = coordinate
        self.root = None
        
nn = []
def main_function(start_coordinate):
    sn = Node(start_coordinate)
    open_nodes = {(start_coordinate[0], start_coordinate[1]) : 0.0}
    close_nodes = set()
    gn = {(start_coordinate[0], start_coordinate[1]) : sn}




    while len(open_nodes) > 0:
        cn = list(open_nodes.keys())[0]
        cc = list(open_nodes.values())[0]
        del open_nodes[cn]
        close_nodes.add(cn)
        
        if cn[0] == final_coordinate[0] and cn[1] == final_coordinate[1]:
            return gn[cn]

# Possible Movenment
        
        def up_move(node_value):
            if nn != None and nn not in close_nodes:
                if nn not in open_nodes:
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c1
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:                      
                    if cc + c1 < open_nodes[nn]:
                        open_nodes[nn] = cc + c1
                        
                        
        def down_move(node_value):
            if nn != None and nn not in close_nodes:
                
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c1
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c1 < open_nodes[nn]:
                        open_nodes[nn] = cc + c1
                       
         
        def right_move(node_value):
            
            if nn != None and nn not in close_nodes:
                
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c1
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c1 < open_nodes[nn]:
                        open_nodes[nn] = cc + c1
                        
                        
        def left_move(node_value) :
            if nn != None and nn not in close_nodes:
                
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c1
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c1 < open_nodes[nn]:
                        open_nodes[nn] = cc + c1
                        
                        
        def upright_move(node_value):
            if nn != None and nn not in close_nodes:
                
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c2
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c2 < open_nodes[nn]:
                        open_nodes[nn] = cc + c2
                        
                        
        def downright_move(node_value):
         if nn != None and nn not in close_nodes:
            
                if obstacle_space(cn)!=1:# first time
                 gn[nn] = Node(nn)
                 open_nodes[nn] = cc + c2
                 close_nodes.add(nn)
                 gn[nn].root = gn[cn]
                 maze[nn[0]][nn[1]] = [0,255,0]
                 cv2.imshow('Image', maze)
                 cv2.waitKey(1)
         elif nn in open_nodes:
                if cc + c2 < open_nodes[nn]:
                    open_nodes[nn] = cc + c2
                    
                    
        def upleft_move(node_value):
            if nn != None and nn not in close_nodes:
                
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c2
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c2 < open_nodes[nn]:
                        open_nodes[nn] = cc + c2
                       
                        
        def downleft_move(node_value):
            if nn != None and nn not in close_nodes:
               
                    if obstacle_space(cn)!=1:
                     gn[nn] = Node(nn)
                     open_nodes[nn] = cc + c2
                     close_nodes.add(nn)
                     gn[nn].root = gn[cn]
                     maze[nn[0]][nn[1]] = [0,255,0]
                     cv2.imshow('Image', maze)
                     cv2.waitKey(1)
            elif nn in open_nodes:
                    if cc + c2 < open_nodes[nn]:
                        open_nodes[nn] = cc + c2
                        
                         
        nn = up(cn)
        up_move(nn)

                    
        
        nn = down(cn)
        down_move(nn)

        nn = right(cn)
        right_move(nn)
                    
        
        nn = left(cn)
        left_move(nn)
        
                    
        
        nn = up_right(cn)
        upright_move(nn)
        
        nn = down_right(cn)
        downright_move(nn)
                    
        
        nn = up_left(cn)
        upleft_move(nn)
        
        nn = down_left(cn)
        downleft_move(nn)
         
         
        
        open_nodes = dict(sorted(open_nodes.items(), key = lambda item: item[1]))
   

# checking possiblities of start and initial psoitions
if obstacle_space(initial_coordinate) == True or obstacle_space(final_coordinate) == True:
    print("Try again: The robot location is not possible")
else:    
    goal = main_function(initial_coordinate)


# Backtrack
while goal.config!= initial_coordinate:
        maze[goal.config[0]][goal.config[1]] = 0
        goal = goal.root

# Display the final result        
cv2.imshow('Image', maze) 
cv2.waitKey(0)
cv2.destroyAllWindows()

