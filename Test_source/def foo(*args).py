def foo(*args):
    for a in args:
        print(a)        

foo(1)
# 1

def bar(**kwargs):
    name = kwargs.pop("name",None)
    print('Name:',name)
    for a in kwargs:
        print(a, kwargs[a])  
        

bar( age=27 , sex = 'male')
# age 27
# name one