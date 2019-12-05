# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:28:39 2019

@author: CESharples
"""

import numpy as np

#Instructions
#Define Ecosystem as MxN Boolean Matrix (False representing dead cell, True Representing Live)
#Function tick(Ecosystem) runs 1 iteration of GOL
#Press enter for next iteration, or type exit and hit enter to stop

Ecosystem = np.array([[False,False,False,False,False],[False,False,True,False,False],[False,False,True,False,False],[False,False,True,False,False],[False,False,False,False,False]],np.bool)#Blinker
#^^^Seed the Ecosystem. Below are some other interesting Ecosystems
#Ecosystem = np.array([[False,False,True,False,False,False,False],[True,False,True,False,False,False,False],[False,True,True,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False],[False,False,False,False,False,False,False]],np.bool)#Glider
#Ecosystem = np.array([[False,False,False,False,False,False],[False,False,False,False,False,False],[False,False,True,True,True,False],[False,True,True,True,False,False],[False,False,False,False,False,False],[False,False,False,False,False,False]],np.bool)#Toad

Neighbors=np.array([[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1],],np.int32)

def tick(Ecosystem):
    NCount=np.zeros(Ecosystem.shape)
    for x in range (Ecosystem.shape[0]):#For X*Y Array...
        for y in range (Ecosystem.shape[1]):
            if (Ecosystem[x][y]==True):
                for n in Neighbors:
                    i=x+n[0]
                    j=y+n[1]
                    if (i>=0 and i<Ecosystem.shape[0] and j>=0 and j<Ecosystem.shape[1]):#For each neighbor not inside the matrix...
                        NCount[i][j]+=1#If alive add 1 to each neighbor count
    
    for x in range (NCount.shape[0]):#For each Neighbor Count
        for y in range (NCount.shape[1]):
            if(Ecosystem[x][y]):#If Cell is alive...
                if(NCount[x][y]<2):
                    Ecosystem[x][y]=False#Underpopulation
                elif (NCount[x][y]>3):
                    Ecosystem[x][y]=False#Overcrowding
                else:
                    Ecosystem[x][y]=True#Survival
            else:
                if(NCount[x][y]==3):
                    Ecosystem[x][y]=True#Reproduction
                #else: stagnation
    print("")
    print(Ecosystem)
    pause=input(">>>")
    if (pause !="exit"):#Handle Exit
        tick(Ecosystem)

print(Ecosystem)
tick(Ecosystem)
