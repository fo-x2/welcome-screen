from sys import pycache_prefix

a1 = 'hello world'
a2 = "hello world"
a3 = '''hello 
world'''
# print(a1)
# print(a2)
# print(a3)
#
# account=input("账号:")
# password=input("密码:")
# print("%s,欢迎登录! " % account)
fmt = "{}, 欢迎登录！"
print(fmt.format("张三"))

b ='pcy'
print(f"{b},您好" )

print(a1.find("python"))
print(a1. index( "world"))