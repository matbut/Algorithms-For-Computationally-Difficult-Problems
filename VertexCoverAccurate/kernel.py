# APTO Mateusz Buta 2019
# Graph compression for the VertexCover problem


def compress(G,k):
  C = set()
  V = len(G)
  changed = True
  while changed:
    changed = False
    for v in range(V):
      if len(G[v])>k:
        C.add(v)
        k-=1        
        changed = True
        for u in G[v].copy():
          G[u].remove(v)
          G[v].remove(u)   
        if k<=0:
          return G,C,k
      else: 
        if len(G[v])==1:
          u = list(G[v])[0]
          C.add(u)
          changed = True
          for w in G[u].copy():
            G[u].remove(w)
            G[w].remove(u)
  return G,C,k

def rejectCompress(G,k):
  edges = 0
  V = len(G)
  for v in range(V):
    edges += len(G[v])
  edges = edges/2
  return edges>k**2