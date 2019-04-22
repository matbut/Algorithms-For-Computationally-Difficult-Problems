# APTO Mateusz Buta 2019
# Recursion solution for the VertexCover problem


from itertools import combinations, count
from dimacs import *
from sys import argv
from kernel import *
from copy import deepcopy

def find(G,C,k):
  V = len(G)
  E = edgeList(G)

  if k==0 or E == []:
    if isVC(E,C):
      return C
    return None

  for v in list(E[0]):
    C.add(v)
    N = []            
    for w in G[v].copy(): 
      N += [(w,v)] 
      G[w].remove(v)   
      G[v].remove(w)   

    sol = find(G,C,k-1)
    if sol != None:
      return sol

    for (w,v) in N:
      G[w].add(v)
      G[v].add(w)
    C.remove(v)

  return None

def solve(Old):
  V = len(Old)
  E = edgeList(Old)
  for k in count():
    G = deepcopy(Old)
    G,C,k = compress(G,k)

    if k<0 or rejectCompress(G,k):
      continue

    sol = find(G,set(),k)
    if sol!=None:
      return C.union(sol)

name = argv[1]
G = loadGraph(name)
sol = solve(G)
saveSolution(name + '.sol', sol)