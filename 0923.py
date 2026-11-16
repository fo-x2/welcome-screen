a = [True,1,2]
a2 = True
b = False
d = a
d2 = [True,1,2]
c = 3
g , h =12 , 45
c += g
print(a or b)
print(a and a2)
print(not b)
print(id(a),id(b))
print(a is d2)
print(a is not d2)
print(c)
print((c+h)/2,(c+h)%2,(c+h)**2,)
n = '男'
age = 10
lolgit = n == '男' and age <= 10
print(lolgit)

lolgit2 = n == '女' and age >= 11
print(lolgit2)
print(not(lolgit2))

lolgit3 = n == '女' or age <= 11
print(lolgit3)

a3 = 3242
a4 = str(a3)
print(bin(a3))

a5 = True
a6 = str(a5)
print(bin(a5))
print(type(print(bin(a5))))

aoo = input('eee')