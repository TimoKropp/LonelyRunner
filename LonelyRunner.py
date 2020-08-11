import numpy as np
import math
import random
import pygame


k_runners = 5
sim_step = 0.0001
sim_speed = 600

max_speed = k_runners * 20  # max possible speed for runners

# Define some colors for drawings
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
green = (  0, 255,   0)

size = 400              # window size

# Initializing pygame
pygame.init()
w_h     = [size, size]
Runners = []
circle_color = white
screen  = pygame.display.set_mode(w_h)
stop    = False
animationTimer = pygame.time.Clock()
pygame.display.set_caption("LONELY RUNNER")

class Runner:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed
        self.lonely = False
        self.color = white
        self.size = 5
        self.distances = [0] * k_runners
        
    def checkLonely(self):
        for k in range(0, k_runners):
            # calculate distance to all other runners including self
            self.distances[k] = abs(self.pos - Runners[k].pos)

            # sort list to get closest runners, start at [1] to skip distance to self .
            # a runner is lonely if the two closest runners have a distance > 2 * np.pi / k_runners
            # on a unit circle
        if sorted(self.distances)[1] > (2 * np.pi / k_runners) and sorted(self.distances)[2] > (2 * np.pi / k_runners):
            self.lonely = True

                
    def display(self):
        displx = int(np.round(size/2) + np.round(size/4) * (math.cos(self.pos)))
        disply = int(np.round(size/2) + np.round(size/4) * (-(math.sin(self.pos))))
        pygame.draw.circle(screen, self.color , [displx, disply], self.size)
            

### create runners ###
speed_list = list(range(1, max_speed))          # create speed list with number increasing and distinct values
random.shuffle(speed_list)                      # shuffle list for random value
for k in range(0, k_runners):                   # create Runners with speed value from shuffled list
    Runners.append(Runner(0, speed_list[k]))

### loop ###
while stop == False:                        # check for exit
    for event in pygame.event.get():        # User did something
        if event.type == pygame.QUIT:       # If user clicked close
            stop = True                     # Flag that we are done so we exit this loop

    # draw background and circle track
    screen.fill(black)

    pygame.draw.circle(screen, circle_color, [int(np.round(size / 2)), int(np.round(size / 2))], int(np.round(size / 4)), 1)
    for k in range(0, k_runners):
        # calculate distance to all other runners including self
        Runners[k].pos += Runners[k].speed * sim_step

    for k in range(0, k_runners):
        Runners[k].checkLonely()    # check if a runner is lonely at this time step

        if (Runners[k].lonely):     # draw lonely runners red
           Runners[k].color = red

        Runners[k].display()        # draw all runners
        
    animationTimer.tick(sim_speed)  # increment simulation
    pygame.display.update()         # update animation window
  
    
pygame.quit()