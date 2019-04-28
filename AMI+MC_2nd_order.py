###################################
#########Import libraries##########
###################################
#Begin
import pickle
from Symbolic_multi_AMI_new import *
from random import *
#End
###################################


###################################
############Update momenta#########
###################################
#Begin
def Integrand(arrs,M,F):
  out=[]
  ###################################
  #####Initialize moemntum array#####
  ###################################
  #Begin
  k_init=[ [0]*2 for i in range (0,M+1) ]  # initialize momenta
  k_init[M][0] = px_ext
  k_init[M][1] = py_ext
  #print k_init
  #End
  ###################################

  #start_time=time.time()
  
  
    
  ###################################
  #########Store AMI arrays########## 
  ###################################
  #Begin
  s_list=deepcopy(arrs[0])
  p_list_freq=deepcopy(arrs[1])
  p_list_mnta=deepcopy(arrs[2])
  r_freq=deepcopy(arrs[3])
  r_mnta=deepcopy(arrs[4])
  g_sym=deepcopy(arrs[5])
  #print 'S_list = ', s_list
  #print 'P_list_freq = ', p_list_freq
  #print 'P_list_mnta = ', p_list_mnta
  #print 'temp2_freq = ', r_freq
  #print 'temp2_mnta = ', r_mnta
  #print 'G_sym = ', g_sym
  #len_R=0
  #for i in range (0,len(temp2_freq)):
    #if temp2_freq[i]!=None:
      #len_R=len_R+1
    #else:
      #break
 
  for i in range (0,M):  # Pick momenta randomly
    for j in range (0,2):
      k_init[i][j]= (b_h-a_l)*random()+a_l
  #print 'k_init = ', k_init
  poles = Poles(p_list_freq, p_list_mnta,g_sym[0],k_init,t,mu)
  for i in range (0,len(poles)):
    for j in range (0,len(poles[i])):
      if poles[i][j]==None:
        j = len(poles[i])+1
      else:
        for l in range (0,len(poles[i][j])):
          #print poles[i][j][k]
          poles[i][j][l] = f(poles[i][j][l],beta)  # Find the numerical values 

  ########################################
  ################AMI Algebra#############
  ########################################

  res1 = dot_num(s_list[1][0], poles[1][0])
  temp=res1
  for it_m in range (2,M+1):
    o = 0
    for i in range(0, len(s_list[it_m])):
      if s_list[it_m][i] != None:
        o = o + 1
      else:
        i = len(poles[it_m]) + 1
    
    S_new = [None]*(o)
    P_new = [None]*(o)
    for i in range(0, len(S_list[it_m])):
      if S_list[it_m][i] != None:
        S_new[i] = s_list[it_m][i]
        P_new[i] = poles[it_m][i]
  
      else:
        i = len(s_list[it_m]) + 1

    res2 = dot_arr(S_new, P_new)
    temp = cross(res1,res2)
    res1 = temp
  
  G_val = 0.0  # To store numerical value at a given external frequency
  if len(r_freq[0])!=0:
    for j in range (0, len(temp)):
      G_val = temp[j]*G_eval(r_freq[j], r_mnta[j], nu_ext, G_sym[0],k_init,t,mu,beta) + G_val
    #print 'G_val = ', G_val
    #print '?????'
  else:
    for j in range (0, len(temp)):
      G_val = temp[j] + G_val 
    #print '?????'   
    #print 'G_val = ', G_val
  out.append((-1)**(M+F)*(U**M)*G_val.real/4**M/pi**(2*M))
  out.append((-1)**(M+F)*(U**M)*G_val.imag/4**M/pi**(2*M))
  #print out
  return out
      
#End
###################################


###################################
########Generate AMI arrays########
###################################
#Begin
file_name_ami_in='ami_in_m_'+str(2)+'_num_'+str(1)
with open(file_name_ami_in,"rb") as fp:
  ami=pickle.load(fp)
print 'ami_in = ', ami
file_name_F='f_m_'+str(2)+'_num_'+str(1)
with open(file_name_F,"rb") as fp:
  loop_num=pickle.load(fp)
print 'number of loops = ', loop_num
m=(len(ami)+1)/2
print 'order = ', m
b= AMI_arrays_out(ami,m)
S_list=deepcopy(b[0])
P_list_freq=deepcopy(b[1])
P_list_mnta=deepcopy(b[2])
R_freq=deepcopy(b[3])
R_mnta=deepcopy(b[4])
G_sym=deepcopy(b[5])
print 'S_list = ', S_list
print 'P_list_freq = ', P_list_freq
print 'P_list_mnta = ', P_list_mnta
print 'R_freq = ', R_freq
print 'R_mnta = ', R_mnta
print 'G_sym = ', G_sym
#print len(R_freq[0])
#End
###################################

###################################
######Read external variables######
###################################
#Begin
data = np.loadtxt('ext_vars.dat')  # reading external variables from a file
count = len(open('ext_vars.dat').readlines())
if count==1:
  EXT_VARS = [None]*count
  EXT_VARS[0]=data
if count>1:
  EXT_VARS = [None]*count  
  for i in range (0, count):
    EXT_VARS[i] = data[i,:]  
#print EXT_VARS
t=EXT_VARS[1][0]
U=EXT_VARS[1][1]
beta=EXT_VARS[1][2]
mu=EXT_VARS[1][3]
nu_ext=(2*EXT_VARS[1][4]+1)*pi/beta
px_ext=EXT_VARS[1][5]
py_ext=EXT_VARS[1][6]
lat_const=EXT_VARS[1][7]
print
print "Evaluation for the following parameters:"
print 't = ', t
print 'U = ', U
print 'beta = ', beta
print 'mu = ', mu
print 'nu_ext = ', nu_ext
print 'px_ext = ', px_ext
print 'py_ext = ', py_ext
print 'a = ', lat_const
a_l=-pi  # Lower limit of the integrals
b_h=pi   # Upper limit of the integrals
print
#End
###################################
#print Integrand(b,m,loop_num)

T=100
N=100000
print 'T = ', T
print 'N = ', N
avg_re=0
avg_im=0
ch_re=[]
ch_im=[]
for i_T in range(0,T):
  for i_N in range(0,N):
    result=Integrand(b,m,loop_num)
    re=result[0]
    im=result[1]
    avg_re=avg_re+re
    avg_im=avg_im+im
  ch_re.append(avg_re/N)
  ch_im.append(avg_im/N)
  avg_re=0 
  avg_im=0

re=0
im=0
for i_T in range(0,T):
  re=re+ch_re[i_T]
  im=im+ch_im[i_T]
re_fin = (2*pi)**(2*m)*re/T
im_fin = (2*pi)**(2*m)*im/T
var_re=0
var_im=0
for i_T in range(0,T):
  var_re=var_re+(re_fin-(2*pi)**(2*m)*ch_re[i_T])**2
  var_im=var_im+(im_fin-(2*pi)**(2*m)*ch_im[i_T])**2
var_re = sqrt(var_re/(T-1.0))
var_im = sqrt(var_im/(T-1.0))
er_re = var_re/sqrt(T)
er_im = var_im/sqrt(T) 
print 'Real Part = ', re_fin, '+-', er_re
print 'Imaginary Part = ', im_fin, '+-', er_im 

