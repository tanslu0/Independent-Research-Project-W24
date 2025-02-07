import random
import math
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

n = 6   #SIZE OF GRAPH (n > 250 takes a long time to process)
games = 10   #NUMBER OF GAMES SIMULATED
baselist = [0]
redWinList = []
redWins = 0
p1 = []
p2 = []

edges = int(math.factorial(n)/(2*math.factorial(n-2)))

def gameSim(blue,red,edges,n,winList):
    x = 0
    num1 = 0
    num2 = 0
    for x in range(0,edges):
        while x == 0 or blue[num1][num2] != 0 or num1 == num2 or red[num1][num2] != 0:
            if x == 0:
                num1 = random.randint(0,n-1)
                num2 = random.randint(0,n-1)
                if num1 != num2:
                    break
            else:
                num1 = random.randint(0,n-1)
                num2 = random.randint(0,n-1)
        if x % 2 == 0: #even, p1 goes
            blue[num1][num2] = 1
            blue[num2][num1] = 1
        else: #odd, p2 goes
            red[num1][num2] = 1
            red[num2][num1] = 1

    npBlue = np.array(blue)
    nxBlue = nx.from_numpy_array(npBlue)
    blueClique = list(nx.find_cliques(nxBlue))
    blueLargest = len(max(blueClique, key=len))
    #nx.draw(nxBlue)
    #plt.show()    #UNCOMMENT TO SEE SOMETHING INTERESTING (with large n)
    npRed = np.array(red)
    nxRed = nx.from_numpy_array(npRed)
    redClique = list(nx.find_cliques(nxRed))
    redLargest = len(max(redClique, key=len))
    if redLargest >= blueLargest:
        winList.append(1)

    """for y in range(0,n):
        print(npBlue[y])      #UNCOMMENT TO VIEW P1 ADJACENCY MATRICES
    print("")"""
    return winList

for z in range(0,games):
    p1 = []
    p2 = []
    baselist = [0]
    for b in range (0,n):
        baselist = [0]
        p1.append(baselist)
        for c in range(0,n-1):
            p1[b].append(0)
    for b in range (0,n):
        baselist = [0]
        p2.append(baselist)
        for c in range(0,n-1):
            p2[b].append(0)
    redWinList = gameSim(p1,p2,edges,n,redWinList)

redWins = len(redWinList)
redProportion = redWins/games
print(redProportion)
