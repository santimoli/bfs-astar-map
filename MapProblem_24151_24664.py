from copy import deepcopy
from libskmaps import *
import math
from collections import deque

class MapProblem:

    def __init__(self,file):
       
        self.Map = readSkMap(file)
        self.PosPlayer = tuple(foundPlayerSkMap(self.Map))
        self.goal = tuple(foundGoalSkMap(self.Map))
        self.moves = [
            ((-1, 0), "up"),
            ((1, 0), "down"),
            ((0, -1), "left"),
            ((0, 1), "right")
        ]

    def isFinal(self):
      return self.PosPlayer == self.goal or self.Map[self.PosPlayer[0]][self.PosPlayer[1]] == '+'
   
    def succ(self):
        successors = []

        for move, action in self.moves:
            newl = self.PosPlayer[0] + move[0]
            newc = self.PosPlayer[1] + move[1]

            if 0 <= newl < len(self.Map) and 0 <= newc < len(self.Map[0]):
                if self.Map[newl][newc] != "#":
                    new_state=deepcopy(self)
                    new_state.PosPlayer=(newl,newc)
                    successors.append((new_state, action, 1))

        return successors
    
    def isEqual(self, Mp):
    
        return self.PosPlayer == Mp.PosPlayer
        
        
    def heuristic(self):
        return abs(self.goal[0]-self.PosPlayer[0]) + abs(self.goal[1]-self.PosPlayer[1]) 
    
    
    def __str__(self): ##PARA FINS DE DEBUG
        map = ""
        for i, line in enumerate(self.Map):
            l = ""
            for j, celula in enumerate(line):
                if (i, j) == self.PosPlayer:
                    l += "@"  
                else:
                    l += celula
            map += l + "\n"
        return map
 
class Heuristic(MapProblem):
    
    def heuristic(self):
        return abs(self.goal[0]-self.PosPlayer[0]) + abs(self.goal[1]-self.PosPlayer[1]) 
    

