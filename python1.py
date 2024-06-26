#！usr/bin/python3
# Print a greeting message to the console
import time
# for i in range(101):
#     print("\r{:3}%".format(i),end='')
#     time.sleep(0.05)
# Number String Tuple (不可变数据)
# List Dictionary Set (可变数据）
a , b, c, d =20, 5.5, True,4+3j
print(type(a),type(b),type(c),type(d))

str = 'mypython'
print(str[0:2])
print(str[0:-1])
print(str+'TEST')

t = ["a",'b','c',"d"]
i = ["e","f","g"]
print(t)
t[1] = 'x'
print(t)

tuple = (1,2,3,4,5)
print(tuple[1:3])
print(tuple[2:])

sites_1 = {'a','b','c','d'}
sites_2 = {'e','f','g','d'}
print(sites_1)
print(sites_1-sites_2)
print(sites_1 | sites_2)
print(sites_1 & sites_2)
print(sites_1 ^ sites_2)

dic = {'name':'John', 'age':30, 'city':'New York'}
print(dic['name'])
print(dic.keys())
print(dic.values())
print(dic.items())

x = b'hello'
y = x[1:3]
z = x + b'world'
print(x)
print(y)
print(z)

n = 10
if n>5:
    print(n)
if (n:=10) > 5:
    print(n)
# := 等于 == and =
