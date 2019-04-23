##################################
##########Import Libraries########
##################################
#Begin
from Label_self import *
from igraph import *
from random import *
from AMI_zero import *
from Hubbard_like_diagram import *
from is_connected import *
from add_remove import *
from Topology_check import *
import numpy
#End
###################################

########################################
##Define a 1st order self-energy graph##
########################################
#Begin
def generate_g_1_1(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,2)])
  G.add_edges([(3,1)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3]
  G.vs["visited"] = [1,1,0,0]
  G.vs["Spin"] = [None]*n_v
  G.es["name2"] = ["0-F", "1-F", "2-B", "3-F"]
  G.es["F_or_B"] = [1,1,0,1]
  G.es["INT_or_EXT"] = [0,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
###################################

########################################
##Define a 1st order self-energy graph##
########################################
#Begin
def generate_g_1_2(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(2,3)])
  G.add_edges([(3,1)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3]
  G.vs["visited"] = [1,1,0,0]
  G.vs["Spin"] = [None]*n_v
  G.es["name2"] = ["0-F", "1-F", "2-B", "3-F"]
  G.es["F_or_B"] = [1,1,0,1]
  G.es["INT_or_EXT"] = [0,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
###################################

########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_2_1(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,4)])
  G.add_edges([(4,5)])
  G.add_edges([(2,4)])
  G.add_edges([(3,5)])
  G.add_edges([(5,1)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3, 4, 5]
  G.vs["visited"] = [1,1,0,0,0,0]
  G.vs["Spin"] = [None]*n_v
  #G.es["name2"] = ["0-F", "1-B", "2-F", "3-F", "4-B", "5-F", "6-F"]
  G.es["F_or_B"] = [1,1,1,1,0,0,1]
  G.es["INT_or_EXT"] = [0,1,1,1,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
######################################

########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_2_2(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,4)])
  G.add_edges([(4,3)])
  G.add_edges([(5,4)])
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
###################################

###################################
##########Update topol#############
###################################
#Begin
def update_topol(G,M):
  r=random()
  if M==1:
    r=1
  if M==highest_order:
    r=0
  if r<0.5:
    G=remove_int_line(G)
    ORDER=M-1
    reset_g(G,ORDER)
  if r>=0.5:
    G=add_int_line(G)
    ORDER=M+1
    reset_g(G,ORDER)
  return G,ORDER
#End
###################################
########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_2_red(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,2)])
  G.add_edges([(3,4)])
  G.add_edges([(4,5)])
  G.add_edges([(5,4)])
  G.add_edges([(5,1)])

  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3, 4, 5]
  G.vs["visited"] = [1,1,0,0,0,0]
  G.vs["Spin"] = [None]*n_v
  G.es["name2"] = ["0-F", "1-F", "2-B", "3-F", "4-F", "5-B", "6-F"]
  G.es["F_or_B"] = [1,1,0,1,1,0,1]
  G.es["INT_or_EXT"] = [0,1,1,1,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
######################################

###################################
########################################
##Define a 2nd order self-energy graph##
########################################
#Begin
def generate_g_3_red(M):  # M: order of diagram
  n_v = N_V(M)
  l = L(M)
  G = Graph(directed=True)
  G.add_vertices(n_v) 

  G.add_edges([(0,2)])
  G.add_edges([(2,3)])
  G.add_edges([(3,4)])
  G.add_edges([(4,5)])
  G.add_edges([(5,6)])
  G.add_edges([(6,7)])
  G.add_edges([(3,4)])
  G.add_edges([(2,5)])
  G.add_edges([(7,6)])
  G.add_edges([(7,1)])
  #####################################
  ############Attributes###############
  #####################################
  #Begin
  G.vs["name1"] = [0, 1, 2, 3, 4, 5]
  G.vs["visited"] = [1,1,0,0,0,0,0,0]
  G.vs["Spin"] = [None]*n_v
  G.es["name2"] = ["0-F", "1-F", "2-F", "3-F", "4-F", "5-F", "6-B", "7-B","8-B","9-F"]
  G.es["F_or_B"] = [1,1,1,1,1,1,0,0,0,1]
  G.es["INT_or_EXT"] = [0,1,1,1,1,1,1,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
######################################


highest_order=3
iso_gs=[]  # To store all topologically distint diagrams
count=0
m=2
g1=generate_g_2_1(m)  # Initial diagram: Fock term
#print '******', Irreducible(g1)

iso_gs.append(g1.copy())
print
print '*******'
print 'g1 --> ' 
print g1
print 'visited = ', g1.vs['visited']
print 'F_or_B  = ', g1.es['F_or_B']
print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
print 'Labels = ', g1.es["Label"]
print '*******'
print
reset_g(g1,m)
print g1.es["Label"]
###################################
############Save Figure############
###################################
#Begin
visual_style = {}
color_dict = {"m": "black", "f": "white"}
visual_style["vertex_size"] = 20
visual_style["edge_label"] = g1.es["F_or_B"]
file_name = 'm_'+str(m)+'_'+'num_'+str(count)+'.eps'
plot(g1,file_name, **visual_style)
file_name= 'm_'+str(m)+'_'+'num_'+str(count)
g1.save(file_name+'.graphml')
#End
###############################

for i in range (0,100000):
  g1_old=g1.copy()
  g_order_new=update_topol(g1,m)
  m=g_order_new[1]
  g1=g_order_new[0].copy()
  reset_g(g1,m)
  #print 'g_new --> ' 
  #print g1
  #print 'visited = ', g1.vs['visited']
  #print 'F_or_B  = ', g1.es['F_or_B']
  #print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
  #print 'Labels = ', g1.es["Label"]
  #print '*******'
  #print 
  flag_iso=True
  for j in range(0,len(iso_gs)):
    g_iso_mod=iso_gs[j].copy()
    mod_iso(g_iso_mod)
    g1_mod=g1.copy()
    mod_iso(g1_mod)
    #print g_iso_mod.isomorphic_vf2(g1_mode, return_mapping_12=False, return_mapping_21=False)
    if g_iso_mod.isomorphic_vf2(g1_mod, return_mapping_12=False, return_mapping_21=False)==True:
      flag_iso=False
      break
  #print 'flag_iso = ', flag_iso
  if flag_iso:
    #print g1
    #print 'visited = ', g1.vs['visited']
    #print 'F_or_B  = ', g1.es['F_or_B']
    #print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
    #print 'Labels = ', g1.es["Label"]
    if Irreducible(g1):
      #reset_g(g1,m)
      iso_gs.append(g1.copy())
      count=count+1
      ###################################
      ############Save Figure############
      ###################################
      #Begin
      visual_style = {}
      color_dict = {"m": "black", "f": "white"} 
      visual_style["vertex_size"] = 20
      visual_style["edge_label"] = g1.es["F_or_B"]
      file_name = 'm_'+str(m)+'_'+'num_'+str(count)+'.eps'
      plot(g1,file_name, **visual_style)
      file_name= 'm_'+str(m)+'_'+'num_'+str(count)
      g1.save(file_name+'.graphml')
      #End
      ###############################

for i in range (0,len(iso_gs)):
  print 'iso_gs --> ' 
  print iso_gs[i]
  print 'visited = ', iso_gs[i].vs['visited']
  print 'F_or_B  = ', iso_gs[i].es['F_or_B']
  print 'INT_or_EXT = ', iso_gs[i].es["INT_or_EXT"]
  print 'Labels = ', iso_gs[i].es["Label"]
  print '*******'
  print 
print 'count = ', count  
print len(iso_gs)

'''
print 
g1_copy = g1.copy()
g2_copy = g2.copy()

mod_iso(g1)
print '*******'
print 'g1_mod --> ' 
print g1
print 'visited = ', g1.vs['visited']
print 'F_or_B  = ', g1.es['F_or_B']
print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
print 'Labels = ', g1.es["Label"]
print '*******'
print

mod_iso(g2)
print '*******'
print 'g2_mod --> ' 
print g2
print 'visited = ', g2.vs['visited']
print 'F_or_B  = ', g2.es['F_or_B']
print 'INT_or_EXT = ', g2.es["INT_or_EXT"]
print 'Labels = ', g2.es["Label"]
print '*******'
print
print g2.isomorphic_vf2(g1, return_mapping_12=False, return_mapping_21=False)
'''
'''
m=2
g1=generate_g_2_1(m)
print
print '*******'
print 'g1 --> ' 
print g1
print 'visited = ', g1.vs['visited']
print 'F_or_B  = ', g1.es['F_or_B']
print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
print 'Labels = ', g1.es["Label"]
print '*******'
print
g2=generate_g_2_2(m)
print 'g2 --> ' 
print g2
print 'visited = ', g2.vs['visited']
print 'F_or_B  = ', g2.es['F_or_B']
print 'INT_or_EXT = ', g2.es["INT_or_EXT"]
print 'Labels = ', g2.es["Label"]
print '*******'
print

print g1.isomorphic_vf2(g2, return_mapping_12=False, return_mapping_21=False)
g1_copy = g1.copy()
g2_copy = g2.copy()

mod_iso(g1)
print '*******'
print 'g1_mod --> ' 
print g1
print 'visited = ', g1.vs['visited']
print 'F_or_B  = ', g1.es['F_or_B']
print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
print 'Labels = ', g1.es["Label"]
print '*******'
print

mod_iso(g2)
print '*******'
print 'g2_mod --> ' 
print g2
print 'visited = ', g2.vs['visited']
print 'F_or_B  = ', g2.es['F_or_B']
print 'INT_or_EXT = ', g2.es["INT_or_EXT"]
print 'Labels = ', g2.es["Label"]
print '*******'
print
print g2.isomorphic_vf2(g1, return_mapping_12=False, return_mapping_21=False)


print 'g1_mod --> ', g1
print 'g1_old --> ', g1_copy
print 'g2_mod --> ', g2
print 'g2_old --> ', g2_copy

g1.save('first.graphml')
X=load('first.graphml')
print X
print g1



m=1
g=generate_g_1_con(m)
print 'initial diagram = ', g
print '*******'
print 'after add_int_line : ',
add_int_line(g)
m=m+1
reset_g(g,m)
print g
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]
print '*******'
print 'after add_bub : ', 
add_bub(g)
m=m+2
reset_g(g,m)
print g
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]
print '*******'
print 'after add_tad : '
add_tad(g,m)
m=m+1
reset_g(g,m)
print g
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]
print '*******'
print 'after remove_bub : '
remove_bub(g)
m=m-2
flag_con=is_connected(g)
if flag_con:
  reset_g(g,m)
print flag_con
print g
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]
print '********'
print 'after remove_int_line : '
remove_int_line(g)
m=m-1
print g
flag_con=is_connected(g)
print flag_con
print 'visited after adding second edge = ', g.vs['visited']
print 'F_or_B after adding second edge = ', g.es['F_or_B']
print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
print 'Labels after adding second edge = ', g.es["Label"]
print
if flag_con:
  reset_g(g,m)
  print g
  print 'visited after adding second edge = ', g.vs['visited']
  print 'F_or_B after adding second edge = ', g.es['F_or_B']
  print 'INT_or_EXT after adding second edge = ', g.es["INT_or_EXT"]
  print 'Labels after adding second edge = ', g.es["Label"]
  print
print flag_con
'''

