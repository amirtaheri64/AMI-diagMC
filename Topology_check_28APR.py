##################################
##########Import Libraries########
##################################
#Begin
from igraph import *
from random import *
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

###################################
###########Switch nodes############
###################################
#Begin
def switch_nodes(G):
  #nv=G.vcount()
  l=G.ecount()
  b_list=[]
  for i in range(0,l):
    if G.es['F_or_B'][i]==0:
      b_list.append(i)
      #V.append(G.get_edgelist()[i][0])  # The first node connected to b
      #V.append(G.get_edgelist()[i][1])  # The second node connected to b
  n_b=len(b_list)
  if n_b>=2:
    pick1=randint(0,n_b-1)
    pick2=randint(0,n_b-1)
    b1=b_list[pick1]
    b2=b_list[pick2]
    #print 'b1 = ', b1
    #print 'b2 = ', b2
    if b1!=b2:
      V11=G.get_edgelist()[b1][0]
      #print 'V11 = ', V11 
      V12=G.get_edgelist()[b1][1]
      #print 'V12 = ', V12
      V21=G.get_edgelist()[b2][0]
      #print 'V21 = ', V21 
      V22=G.get_edgelist()[b2][1]
      #print 'V22 = ', V22
      G.delete_edges(b1)   # Delete b1
      if b1<b2:
        G.delete_edges(b2-1)  # Delete b2
      else:
        G.delete_edges(b2)  # Delete b2
      G.add_edges([(V11,V21)])     # Add first edge between V1 and new node
      G.es[G.get_eid(V11,V21)]['F_or_B'] = 0   # Update 'F_or_B' attribute of the new edge
      G.es[G.get_eid(V11,V21)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
      G.add_edges([(V12,V22)])     # Add first edge between V1 and new node
      G.es[G.get_eid(V12,V22)]['F_or_B'] = 0   # Update 'F_or_B' attribute of the new edge
      G.es[G.get_eid(V12,V22)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
  #print G
  #print 'F_or_B : ', G.es['F_or_B']
  #print 'INT_or_EXT : ', G.es['INT_or_EXT']
  return G
  
#End
###################################

