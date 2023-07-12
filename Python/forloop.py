for i in range(1,100):
    print("number"+str(i)+str("--->")+str(i*2))
ab = [1,2,3,4,5,6,7,8,9,8] #list declaration
abset = set(ab)
print(abset)
b=0
for i in abset:
    if i>b:
        print(i)
        
    else:
        print("done with list")
    b=b+i

d = {'k1':'ankesh','k2':'nishu','k3':'joey'} #dict no gurentee of order for tht you need tuple
for key,values in d:
    print(values+key)

#enumerate functions usage
new1="ankeshkumar"
for key1,value1 in enumerate(new1):
    print(key1,value1)


#use of zip function
a1=[1,2,3,4,5]
b1=['a','b','c','d','e']
c1=zip(a1,b1)
for item in c1:
    print(item)

#list comprehension
n1="AnkeshKumar"
list_n1=list(n1)
list_n1.append('l')
print(list_n1)

#n2=[x for x in "ankesh"]
print([x for x in "ankesh"])
print([x**2 for x in range(1,10) if x<5])

x1=[]
for i in range(1,10):
    if i<5:
        x1.append(i**2)
print(x1)