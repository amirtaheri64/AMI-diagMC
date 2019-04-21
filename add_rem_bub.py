##################################
##########Import Libraries########
##################################
#Begin
from random import *
from igraph import *
import numpy
from Label_self import * 
#End
###################################

##############################
####Compute l_f, l_i,l,n_v####
##############################

def L_F(M):
  return 2*M+1

def L_I(M):
  return M

def L(M):
  return L_F(M)+L_I(M)

def N_V(M):
  return 2*M+2

#End
################################

########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_1_con(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(2,3)])
  G.add_edges([(3,1)])
  G.add_edges([(0,3)])
  G.add_edges([(2,2)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3]
  G.vs["visited"] = [1,1,0,0]
  G.vs["Spin"] = [None]*n_v
  G.es["name2"] = ["0-F", "1-F", "2-B", "3-F"]
  G.es["F_or_B"] = [0,1,1,1]
  G.es["INT_or_EXT"] = [1,0,0,1]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
#############################################

########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_2(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,4)])
  G.add_edges([(4,3)])
  G.add_edges([(4,5)])
  G.add_edges([(2,5)])
  G.add_edges([(5,1)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3, 4, 5]
  G.vs["visited"] = [1,1,0,0,0,0]
  G.vs["Spin"] = [None]*n_v
  #G.es["name2"] = ["0-F", "1-B", "2-F", "3-F", "4-B", "5-F", "6-F"]
  G.es["F_or_B"] = [1,0,1,1,0,1,1]
  G.es["INT_or_EXT"] = [0,1,1,1,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
######################################

###################################
###########Add vertices############
###################################
#Begin
def add_nodes(G):
  NV = G.vcount()
  #print 'NV = ', NV
  l = G.ecount()
  #print 'l = ', l
  #l_f = 0
  #for i in range (0,l):   # Sweep all the lines
    #if G.es[i]['F_or_B'] == 1:   # If the line is fermionic
      #l_f = l_f+1  
  #print 'l_f = ', l_f
  #f_list = [None]*l_f   # To store the fermionic lines' indices
  #index_f_list = 0   # The index of f_list
  #for i in range (0,l):   # Sweep all the lines
    #if G.es[i]['F_or_B'] == 1:   # If the line is fermionic
      #f_list[index_f_list] = i   # Store the fermionic line index
      #index_f_list = index_f_list + 1 
  #print 'f_list = ', f_list 
  ### 
  f_list=[]
  for i in range (0,l):   # Sweep all the lines
    if G.es[i]['F_or_B'] == 1:   # If the line is fermionic
      f_list.append(i) 
  l_f=len(f_list) 
  pair=[]
  pairs=[]
  for i in range(0,l_f):
    for j in range(i,l_f):
      pair.append(i)
      pair.append(j)
      pairs.append(pair)
      pair=[]
  pick_lines=randint(0,len(pairs)-1)
  f1=pairs[pick_lines][0]
  f2=pairs[pick_lines][1]
  ###
  #f1 = randint(0,l_f-1)   # Choose one of the fermionic lines randomly
  #f2 = randint(0,l_f-1)   # Choose another fermionic line randomly
  #print 'f1 = ', f1
  #print 'f2 = ', f2
  V1 = G.get_edgelist()[f_list[f1]][0]  # The first node connected to f1
  print 'V1 = ', V1
  V2 = G.get_edgelist()[f_list[f1]][1]  # The second node connected to f1
  print 'V2 = ', V2
  V3 = G.get_edgelist()[f_list[f2]][0]  # The first node connected to f1
  print 'V3 = ', V3
  V4 = G.get_edgelist()[f_list[f2]][1]  # The second node connected to f1
  print 'V4 = ', V4
  #print 'Initial diagram = ', G
  #print 'Initial name1 = ', G.vs['name1']
  #print 'Initial visited = ', G.vs['visited']
  #print 'Initial F_or_B = ', G.es['F_or_B']
  #print 'Initial INT_or_EXT = ', G.es["INT_or_EXT"]
  if f1==f2:
    G.add_vertices(2)  # Add a node
    #G.vs[NV]['name1'] = NV  # Update 'name1' attribute of the new node
    G.vs[NV]["visited"] = 0       # Update 'visited' attribute of the new node
    #G.vs[NV+1]['name1'] = NV+1  # Update 'name1' attribute of the new node
    G.vs[NV+1]["visited"] = 0       # Update 'visited' attribute of the new node
    #print 'Diagram after one node = ', G
    #print 'name1 after one node = ', G.vs['name1']
    #print 'visited after one node = ', G.vs['visited']
    #print 'F_or_B after one node = ', G.es['F_or_B']
    #print 'INT_or_EXT after one node = ', G.es["INT_or_EXT"]
    G.delete_edges(f_list[f1])  # Delete f1
    #print 'Diagram after deleting one edge = ', G
    #print 'name1 after deleting one edge = ', G.vs['name1']
    #print 'visited after deleting one edge = ', G.vs['visited']
    #print 'F_or_B after deleting one edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after deleting one edge = ', G.es["INT_or_EXT"]
    G.add_edges([(V1,NV)])     # Add first edge between V1 and new node
    G.es[G.get_eid(V1,NV)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(V1,NV)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding first edge = ', G
    #print 'name1 after adding first edge = ', G.vs['name1']
    #print 'visited after adding first edge = ', G.vs['visited']
    #print 'F_or_B after adding first edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding first edge = ', G.es["INT_or_EXT"]
    G.add_edges([(NV,NV+1)])     # Add second edge between new node and V2
    G.es[G.get_eid(NV,NV+1)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(NV,NV+1)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding second edge = ', G
    #print 'name1 after adding second edge = ', G.vs['name1']
    #print 'visited after adding second edge = ', G.vs['visited']
    #print 'F_or_B after adding second edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding second edge = ', G.es["INT_or_EXT"]
    G.add_edges([(NV+1,V2)])     # Add second edge between new node and V2
    G.es[G.get_eid(NV+1,V2)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(NV+1,V2)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding second edge = ', G
    #print 'name1 after adding second edge = ', G.vs['name1']
    #print 'visited after adding second edge = ', G.vs['visited']
    #print 'F_or_B after adding second edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding second edge = ', G.es["INT_or_EXT"]
  if f1!=f2:
    G.add_vertices(2)  # Add two nodes
    #G.vs[NV]['name1'] = NV  # Update 'name1' attribute of the new node
    G.vs[NV]["visited"] = 0       # Update 'visited' attribute of the new node
    #G.vs[NV+1]['name1'] = NV+1  # Update 'name1' attribute of the new node
    G.vs[NV+1]["visited"] = 0       # Update 'visited' attribute of the new node
    #print 'Diagram after one node = ', G
    #print 'name1 after one node = ', G.vs['name1']
    #print 'visited after one node = ', G.vs['visited']
    #print 'F_or_B after one node = ', G.es['F_or_B']
    #print 'INT_or_EXT after one node = ', G.es["INT_or_EXT"]
    G.delete_edges(f_list[f1])  # Delete f1
    #print '*****************8'
    #print 'Diagram after deleting one edge = ', G
    #print 'name1 after deleting one edge = ', G.vs['name1']
    #print 'visited after deleting one edge = ', G.vs['visited']
    #print 'F_or_B after deleting one edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after deleting one edge = ', G.es["INT_or_EXT"]
    if f_list[f1]<f_list[f2]:
      G.delete_edges(f_list[f2]-1)  # Delete f2
    else:
      G.delete_edges(f_list[f2])  # Delete f2
    #print 'Diagram after deleting one edge = ', G
    #print 'name1 after deleting one edge = ', G.vs['name1']
    #print 'visited after deleting one edge = ', G.vs['visited']
    #print 'F_or_B after deleting one edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after deleting one edge = ', G.es["INT_or_EXT"]
    G.add_edges([(V1,NV)])     # Add first edge between V1 and new node
    G.es[G.get_eid(V1,NV)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(V1,NV)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding first edge = ', G
    #print 'name1 after adding first edge = ', G.vs['name1']
    #print 'visited after adding first edge = ', G.vs['visited']
    #print 'F_or_B after adding first edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding first edge = ', G.es["INT_or_EXT"]
    G.add_edges([(NV,V2)])     # Add second edge between new node and V2
    G.es[G.get_eid(NV,V2)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(NV,V2)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding second edge = ', G
    #print 'name1 after adding second edge = ', G.vs['name1']
    #print 'visited after adding second edge = ', G.vs['visited']
    #print 'F_or_B after adding second edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding second edge = ', G.es["INT_or_EXT"]
    
    G.add_edges([(V3,NV+1)])     # Add first edge between V1 and new node
    G.es[G.get_eid(V3,NV+1)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(V3,NV+1)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding first edge = ', G
    #print 'name1 after adding first edge = ', G.vs['name1']
    #print 'visited after adding first edge = ', G.vs['visited']
    #print 'F_or_B after adding first edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding first edge = ', G.es["INT_or_EXT"]
    G.add_edges([(NV+1,V4)])     # Add second edge between new node and V2
    G.es[G.get_eid(NV+1,V4)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
    G.es[G.get_eid(NV+1,V4)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge
    #print 'Diagram after adding second edge = ', G
    #print 'name1 after adding second edge = ', G.vs['name1']
    #print 'visited after adding second edge = ', G.vs['visited']
    #print 'F_or_B after adding second edge = ', G.es['F_or_B']
    #print 'INT_or_EXT after adding second edge = ', G.es["INT_or_EXT"]   
  return G, NV   
#End
################################### 

###################################
#####Add an independent bubble#####
###################################
#Begin
def add_bub(G):
  out1 = add_nodes(G)
  NV = G.vcount()   # Total number od nodes
  print NV
  V1 = out1[1]
  V2 = V1+1
  G_imt = out1[0]
  #print 'First added node = ', V1
  #print 'Second added node = ', V2
  #print 'G_final_before_int_line = ', G_imt
  G.add_vertices(2)  # Add a node
  #G.vs[NV]['name1'] = NV  # Update 'name1' attribute of the new node
  G.vs[NV]["visited"] = 0       # Update 'visited' attribute of the new node
  #G.vs[NV+1]['name1'] = NV+1  # Update 'name1' attribute of the new node
  G.vs[NV+1]["visited"] = 0       # Update 'visited' attribute of the new node
  #print 'Diagram after two nodes = ', G
  #print 'name1 after two nodes = ', G.vs['name1']
  #print 'visited after two nodes = ', G.vs['visited']
  #print 'F_or_B after two nodes = ', G.es['F_or_B']
  #print 'INT_or_EXT after two nodes = ', G.es["INT_or_EXT"]
  G.add_edges([(V1,NV)])     # Add an interaction line between two new nodes
  G.es[G.get_eid(V1,NV)]['F_or_B'] = 0   # Update 'F_or_B' attribute of the new edge
  G.es[G.get_eid(V1,NV)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge

  G.add_edges([(NV+1,V2)])     # Add an interaction line between two new nodes
  G.es[G.get_eid(NV+1,V2)]['F_or_B'] = 0   # Update 'F_or_B' attribute of the new edge
  G.es[G.get_eid(NV+1,V2)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge

  G.add_edges([(NV,NV+1)])     # Add first fermionic edge
  G.es[G.get_eid(NV,NV+1)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
  G.es[G.get_eid(NV,NV+1)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge

  G.add_edges([(NV+1,NV)])     # Add first fermionic edge
  G.es[G.get_eid(NV+1,NV)]['F_or_B'] = 1   # Update 'F_or_B' attribute of the new edge
  G.es[G.get_eid(NV+1,NV)]['INT_or_EXT'] = 1   # Update 'INT_or_EXT' attribute of the new edge


  #print 'Diagram after adding second edge = ', G
  #print 'name1 after adding second edge = ', G.vs['name1']
  #print 'visited after adding second edge = ', G.vs['visited']
  #print 'F_or_B after adding second edge = ', G.es['F_or_B']
  #print 'INT_or_EXT after adding second edge = ', G.es["INT_or_EXT"] 
  return G
#End
###################################

###################################
#########Bubble Finder############# 
###################################
#Begin
def bubble_finder(G):
  #print 'Initial diagram = ', G
  #print 'Initial name1 = ', G.vs['name1']
  #print 'Initial visited = ', G.vs['visited']
  #print 'Initial F_or_B = ', G.es['F_or_B']
  #print 'Initial INT_or_EXT = ', G.es["INT_or_EXT"]
  NV = G.vcount()   # Total number od nodes
  #print 'NV = ', NV  
  l = G.ecount()   # Total number of lines
  #print 'l = ', l
  bubble_list = []
  nodes_list = []
  legs = []
  
  for i in range(0,NV):
    #print i
    counter = 0
    out_nodes = G.neighbors(i,mode=OUT)
    in_nodes = G.neighbors(i,mode=IN)
    nodes = [None]*(len(out_nodes) + len(in_nodes))
    for j in range(0,len(out_nodes)):
      nodes[counter]=out_nodes[j]
      counter = counter + 1
    for j in range(0,len(in_nodes)):
      nodes[counter]=in_nodes[j]
      counter = counter + 1
    #print 'len = ', len(nodes)
    #print 'node = ', i
    #print 'out_nodes = ', out_nodes
    #print 'in_nodes = ', in_nodes
    for j in range(0,len(nodes)):
      for k in range(j+1,len(nodes)): 
        #print 'j =',j
        #print 'k =', k
        a = nodes[j]
        b = nodes[k]
        
        if a == b:
          
          if a in in_nodes:
            if a in out_nodes:
              if G.es[G.get_eid(a,i)]['F_or_B'] == 1 and G.es[G.get_eid(i,a)]['F_or_B'] == 1 and a!=i:
                bubble_list.append(nodes)
                nodes_list.append(a)
                nodes_list.append(i)
                for r in range (0,len(nodes)):
                  if nodes[r]!=a:
                    legs.append(nodes[r])
                for s in range(0,len(G.neighbors(a,mode=OUT))):
                  if G.es[G.get_eid(a,G.neighbors(a,mode=OUT)[s])]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=OUT)[s])
                for s in range(0,len(G.neighbors(a,mode=IN))):
                  if G.es[G.get_eid(G.neighbors(a,mode=IN)[s],a)]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=IN)[s])  
          
          if a in in_nodes:
            if a not in out_nodes:
              if len(out_nodes)!=0:
                c = out_nodes[0] 
              else:
                for t in range(0,len(in_nodes)):
                  if in_nodes[t]!=a:
                    c=in_nodes[t] 
              if (c in in_nodes) and (G.es[G.get_eid(c,i)]['F_or_B'] == 0) and (a!=i):
                bubble_list.append(nodes)
                nodes_list.append(a)
                nodes_list.append(i)
                for r in range (0,len(nodes)):
                  if nodes[r]!=a:
                    legs.append(nodes[r])
                for s in range(0,len(G.neighbors(a,mode=OUT))):
                  if G.es[G.get_eid(a,G.neighbors(a,mode=OUT)[s])]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=OUT)[s])
                for s in range(0,len(G.neighbors(a,mode=IN))):
                  if G.es[G.get_eid(G.neighbors(a,mode=IN)[s],a)]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=IN)[s])  
              if (c in out_nodes) and (G.es[G.get_eid(i,c)]['F_or_B'] == 0) and (a!=i):
                bubble_list.append(nodes)
                nodes_list.append(a)
                nodes_list.append(i)
                for r in range (0,len(nodes)):
                  if nodes[r]!=a:
                    legs.append(nodes[r])
                for s in range(0,len(G.neighbors(a,mode=OUT))):
                  if G.es[G.get_eid(a,G.neighbors(a,mode=OUT)[s])]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=OUT)[s])
                for s in range(0,len(G.neighbors(a,mode=IN))):
                  if G.es[G.get_eid(G.neighbors(a,mode=IN)[s],a)]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=IN)[s])    

          if a not in in_nodes:
            if a in out_nodes:
              if len(in_nodes)!=0:
                c = in_nodes[0] 
              else:
                for t in range(0,len(out_nodes)):
                  if out_nodes[t]!=a:
                    c=out_nodes[t] 
              if (c in in_nodes) and (G.es[G.get_eid(c,i)]['F_or_B'] == 0) and (a!=i):
                bubble_list.append(nodes)
                nodes_list.append(a)
                nodes_list.append(i)
                for r in range (0,len(nodes)):
                  if nodes[r]!=a:
                    legs.append(nodes[r])
                for s in range(0,len(G.neighbors(a,mode=OUT))):
                  if G.es[G.get_eid(a,G.neighbors(a,mode=OUT)[s])]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=OUT)[s])
                for s in range(0,len(G.neighbors(a,mode=IN))):
                  if G.es[G.get_eid(G.neighbors(a,mode=IN)[s],a)]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=IN)[s])  
              if (c in out_nodes) and (G.es[G.get_eid(i,c)]['F_or_B'] == 0) and (a!=i):
                bubble_list.append(nodes)
                nodes_list.append(a)
                nodes_list.append(i)
                for r in range (0,len(nodes)):
                  if nodes[r]!=a:
                    legs.append(nodes[r])
                for s in range(0,len(G.neighbors(a,mode=OUT))):
                  if G.es[G.get_eid(a,G.neighbors(a,mode=OUT)[s])]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=OUT)[s])
                for s in range(0,len(G.neighbors(a,mode=IN))):
                  if G.es[G.get_eid(G.neighbors(a,mode=IN)[s],a)]['F_or_B'] == 0:
                    legs.append(G.neighbors(a,mode=IN)[s])  
  
    #for j in range (0, len(nodes)):
  #print bubble_list  
  #print nodes_list
  #print legs
  for i in range(0,len(legs)/2):
    for j in range(i+1,len(legs)/2):
      if (legs[2*i]==legs[2*j] and legs[2*i+1]==legs[2*j+1]) or (legs[2*i]==legs[2*j+1] and legs[2*i+1]== legs[2*j]):
        legs[2*j]=None
        legs[2*j+1]=None
        nodes_list[2*j]=None
        nodes_list[2*j+1]=None
  new_legs=[]
  new_nodes_list=[]
  for i in range(0,len(legs)):
    if legs[i]!=None:
      new_legs.append(legs[i])
      new_nodes_list.append(nodes_list[i])
  return new_nodes_list, new_legs
#End
###################################

m=2
g=generate_g_2(m)
print 'initial diagram = ', g
add_bub(g)
reset_g(g,m+2)
print g
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]

print 'bubbles = ', bubble_finder(g)



