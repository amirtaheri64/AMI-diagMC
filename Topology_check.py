##################################
##########Import Libraries########
##################################
#Begin
from igraph import *
#End
###################################

###################################
########Diagram modification#######
###################################
#Begin
def mod_iso(G):
  nv=G.vcount()
  l=G.ecount()
  #print 'nv = ', nv
  #print 'l = ', l 
  b_list=[]   
  V1=[]
  V2=[]
  for i in range(0,l):
    if G.es['F_or_B'][i]==0:
      b_list.append(i)
      V1.append(G.get_edgelist()[i][0])  # The first node connected to b
      V2.append(G.get_edgelist()[i][1])  # The second node connected to b
  #print 'V1 = ', V1
  #print 'V2 = ', V2
  for i in range(0,len(V1)):
    G.add_edges([(V2[i],V1[i])])
    G.es[G.get_eid(V2[i],V1[i])]['F_or_B'] = 0   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(V2[i],V1[i])]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
  
  return G
#End
###################################

