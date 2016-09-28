# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:08:30 2016
@company: ACM@UIUC SIGSPATIAL
@author: Derek Chen and Anselmo Shim
"""
# import libraries
import numpy as np
import random
import matplotlib.pyplot as plt

# close to clear any previously opened plots
plt.close('all')


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, vx, vy, dt):
        self.x = self.x + vx*dt
        
class Landmark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def rangescan(robot, landmark):
    # distance formula
    return ((robot.x-landmark.x)**2 + (robot.y-landmark.y)**2)**(.5)

Alice = Robot(1,1)
ECEB = Landmark(1,1)
Siebel = Landmark(2,2)
Landmarks = [ECEB, Siebel]

# Alice is at ECEB, so it should show 0.0
print rangescan(Alice, ECEB)
# Distance from Alice and Siebel
print rangescan(Alice, Siebel)

# moving the robot part
x_list = [];
y_list = [];

for i in range(1,10):
    Alice.move(1,1,.1)
    x_list.append(Alice.x)
    y_list.append(Alice.x)
    
plt.plot(x_list,y_list,'o')

l_list = [];
new_list = [];

# final part
for i in range(0,5):
    # generate five random landmarks and put them into l_list
    l_list.append(Landmark(20*random.random(),20*random.random()))
    # plot the five randomly generated landmarks from l_list
    plt.plot(l_list[i].x,l_list[i].y,'v', ms = 10)
    # find distance between Alice and landmark, put them into new_list
    new_list.append(rangescan(Alice, l_list[i]))
    # put names of buildings into a list
    name_list = ['DCL', 'ECEB', 'Siebel', 'Grainger', 'CSL']
    # combined list of names and list of landmark distances
    zipped_list = zip(name_list, new_list)
    
# sort by distance
zipped_list.sort(key=lambda tup: tup[1])  # sorts in place
# print
print zipped_list
