#baitap1
import math 
def calc_f1_score(tp, fp, fn):
  precision=tp/(tp+fp)
  recall=tp/(tp+fn)
  f1_score=2*((precision*recall)/(precision+recall))
  return f1_score
assert round ( calc_f1_score ( tp =2 , fp =3 , fn =5) , 2) == 0.33
print(round(calc_f1_score(tp=2, fp=3, fn=5), 2))

#baitap2
import math
def is_number(n):
  try:
    float(n)  
  except ValueError:
    return False 
  return True   
assert is_number (3) == True
assert is_number (' -2a') == False
print ( is_number (1) )
print ( is_number ('n') )

#baitap3
x=-2.0
if x<=0:
  y=0.0
else:
  y=x
print(y)

#baitap4
import math
def calc_sig(x):
  signmoid=1/(1+math.e**(-x))
  return signmoid
assert round ( calc_sig (3) , 2) ==0.95
print ( round ( calc_sig (2) , 2) )

#baitap5
import math
a=0.01
def calc_elu(x):
  if x <= 0:
    elu=a*(math.e**x-1)
  else:
    elu=x
  return elu
assert round ( calc_elu (1)) ==1
print(round(calc_elu(-1),2))

#baitap6
import math
def calc_activation_func (x, act_name):
  act=1/(1+math.e**-x)
  return act
assert calc_activation_func(x=1,act_name='relu')
print(round(calc_activation_func(x=3,act_name='sigmoid'),2))

#baitap7
import math 
def calc_ae(y,y_hat):
  ae=math.fabs(y-y_hat)
  return ae
y=1
y_hat=6
assert calc_ae(y,y_hat)==5
y=2
y_hat=9
print(calc_ae(y,y_hat))

#baitap8
def calc_se(y,y_hat):
   se=(y-y_hat)**2
   return se 
y=4
y_hat=2
assert calc_se(y,y_hat)==4
print(calc_se(2,1))

#baitap9
def factorial_fcn(x):
  res=1
  for i in range(x):
    res=res*(i+1)
  return res 

def approx_cos(x,n):
  cos_approx=0
  for i in range(n+1):
    a=(-1)**i
    b=x**(2*i)
    c=factorial_fcn(2*i)
    cos_approx += a*(b/c)
  return cos_approx 
assert round ( approx_cos ( x =1 , n =10) , 2) ==0.54
print ( round ( approx_cos ( x =3.14 , n =10) , 2) )

#baitap10
def factorial_fcn(x):
  res=1
  for i in range(x):
    res=res*(i+1)
  return res 

def approx_sin(x,n):
  sin_approx=0
  for i in range(n+1):
    a=(-1)**i
    b=x**(2*i+1)
    c=factorial_fcn(2*i+1)
    sin_approx += a*(b/c)
  return sin_approx
assert round ( approx_sin ( x =1 , n =10) , 4) ==0.8415
print ( round ( approx_sin ( x =3.14 , n =10) , 4) )

#baitap11
def factorial_fcn(x):
  res=1
  for i in range(x):
    res=res*(i+1)
  return res 

def approx_sinh(x,n):
  sinh_approx=0
  for i in range(n+1):
    a=1
    b=x**(2*i+1)
    c=factorial_fcn(2*i+1)
    sinh_approx += a*(b/c)
  return sinh_approx 
assert round ( approx_sinh ( x =1 , n =10) , 2) ==1.18
print ( round ( approx_sinh ( x =3.14 , n =10) , 2) )

#baitap12
def factorial_fcn(x):
  res=1
  for i in range(x):
    res +=(i)
    return res 
  
def approx_cosh(x,n):
  cosh_approx=0
  for i in range(n+1):
    d=1
    e=x**(2*i)
    f=factorial_fcn(2*i)
    cosh_approx += d*(e/f) 
  return cosh_approx 
assert round ( approx_cosh ( x =1 , n =10) , 2) ==1.54
print ( round ( approx_cosh ( x =3.14 , n =10) , 2) )



