a = [1,2,3,4,5,6,7]
print(list(map(lambda x:x**2,a)))
print(list(filter(lambda x:x%2==0,list(map(lambda x:x**2,a)))))


#LEGB rule
