# data type in python

# integers
a = 23
print(type(a))
b = 23444
print(type(b))

# float
num = 2.53
print(type(num))
val = 234.483
print(type(val))

# complex numbers

comp = 2+5j
print(type(comp))
print(comp.real)
print(comp.imag)

# Arithmetic operation
num1 = 24
num2 = 26
print(num1 + num2)

num3 = 23
num4 =3
print(num3 - num4)

num5 = 44
num6 = 45
print (num5 * num6)

num7 =43
num8 = 7
print(num7 / num8)

num9 = 51
num0 =12
print(num9 // num0)

numA = 2
numB =10
print(numA % numB)


nuM = 5
nUm = 10
print(nuM ** nUm)

# string

st = "192"
print(type(st))
print(st)

st = int(st)
print(type(st))
print(st)

st = float(st)
print(type(st))
print(st)

st = complex(st)
print(type(st))
print(st)


# functions

p = -7.5
print(abs(p))

import math
z =10
print(math.exp(z))

print(math.sqrt(9))

# 
# list
# 
num=[1,2,3,4]
print(num)
letter=['a','b','c','d']
print(letter)
print(letter[0:3])
stg=["adeel","hassan","sheikh"]
print(stg)
print(stg[0])
mix=[1,2,"adeel"]
print(mix)
print(mix[-1])
mat=[[1,2],["a","b"]]
print(mat)

conc = stg + num
print(conc)

x=[0]*100
print(x)

var =list("Muslim")
print(var)

num=[1,2,3,4]
one, *other =num
print(one)
print(other)
num.append(9)
print(num)

num.extend(mix)
print(num)

# var1=("d","a","c")
# var1.sort()
# print(var1)

a= (1,2,454,67)
print(len(a))
print(max(a))
print(min(a))
print(sum(a))

# 
#Tuple
# 
emp = "karachi",
print(type(emp))

emp1 =(1,2,3,4)
print(emp1) 
print(type(emp1))

city =("karachi","lahore","islamabad")
print(city[1])

print(city+emp1)
print(city,emp1)
print(city*5)
cit=("abcdef")
print(tuple(cit))

o= (1,2,4,5,5,4,3,2,1,1,9)
print(o.count(1))