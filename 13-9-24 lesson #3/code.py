# 
# String in python
# 
sti ="Asslam O Alikum"
print(sti)

srt= 'Asslam O Alikum'
print(srt)

st='Adeel said "I am busy today"'
print(st)

s ='Adeel said "I\'m busy today"'
print(s)
t='''Adeel said 
I am busy today'''
print(t)

ln="adeelhassan"
print(len(ln))
print(ln[5])
print(ln[0:5])
print(ln[5:])
print(ln[:5])

up="welcome to house"
print(up.upper())
print(up.find('o'))
print(up.replace("house", "python world"))
low="WELCOME"
print(low.lower())
print(low.split(" "))

stg1 ="good"
stg2 ="night"
stg3 ="boy"
stg= stg1 + stg2 +stg3
print(stg)

stg1 ="good"
stg2 ="night"
stg3 ="boy"
stg= "{} {} {}".format(stg1,stg2,stg3)
print(stg)

# 
# creating a dictionaries
# 
d1 ={}
print(d1)
print(type(d1))

d2={1:"Welcome", 2:"to", 3:"python"}
print(d2)

d3 ={
    "name":"Adeel",
    "age":"22",
    "profession":"student"
     }
print(d3)
d4 =({1:"Welcome", 2:"to", 3:"python"})
print(d4)
d4 =[{1:"Welcome", 2:"to", 3:"python"}]
print(d4)

d5={0:"we",1:"are",2:"one"}
print(d5.pop(0))
print(d5)

# 
# set
# 
s =set([1,2,3,4])
print(s)
print(type(s))

s1 =set([1,3,7,2])
s2 =set([3,2,8,9])
print(s1.union(s2))
print(s1.difference(s2))

# youtube


dic ={
    "Adeel":"Muslim country leader",
    "Country":"Pakistan"
}
print(dic["Adeel"])

dic.pop("Country")
print(dic)

dat ={
    350:"Adeel",
    351:"Zohaib"
}
print(dat[351])
print(dat.keys())
print(dat.get(350))
print(dat.values())
print(dat.items())

# print(dic.update(dat))

