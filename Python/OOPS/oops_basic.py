class Animal():
    def __init__(self,cat,name,age):
        self.cat=cat
        self.name=name
        self.age= age
    def age_cal(self,age):
        if age>5:
            return 'young'
        else:
            return 'old'

my_animal = Animal('dog','Neo',7);
print(my_animal.name)
print(my_animal.cat)
print(my_animal.age)
print(my_animal.age_cal(4))

