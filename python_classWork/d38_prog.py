a=list(range(1,501))
b=list(filter(lambda x:x%3==0,a))
c=list(map(lambda x:x**5,b))
d=list(filter(lambda x:x%5==0,c))
e=list(map(lambda x:x//10,d))
print(e)