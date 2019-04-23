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
import numpy
#End
###################################

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


