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


x= lambda a : a+20
print(x(10)) 

a= lambda x,y: x*y
print(a(6,8))

#装饰器
class myfunc:
   @staticmethod
   def add(x,y):
      return x+y

print(myfunc.add(10,20))
 
class myfunc1:
   @classmethod
   def add(cls,x,y):
      return x+y

print(myfunc1.add(10,20))


list1 = [1,2,3,4,5]

list1.append(6)
print(list1)
list1.extend([7,8,9,10])
print(list1)
list1.insert(2,100)
print(list1)
list1.remove(100)
print(list1)
list1.pop(2)
print(list1)
list1.clear()

list2 = [9,7,8,0,1,2,3,4,5]
aa=list2.index(7)
print(aa)
bb=list2.count(8)
print(bb)
list2.sort()
print(list2)
list2.reverse()
print(list2)

#栈
class stack:
    def __init__(self):
      self.stack = []

    def push(self,item):
       self.stack.append(item)
    def pop(self):
       if not self.is_empty():
          return self.stack.pop()
       else:
           raise IndexError("Stack is empty")
    def peek(self):
       if not self.is_empty():
          return self.stack[-1]
       else:
           raise IndexError("Stack is empty")
    def is_empty(self):
       return len(self.stack) == 0
    def size(self):
       return len(self.stack)

stack1 = stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
print(stack1.pop())
print(stack1.peek())
print(stack1.size())
print(stack1.is_empty())


from collections import deque
queue1   = deque()
queue1.append(10)
queue1.append(20)
queue1.append(30)

print("deque:",queue1)

first_element = queue1.popleft()
print("First element:",first_element)
print("deque:",queue1)

front_element = queue1[0]
print("Front element:",front_element)

is_empty = len(queue1) == 0
print("Is queue empty:",is_empty)

size =len(queue1)
print("Size of queue:",size)


class Queue:
   def __init__(self):
        self.items = []
   def enqueue(self, item):
       self.items.append(item)
   def dequeue(self):
       if not self.is_empty():
          return self.items.pop(0)
       else:
           raise IndexError("Queue is empty")
   def peek(self):
       if not self.is_empty():
          return self.items[0]
       else :   
            raise IndexError("Queue is empty")
       
   def is_empty(self):
       return len(self.items) == 0
   def size(self):
       return len(self.items)
   

queue2 = Queue()
queue2.enqueue(10)
queue2.enqueue(20)      
queue2.enqueue(30)


print("Queue:",queue2.items)

print("Dequeued element:",queue2.dequeue())
print("Queue:",queue2.items)

print("Front element:",queue2.peek())
print("Queue:",queue2.items)
print("Is queue empty:",queue2.is_empty())
print("Size of queue:",queue2.size())

vec = [1,2,3,4,5]
vec1=[x**2 for x in  vec]
print(vec1)

matrix = [[1,2,3,4],[4,5,6,7],[7,8,9,10]]
print(matrix)
[[row[i] for row in matrix] for i in range(4)]
print(matrix)