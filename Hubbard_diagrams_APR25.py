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

###################################
###########Diagram checks##########
###################################
#Begin
def checks(G,M):
  FLAG_AMI=0
  if is_connected(G) and Irreducible(G):
    labels = G.es["Label"]
    reset_g(G,M)
    if Hubbard_diagram(G,M):
      AMI_INPUT = AMI_Input(labels,M)
      FLAG_AMI=AMI_zero(AMI_INPUT)
  val=[]
  val.append(FLAG_AMI)
  if FLAG_AMI!=0:
    val.append(AMI_INPUT)
  return val
#End
###################################

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
  G.es["name2"] = ["0-F", "1-B", "2-F", "3-F", "4-B", "5-F", "6-F"]
  G.es["F_or_B"] = [1,0,1,1,0,1,1]
  G.es["INT_or_EXT"] = [0,1,1,1,1,1,0]
  G.es["Label"] = [[None]*(M+1)]*l  # Define "None" labels
   
  #End
  #####################################
  
  return G

#End
######################################

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

highest_order=6
D=[0]*highest_order
D[1]=1
iso_gs=[]  # To store all topologically distint diagrams
count=0
m=2
g1=generate_g_2(m)
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
file_name = 'm_'+str(m)+'_'+'num_'+str(count+1)+'.eps'
plot(g1,'result_int/'+file_name, **visual_style)
file_name= 'm_'+str(m)+'_'+'num_'+str(count+1)
g1.save('result_int/'+file_name+'.graphml')
#End
###############################

for i in range (0,1000000):
  #if i%5000==0:
    #print i
  #if count==8954:
    #print i
  g1_old=g1.copy()
  m_old=m
  g_order_new=update_topol(g1,m)
  m=g_order_new[1]
  g1=g_order_new[0].copy()
  if is_connected(g1)==False:
    g1=g1_old.copy()
    m=m_old 
    reset_g(g1,m)
  CHECKS=checks(g1,m)
  reset_g(g1,m)
  #print 'g_new --> ' 
  #print g1
  #print 'visited = ', g1.vs['visited']
  #print 'F_or_B  = ', g1.es['F_or_B']
  #print 'INT_or_EXT = ', g1.es["INT_or_EXT"]
  #print 'Labels = ', g1.es["Label"]
  #print '*******'
  #print 
  if CHECKS[0]==1:
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
      #if Irreducible(g1):
      #reset_g(g1,m)
      iso_gs.append(g1.copy())
      count=count+1
      D[m-1]=D[m-1]+1
      ###################################
      ############Save Figure############
      ###################################
      #Begin
      visual_style = {}
      color_dict = {"m": "black", "f": "white"} 
      visual_style["vertex_size"] = 20
      visual_style["edge_label"] = g1.es["F_or_B"]
      file_name = 'm_'+str(m)+'_'+'num_'+str(D[m-1])+'.eps'
      plot(g1,'result_int/'+file_name, **visual_style)
      file_name= 'm_'+str(m)+'_'+'num_'+str(D[m-1])
      g1.save('result_int/'+file_name+'.graphml')
      
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
print D

'''
for i in range(0,1000):
  if m>3:
    m=2
    g1=generate_g_2(m)
    
  g1_old=g1.copy()
  #r=randint(0,2)
  if i%2==0: 
    add_int_line(g1)
    m=m+1
    reset_g(g1,m)
    if is_connected(g1)==False:
      g1=g1_old.copy()
      m=m-1 
    reset_g(g1,m)
    CHECKS=checks(g1,m)
    
    
      
    if CHECKS[0]==1:
      
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
      #file_name = 'm_'+str(m)+'_'+'num_'+str(1)+'.eps'
      plot(g1, **visual_style)
      #file_name= 'm_'+str(m)+'_'+'num_'+str(1)
      #g1.save('result/'+file_name+'.graphml')
      #End
      ###############################
  else:
    remove_int_line(g1)
    m=m-1
    reset_g(g1,m)
    if is_connected(g1)==False:
      g1=g1_old.copy()
      m=m+1 
    reset_g(g1,m)
    CHECKS=checks(g1,m)
    reset_g(g1,m)
    
    if CHECKS[0]==1:
     
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
      #file_name = 'm_'+str(m)+'_'+'num_'+str(1)+'.eps'
      plot(g1, **visual_style)
      #file_name= 'm_'+str(m)+'_'+'num_'+str(1)
      #g1.save('result/'+file_name+'.graphml')
      #End
      ###############################  
'''


