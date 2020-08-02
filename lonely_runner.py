# Standard data science libraries
import pandas as pd
import numpy as np
import math
import random
import pygame
k_runners=5
cc=0
        
runners=[]
sim_step=0.0001
size=400

### Initializing ###
pygame.init()
w_h = [size,size]
screen = pygame.display.set_mode(w_h)
pygame.display.set_caption("LONELY RUNNER")
stop = False
animationTimer = pygame.time.Clock()





class runner():
    def __init__(self, pos,speed):    
        self.pos = pos
        self.speed = speed
        self.lonely = 0
        self.color= (255,255,255)
        self.size=5
        self.distances = [0]*k_runners
        
    def check_lonely(self): 
        for k in range(0,k_runners):
            self.distances[k]=abs(self.pos-runners[k].pos)    
        if sorted(self.distances)[1]>(2*np.pi/k_runners) and sorted(self.distances)[2]>(2*np.pi/k_runners):
            self.lonely=1

                
    def display(self):
        displx=int(np.round(size/2)+np.round(size/4)*(math.cos(self.pos)))
        disply=int(np.round(size/2)+np.round(size/4)*(-(math.sin(self.pos))))
        pygame.draw.circle(screen, self.color , [displx,disply], self.size)
            

## Create runners ###
speed_list = list(range(1,k_runners*20))
random.shuffle(speed_list)
for k in range(0,k_runners):
    runners.append(runner(0,speed_list[k]))
    print(runners[k].speed)

        
#### Loop ####
while stop == False: # check for exit
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            stop = True # Flag that we are done so we exit this loop
            
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,255), [int(np.round(size/2)),int(np.round(size/2))], int(np.round(size/4)),1)
    
    for k in range(0,k_runners):     
        runners[k].pos += runners[k].speed*sim_step
    for k in range(0,k_runners):        
        runners[k].check_lonely()
        if runners[k].lonely==1:
           runners[k].color=(255,0,0)       
        runners[k].display()
        
    animationTimer.tick(600)
    pygame.display.update()      
  
    
pygame.quit()        