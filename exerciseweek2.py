# bai tap mot
def max_kernel(num_list,k):
  result=[]
  k_list=[]
  k=3
  for number in num_list:
    k_list.append(number)
    if len(k_list)==k:
      result.append(max(k_list))
      k_list.pop(0)
  return result
assert max_kernel([3,4,5,1,-44],3)==[5,5,5]
num_list=[3,4,5,1,-44,5,10,12,33,1]
k=3
print(max_kernel(num_list,k))

# bai tap hai
def character_count(word):
  thongke={}
  for i in word:
    if i in thongke:
      thongke[i]+=1
    else:
      thongke[i]=1
  return thongke
assert character_count("Baby")=={'B':1,'a':1,'b':1,'y':1}
print(character_count("Smile"))
           
# bai tap ba
#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

# bai tap bon
def levenshtein_distance(token1,token2):
  distances=[[0]*(len(token2)+1) for i in range(len(token1)+1)]

  for t1 in range(len(token1)+1):
    distances[t1][0]=t1
  for t2 in range(len(token2)+1):
    distances[0][t2]=t2

  a=0
  b=0
  c=0
  for t1 in range(1, len(token1)+1):
    for t2 in range(1, len(token2)+1):
      if (token1[t1-1]==token2[t2-1]):
        distances[t1][t2]=distances[t1-1][t2-1]
      else:
        a=distances[t1][t2-1]
        b=distances[t1-1][t2]
        c=distances[t1-1][t2-1]

        if (a<=b and a<=c):
          distances[t1][t2]=a+1
        elif (b<=a and b<=c):
          distances[t1][t2]=b+1
        else:
          distances[t1][t2]=c+1
  return distances[len(token1)][len(token2)]
assert levenshtein_distance("hi","hello")==4
print(levenshtein_distance("hola","hello"))        

# bai tap nam
def check_the_number(N):
  list_of_numbers=[]
  results=""
  for i in range(1,5):
    list_of_numbers.append(i)
  if N in list_of_numbers:
    results="True"
  if N not in list_of_numbers:
    results="False"
  return results
N=7
assert check_the_number(N)=="False"
N=2
results=check_the_number(N)
print(results)

# bai tap sau
def my_function(data, max, min):
  result=[]
  for i in data:
    if i < min:
      result.append(min)
    elif i > max:
      result.append(max)
    else:
      result.append(i)
  return result
my_list=[5,2,5,0,1]
max=1
min=0
assert my_function(max=max, min=min,data=my_list)==[1,1,1,0,1]
my_list=[10,2,5,0,1]
max=2
min=1
print(my_function(max=max,min=min,data=my_list))

# bai tap bay
def my_function(x,y):
  x.extend(y)
  return x
list_num1=['a',2,5]
list_num2=[1,1]
list_num3=[0,0]
assert my_function(list_num1,my_function(list_num2,list_num3))==['a',2,5,1,1,0,0]
list_num1=[1,2]
list_num2=[3,4]
list_num3=[0,0]
print(my_function(list_num1,my_function(list_num2,list_num3)))

# bai tap tam
def my_function(a):
  min_value =a[0]
  for num in a:
    if num < min_value:
      min_value =num
  return min_value
my_list=[1,22,93,-100]
assert my_function(my_list)==-100
my_list= [1, 2, 3, -1]
print(my_function(my_list))

# bai tap chin
def my_function(n):
  max_value=n[0]
  for num in n:
    if num > max_value:
      max_value=num
  return max_value 
my_list=[1001,9,100,0]
assert my_function(my_list)==1001
my_list=[1,9,9,0]
print(my_function(my_list))

# bai tap muoi
def My_function(intergers, number=1):
  for num in intergers:
    if num == number:
      return True
    else:
      return False
my_list=[1,3,9,4]
assert My_function(my_list,-1)==False
my_list=[1,2,3,4]
print(My_function(my_list,2))

# bai tap muoi mot
def my_function(list_nums=[0,1,2]):
  var=0
  for i in list_nums:
    var +=i
  return var/len(list_nums)
assert my_function([4,6,8])==6
print(my_function())

# bai tap muoi hai
def my_function(data):
  var=[]
  for i in data:
    if i%3==0:
      var.append(i)
  return var
assert my_function([3,9,4,5])==[3,9]
print(my_function([1,2,3,5,6]))

# bai tap muoi ba
def my_function(y):
  var=1
  for i in range(1,y+1):
      var*=i
  return var
assert my_function(8)==40320
print(my_function(4))

# bai tap muoi bon
def my_function(x):
  reverse_str=""
  for i in range(len(x)-1,-1,-1):
    reverse_str += x[i]
  return reverse_str 
x='I can do it'
assert my_function(x)=='ti od nac I'
x='apricot'
print(my_function(x))

# bai tap muoi lam
def function_helper(x):
    if x > 0:
      return 'T'
    else:
      return 'N'
def my_function(data):
  res=[function_helper(x) for x in data]
  return res
data1=[10,0,-10,-1]
assert my_function(data1)==['T','N','N','N']
data2=[2,3,5,-1]
print(my_function(data2))

# bai tap muoi sau
def function_helper(x, data):
  for i in data:
    if x==i:
      return 0
    else:
      return 1
def my_function(data):
  res=[]
  for i in data:
    if function_helper(i,res):
      res.append(i)
  return res
lst1=[10,10,9,7,7]
assert my_function(lst1)==[10,9,7]
lst2=[9,9,8,1,1]
print(my_function(lst2))
  
    
     



    
