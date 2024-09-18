# for loop

x = "adeelhassan"
for i in x :
    print(i)
    

a = "adeelhassan"
for i in a :
    print(i, end='')
    
for i in range(0,11):
    print(i)
    
n = int(input("enter a number"))
for i in range(1, n+1):
    for j in range(1, i+1): 
        print(j , end='')
        print()