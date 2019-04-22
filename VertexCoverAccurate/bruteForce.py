# APTO Mateusz Buta 2019
# Brute force solution for the VertexCover problem


from itertools import combinations, count
from dimacs import *
from sys import argv
from kernel import *
from copy import deepcopy

def subset(G,k):
  V = len(G)
  E = edgeList(G)
  for C in combinations(range(V),k):
    if isVC(E,C):
      return C
  return None

def solve(Old):
  V = len(Old)
  E = edgeList(Old)
  for k in count():
    G = deepcopy(Old)
    G,C,k = compress(G,k)

    if k<0 or rejectCompress(G,k):
      continue
    else: 
      if k==0 and isVC(E,C): 
        return C

    sol = subset(G,k)
    if sol!=None:
      return C.union(sol)

name = argv[1]
G = loadGraph(name)
sol = solve(G)
saveSolution(name + '.sol', sol)