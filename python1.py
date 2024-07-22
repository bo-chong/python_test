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
print("string------------------------------------------------")
str = 'mypython' # 字符串
print(str[0:2])
print(str[0:-1])
print(str+'TEST')

print("list------------------------------------------------")
muitiples = [i for i in range(30) if i%3==0] # 列表推导式
print(muitiples)

t = ["a",'b','c',"d"] # 列表
i = ["e","f","g"]
print(t)
t[1] = 'x'
print(t)
it = iter(t)
print(next(it))
print(next(it))
print(next(it))

print("tuple------------------------------------------------")
tuple = (1,2,3,4,5) # 元组
print(tuple[1:3])
print(tuple[2:])

a =(tuple(x) for x in range(10)) # 元组推导式
print(a)

print("set------------------------------------------------")
sites_1 = {'a','b','c','d'} # 集合
sites_2 = {'e','f','g','d'}
print(sites_1)
print(sites_1-sites_2)
print(sites_1 | sites_2)
print(sites_1 & sites_2)
print(sites_1 ^ sites_2)

setnew ={i**2 for i in range(4)} # 集合推导式
print(setnew)

print("dictionary------------------------------------------------")
dic = {'name':'John', 'age':30, 'city':'New York'} # 字典
print(dic['name'])
print(dic.keys())
print(dic.values())
print(dic.items())

dic1 = {x: x**2 for x in range(1,6)} # 字典推导式
print(dic1)

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

a = 10
if a > 5:
    print(a)
else:
    print("a is less than 5")

def count_down(n):
    while n>0:
        yield n
        n -= 1

generator = count_down(10)

print(next(generator))
print(next(generator))
print(next(generator))

def max(a,b):
 if a>b:
    return a
 else:
    return b

print(max(10,20))