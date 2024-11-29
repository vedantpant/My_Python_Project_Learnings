# a, b, c =[int(x) for x in input("enter three numbers: ").split(',')]
# print(a, b, c, sep='-')
"""
import sys

dummy_file = sys.stdout

sample_input = ["hi", "my", "name", "is", "verdant"]

dummy_file = open('output.txt', 'w')

for i in sample_input:
    sys.stdout.write(i + "\n")
    dummy_file.write(i + "\n")
sys.stdout.close()

sys.stdout = dummy_file
"""
# from typing import List

"""
a = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(a)):
    print(a[i], end=' ')
"""

# print("08", "12", "1997", sep="-")
"""
print("verdant: %2f and just: %0.5f" % (2.0000, 0.563980))
print("%7.3o" % 25)
print("%10.3E" % 45.5678)
"""
'''
print('first number is {1} and second number is {0}'.format(1, 2))
print('i am learning python from {0} for {1}'.format('geeks', 'nerds'))
print(f"i love {'geeks'} for \"{'geeks'}!\"")
print(f'{"geeks"} and {"nerds"}')
'''
# print('I have learn {0} from {1} for {other}'.format("C++", "geeks", other="geeks"))

# data = dict(spunk="geeks", kpop="nerds")
# print('learning is for {spunk} but knowledge is for {kpop}'.format(**data))
"""
sent = "this is a string-alignment."
print("centre alignment for sent is: ")
print(sent.center(40, "#"))
print(sent.rjust(30, "-"))
print(sent.ljust(80, ">"))
"""

# a = 10
# b = 4
'''
add = a + b
sub = a - b
mul = a * b
div1 = a / b
div2 = a // b
mod = a % b
pow = a ** b
'''
# print("add:{}, sub:{}, mul:{}, div1(float):{}, div2(floor):{}, mod:{}, pow:{}".format(add, sub, mul, div1, div2, mod,
#                                                                                    pow))
# print("a>b: {},a<b: {},a==b: {},a<=b: {},a>=b: {},a!=b: {}".format(a>b, a<b,a==b, a<=b, a>=b, a!=b))
# print("a or b:{}, a and b:{}, not a:{}".format(a or b, a and b, not a))
# print("a & b:{}, a | b:{}, ~a:{}, a ^ b:{}, a>>:{}, a<<:{}".format(a & b, a | b, ~a, a ^ b, a >> 2, a << 5))
'''
a = b
print(b)

b += a
print(b)

b <<= a
print(b)

b *= a
print(b)
'''
'''
c = a
print(a is b)
print(a is c)
'''
'''
# program to find number in the list
x = [10, 12, 3, [], 45, 56, 78]
arr = [int(c) for c in input("enter the number: ").split()]
for i in x:
    if i in arr:
        print(i, end="\n")
'''
# a, b = 10, 20
# min =a if (a < b) else b
# print(min)

# print((b, a)[a < b])
# print({True: a, False: b}[a < b])
# print((lambda: a, lambda: b)[a < b]())

# print("both a and b are equal:" if a == b else "a is greater than b" if a > b else "b is greater")
# print(a, "a is greater b") if a > b else print(b, "b is greater than a")

# print("float division: {0}, float division: {1}, float division: {2}".format(2/2, 10/2, 13/5))
# print("integer division: {0}, integer division: {1}, integer division: {2}".format(2//2, 14//4, 15//8))

# overloading operator in python
'''
print(2 + 2)
print("geeks" + "\ngeeks")
print("geeks" + "e")
print("geeks" * 4)
'''

'''
class A:
    def __init__(self, a):
        self.a = a

    # adding two object
    def __add__(self, o):
        return self.a + o.a

obj1 = A(1)
obj2 = A(2)
obj3 = A("GEEKS")
obj4 = A("YES")

print(obj1 + obj2)
print(obj3 + obj4)
'''
'''
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b

obj1 = Complex(1, 2)
obj2 = Complex(2, 3)
obj3 = obj1 + obj2
print(obj3)
'''
'''
class Comparison:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a > other.a:
            return "first is greater"
        else:
            return "second is greater"

    def __lt__(self, other):
        if self.a < other.a:
            return "first is less"
        else:
            return "second is less"

    def __eq__(self, other):
        if self.a == other.a:
            return "both are equal"
        else:
            return "both are not equal"


obj1 = Comparison(4)
obj2 = Comparison(4)

# print(obj1 > obj2)
# print(obj1 < obj2)
# print(obj1 == obj2)
'''

# print(any([False, False, False, False]))
# print(all([True, True, True, True]))

'''
list1 = []
list2 = []

for i in range(1, 11):
    list1.append(4*i)

for i in range(0, 10):
    list2.append(list1[i] % 5 == 0)

print("check weather any of the number is divisible by 5 ->\n")
print(any(list2))
'''
'''
list1 = []
list2 = []

for i in range(1, 21):
    list1.append(4*i-3)

for i in range(0, 20):
    list2.append(list1[i] % 2 == 1)

print("weather all the elements in the list are odd -> ")
print(all(list2))
'''
# import operator

'''
print("addition of two number is :", end=" ")
print(operator.add(2, 4))

print("subtraction of two number is :", end=" ")
print(operator.sub(4, 3))

print("multiplication of two number is :", end=" ")
print(operator.mul(4, 3))

a = 8
b = 5

if a < b:
    print("less than: ", operator.lt(a, b), end=" ")
elif a > b:
    print("greater than: ", operator.gt(a, b), end=" ")
'''
'''
list1 = [2, 5, 6, 8, 9, 10]

print("elements are as follows: ", end="")
for i in range(len(list1)):
    print(list1[i], end=' ')

print("\r")
operator.setitem(list1, slice(0, 2), [1, 2, 3])

print("modified list:", end=' ')

for i in range(len(list1)):
    print(list1[i], end=' ')

print("\r")

operator.delitem(list1, slice(3, 5))

print("second time modified list:", end=' ')
for i in range(len(list1)):
    print(list1[i], end=' ')

print("\r")

operator.getitem(list1, 4)

print("get the item:", end=' ')
print(operator.getitem(list1, slice(0, 3)), end=' ')
'''
'''
s1 = 'geeksfor'
s2 = 'geeks'

print(operator.contains(s1, s2))
print("concatinated string is:", operator.concat(s1, s2), end=' ')
'''
'''
list1 = [1, 2, 4, 5, 6, 7]
list2 = [3, 4, 5, 6, 7, 9]
for item in list1 and list2:
    if item not in list1 and list2:
        print("non-overlapping items: ", item)
'''
'''
x = 5
if type(x) is not int:
    print("x is not an integer")
else:
    print("x is an integer")
'''

# a = '''this is a string'''
# print(a)
'''
l = ["a", 1, "ass-whip", 1+2]
print(l)
l.append(6)
print(l)
print(l.pop(l[1]))
'''
'''
t = (3, 4, 5, 6, 7, 'animal', "a")
print(t[1])
'''
'''
i = 0
while i < 10:
    i += 1
    print(i)
'''
'''
s = 'this is a string'
for i in s:
    print(i)
'''
'''
for i in range(0, 10):
    print(i)
'''
'''
s = 'this 
        is
        life'
print(s)
'''
# str = "writing a string to access"
# print("initial string: ", str)
# print(str[::-1])
# str = "".join(reversed(str))
# print(str)

# print(str[3:-4])

# list = list(str)
# print("\nstring as list: ", list)
# list[2] = 'o'
# string = "".join(list)
# string1 = str[0:2] + 'p' + str[3:]
# print("\nupdated string: ", string1)

# string1 = str[0:2] + str[3:]
# print("\nupdated string: ", string1)
# string1 = str
# del string1
# print("\n deleting the entire string: ")
# print(string1)

# str = 'I\'m a "GEEK"'
# print(str)
# str = 'hello\ngeeks'
# print(str)

# str = r'this is something: \110\145\134\157\123'
# print("string in octal : ", str)

# print("string output: {b} {a} {c}".format(a="geeks", b="for", c="geeks"))
# print("{0:2f}".format(1/6))

# print("|{:<10}|{:^10}|{:>10}|".format("geeks", "geeks", "geeks"))
# print("{0:^16} was founded in {1:<4}!".format('geeksforgeeks', 2009))
# i = 10.345667
# print("integer value : %2.3f" %i)

# var = [10, 20, "harry", ("is", "not"), "good"]
# print(var[3][1])
# print(var[-2][0])
# print(len(var))
'''
var = input("enter the separated string:\n")
print("separated string:\n")

lst = var.split()
print("string as list:\n")
print(list(lst))
'''
'''
n = int(input("enter the number in the list:\n"))

lst = list(map(int, input("enter the integer:").strip().split()))[:n]
print("list :\n", lst)
'''
'''
lst = []
for i in range(1, 4):
    lst.append(i)

print(lst)

list1 = ("hello", "nerd")
lst.append(list1)
print("appended list:\n", lst)
lst.insert(3, 12)
lst.insert(0, "hello")
print(lst)
list2 = ["geeks", "hello", "name", 4]
lst.extend(list2)
print(lst)
lst.reverse()
print("reversed list:\n", lst)
lst.remove(2)
print(lst)
'''
'''
list1 = [1, 3, 4, 5, 4, 6, 7, 7, 8, 76, 5, 54]
for i in list1:
    if i % 2 == 0:
        list1.remove(i)
print(list1)
list1.pop(2)
print(list1)
'''
'''
list1 = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(list1)
'''
'''
list1 = []
for i in range(1, 11):
    if i % 2 == 1:
        list1.append(i ** 2)
print(list1)
'''

# Tuples = (12, 3, 44, 5, 5, 66, 7, 7878, 78)
# print(Tuples)
'''
list1 = [1, 23, 45, 6]
print(tuple(list1))
tuple1 = tuple('geeks')
print(tuple1)
'''
'''
tuple1 = (12, 'geeks', "nerds")
tuple2 = ('geek', "love")
tuple3 = (tuple1, tuple2)
print(tuple3)
'''
'''
tuple1 = ('Geeks ') * 3
print(tuple1)
'''
'''
tuple1 = ('geeks',)
n = 5
for i in range(int(n)):
    tuple1 = (tuple1,)
    print(tuple1)
'''
'''
tuple1 = tuple('geeks')
print("print the element of the tuple:\n", tuple1[1])
'''
'''
tuple1 = ("geeks", "for", "geeks")
a, b, c = tuple(tuple1)
print(a)
print(b)
print(c)
'''
'''
tuple1 = tuple("geeksforgeeks")
print(tuple1[::-1])
'''
'''
tuple1 = ("geeks", "for", "geeks")
del tuple1
print(tuple1)
'''
# set1 = set()
# print("empty set:\n", set1)
# set1 = set("geeksforgeeks")
# print(set1)
# string1 = 'geeksforgeeks'
# set1 = set(string1)
# print(set1)

# set1 = set(["geeks", "for", "geeks"])
# print(set1)
# set1 = set([12, 3, 34, 4, 5, 55, 66, 89, 4])
# print(set1)
# set1 = set(["geeks", 2, 3, 4, 2, 3, 4, 56, 7, 7, 8, "geeks", "for"])
# print(set1)
# my_set = {1, 2, 3, 4, 5, 6, 7, 63, 343, 42, 3, 32, 322, 'geeks', 'for', 'geeks'}
# print(my_set)

# set1 = set()
# print("blank set:\n", set1)
# set1.add(7)
# set1.add(2)
# set1.add((6, 7, 8))
# print(set1)
'''
set1 = set()
for i in range(1, 5):
    set1.add(i)

print("print elements from 1 to 5:\n", set1)
'''
'''
set1 = set([5, 6, 7, 8, (5, 6, 7)])
print("set:\n", set1)
set1.update([3, 4, 5])
print("updated set:\n", set1)
'''
'''
set1 = set()
print("blank set:\n", set1)
set1.update([4, 5, 6, 77, 7, 8, 'geeks', "for"])
print("updated set:\n", set1)
print("accessing elements of the set:\n")
for i in set1:
    print(i, end=" ")

print("\n")
print("geeks" in set1)
'''
'''
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
print("set:\n", set1)
set1.remove(5)
set1.remove(6)
print("set remove:\n", set1)
print("\n")

set1.discard(8)
set1.discard(9)
print("set updated:\n", set1)
print("\n")

for i in range(1, 5):
    set1.remove(i)

print(set1)
'''
'''
set1 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
set1.pop()
print("set1:\n", set1)
set1.clear()
print(set1)
'''
'''
string1 = ('g', 'e', 'e', 'k', 's', 'f', 'o', 'r')
fset1 = frozenset(string1)
print("frozen sets:\n", fset1)
print("empty frozen set:\n", frozenset())
'''
'''
my_list = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("my list as set:\n", my_list)
my_string = set("geeksforgeeks")
print("string as set:\n", my_string)
my_dict = set({1: "geeks", 2: "for", 3: "geeks"})
print("dictionary as set:\n", my_dict)
'''
# Dictionary
# dict = {1: "Vedant", 2: "can", 3: "do", 4: "it"}
# print("\ndictionary with use of keywords:", dict)
# name = ["vedant", "bhavay", "swappi"]
# dict = {"hello": name[1], 2: {1: "is", 2: "doing", 3: "well"}}
# print(dict)
# dict= {}
# print("empty dictionary:\n", dict)
# Dict = dict({1: "vedant", 2: "is", 3: "not"})
# print(Dict)
# Dict = dict([(1, "geeks"), (2, "for")])
# print(Dict[2])
# Dict = {1: "vedant", 2: "is", 3: {1: "not", 2: "in", 3: "good"}}
# print(Dict[1], Dict[2], Dict[3])
'''
dict = {}
print("empty dictionary:\n", dict)
dict[1] = "Vedant"
dict[0] = "is"
dict[2] = "good"
print(dict)
dict["hell"] = 2, 3, 4
print(dict)
dict[2] = "hello"
print(dict)
dict[5] = {"Nested": {1: "yo", 2: "this", 3: "is", 4: "not"}}
print(dict[5]["Nested"][1])
print(dict.get(2))
'''
'''
dict1 = {1: 'geeks', 2: 'for', 3: 'geeks', 4: "says", 5: "hello"}
dict2= dict1.copy()
print(dict2)

dict1.clear()
print(dict1)

print(dict2.get(1))
print(dict2.items())
print(dict2.keys())

dict2.pop(4)
print(dict2)

dict2.popitem()
print(dict2)

dict2.update({3: "scala"})
print(dict2)

print(dict2.values())
'''

# import array as arr
'''
a = arr.array('i', [1, 2, 3, 4])
print("the new array: ", end=' ')

for i in range(0, 4):
    print(a[i], end=" ")

print("\n")

a.insert(1, 3)
print("the new array after insertion: ", end=' ')

for i in range(0, 4):
    print(a[i], end=" ")

print("\n")

a = arr.array('d', [2.3, 5.7, 6.7])
print("the decimal data type array: ", end=' ')

for i in range(0, 3):
    print(a[i], end=',')

print('\n')

a.append(8.9)

print("the decimal data type array after insertion: ", end=' ')

for i in range(0, 4):
    print(a[i], end=' ')
'''
'''
a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8])

print("accessing the element: ", a[1])

b = arr.array('d', [1.8, 2, 3.7, 4.1, 5.2, 6.0, 7.5, 8.6, 9.9])
print("accessing decimal elements: ", b[1])
'''
'''
a = arr.array("i", [1, 2, 3, 4, 5, 6])
print("accessing elements: ", end=" ")

for i in range(0, 6):
    print(a[i], end=" ")
print("\n")

a.pop(a[1])

print("accessing elements after popping: ", end=" ")

for i in range(0, 5):
    print(a[i], end=" ")
print("\n")

a.remove(2)

print("accessing elements after removing: ", end=" ")

for i in range(0, 4):
    print(a[i], end=" ")
print("\n")
'''
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = arr.array("i", l)
print("element of the array:\n")
for i in a:
    print(i, end=" ")
print("\n")

sliced_array = a[3:6]
print(sliced_array)

print(a.index(2))

a[5] = 45

print("element of the array after updating:\n")
for i in a:
    print(i, end=" ")
print("\n")
'''
'''
i = 20

if i < 15:
    print("less than 15")
else:
    print("greater than 15")
print("exit from condition")
'''
'''
def digitsum(n):
    digisum = 0
    for ele in str(n):
        digisum += int(ele)
    return digisum

list1 = [1232, 34435, 555, 56, 5656, 56, 888, 42265]
x = [digitsum(i) for i in list1 if i & 1]
print(x)
'''
'''
x = 10

print(5 < x < 15)
print(6 < x < x*10 < 100)
'''
'''
list1 = ["geeks", "for", "geeks"]
for i in list1:
    print(i, end=' ')
'''
'''
print("iterable dictionary")
d = dict()
d['xyz'] = 123
d['abc'] = 456
for i in d:
    print("%s %d" % (i, d[i]))
'''
'''
print("iteration of string")
s = "geeksforgeeks"
for i in s:
    pass
print(i, end=" ")
'''
'''
sum = 0
for i in range(10):
    sum += i
print("print the sum of 10 numbers:", sum)
'''
'''
for i in range(0, 4):
    print(i)
# out of loop because no break is there
else:
    print("no break")
'''
# i = 10
# print(True) if i < 15 else print(False)
'''
count = 0
while count < 3:
    print(count)
    count+=1
'''
'''
list1 = [1, 2, 3, 4]
while list1:
    print(list1.pop())
'''
# i = 0
# a = "geeksforgeeks"
'''
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('current letter:', a[i])
    i+=1
'''
'''
while i < len(a):
    i+=1
    pass
print("count of i:",i)
'''
'''
i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("break out of loop")
'''
'''
a = int(input("enter value to exit the loop (-1)\n:"))

while a != -1:
    a = int(input("enter value to exit the loop (-1)\n:"))
'''
'''
for i in range(10):
    if i == 2:
        break
    print(i)
print(i)
'''
'''
s = 'geeksforgeeks'
for i in s:
    print(i)
    if i == 'e' or i == 's':
        break
print("out of for loop", i)

i = 0
while True:
    print(s[i])
    if s[i] == 'e' or s[i] == 's':
        break
    i += 1
print("out of while loop")
'''
'''
num = 0
for i in range(10):
    num += 1
    if num == 8:
        break
    print("num has value: ", num)
print("out of loop")
'''
'''
s = 'geeksforgeeks'
for i in s:
    if i == 'e':
        continue
    print(i)
'''
'''
for i in range(1, 11):
    if i == 6:
        continue
    print(i, end=' ')
'''
'''
def func():
    pass

a = 10
b = 20

if a < b:
    pass
else:
    print("a is greater than b")
'''
'''
li = ['a', 'b', 'c', 'd']

for i in li:
    if i == 'a':
        pass
    else:
        print(i)
'''
'''
for keys, values in enumerate(['geeks', 'for', 'geeks', 'is', 'best', 'coding', 'platform']):
    print(values, end=" ")
'''
'''
questions = ["fruit", "color", "name"]
answers = ['orange', 'red', 'vedant']

for question, answer in zip(questions, answers):
    print("what is your favourite {0}?: answer:{1}".format(question, answer))
'''
'''
king = {'chandragupta': 'the maurya', "ashoka": "the great", "modi": "the distortionist"}

for key, value in king.items():
    print(key, value)
'''
'''
li = [1, 2, 3, 4, 66, 7, 89, 76, 5, 6, 6, 7, 8, 9, 6, 4, 2, 4, 3, 6, 8, 9, 10]

print("list is in sorted order:")
for i in sorted(li):
    print(i, end=' ')

print('\r')

print("list is in sorted order without duplicates:")
for i in sorted(set(li)):
    print(i, end=" ")
'''
'''
fruits = ['guave', 'guava', 'apple', 'pear', 'banana', 'orange']

for i in sorted(set(fruits)):
    print(i, end=' ')
'''
'''
li = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 7, 8, 9, 10]
print("the list is in reversed order: ")
for i in reversed(li):
    print(i, end=" ")
'''
'''
for i in reversed(range(1, 10, 3)):
    print(i, end=' ')
'''
'''
# function
def fun():
    print("hey yo sup!!")

fun()
'''
'''
def sum_of_two_number(num1, num2):
    num3 = num1 + num2
    return num3

num1, num2 = 1, 4
print(sum_of_two_number(num1, num2))
'''
'''
def is_prime(n):
    if n in [2, 3]:
        return True
    if n == 1 and n % 2 == 0:
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True

print(is_prime(56), is_prime(79))
'''
'''
def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(34)
'''
'''
def num(x, y=80):
    print("x: ", x)
    print("y: ", y)

num(34)
'''
'''
def name(firstname, lastname):
    print(firstname, lastname)

name(firstname="geeks", lastname="practice")
name(lastname='pant', firstname='vedant')
'''
'''
def myfunc(*args):
    for arg in args:
        print(arg)

myfunc('hello', 'welcome', 'to', 'geeks')
'''
'''
def my_func(**kwargs):
    for key, item in kwargs.items():
        print("%s == %s" % (key, item))

my_func(first="geeks", second='for', third='geeks')
'''
'''
def evenodd(x):
    """print weather the number is odd or even"""
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

print(evenodd.__doc__)
evenodd(7)
'''
'''
def square_value(x):
    """This function return the squared value of the number"""
    return x**2

print(square_value.__doc__)
y = int(input("enter the number to be squared: "))
print("square of the number is: ", square_value(y))
'''
'''
def my_func(x):
    x = 20

x = 10
my_func(x)
print("new list is: ", x)
'''
'''
def swap(x, y):
    temp = x
    x = y
    y = temp

x, y = 2, 3
swap(x, y)
print(x, y)
'''
'''
def cube(x):
    return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(3))
print(cube_v2(4))
'''
'''
def f1():
    s = "i love geeksforgeeks"

    def f2():
        print(s)

    f2()

f1()
'''
'''
def myfun(*args):
    for arg in args:
        print(arg)

myfun("hello", 'it', 'is', "geeksforgeeks")
'''
'''
def my_func(argw, *args):
    print("first arg is: ", argw)
    for arg in args:
        print("another argument through *args is: ", arg)

my_func("I", "love", "geeks for geeks", "a lot")
'''
'''
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
'''
'''
def myFun(arg1, **kwargs):
    print("for first argument: ", arg1)
    for key, item in kwargs.items():
        print("%s==%s" % (key, item))

myFun("hello", first="geeks", mid="for", last="geeks")
'''
'''
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ["vedant", "is", "awesome"]
myFun(*args)
print("\r")
kwargs = {"arg1": "geeks", "arg2": "for", "arg3": "geeks"}
myFun(**kwargs)
'''
'''
def myFun(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

myFun("hello", "fans", "of", first="geeks", mid="for", last='geeks')
'''
'''
class car:
    def __init__(self, *args):
        self.speed = args[0]
        self.color = args[1]

audi = car(500, "red")
bmw = car(350, "white")
maruti_suzuki = car(150, "black")

print(audi.color)
print(maruti_suzuki.speed)
'''
'''
class car:
    def __init__(self, **kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']
        self.engine = kwargs['e']

Audi = car(s=500, c='black', e=6.6)
BMW = car(s=600, c='red', e=7.9)
bugatti = car(s=700, c='black', e=16.0)

print(Audi.speed)
print(BMW.engine)
print(bugatti.color)
'''
'''
def SimpleGeneratorFunction():
    yield 1
    yield 2
    yield 3

for i in SimpleGeneratorFunction():
    print(i)
'''
'''
def nxtSqr():
    i = 1
    while True:
        yield i*i
        i += 1

for num in nxtSqr():
    if num > 100:
        break
    print(num)
'''
'''
def MyGeneratorNumber():
    yield 1
    yield 2
    yield 3

x = MyGeneratorNumber()

print(next(x))
print(next(x))
print(next(x))
'''
'''
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for i in fib(5):
    print(i)
'''
'''
calc = lambda num: "even number" if num % 2 == 0 else "odd number"

print(calc(2))
'''
'''
str1 = "geeksforgeeks"

print(lambda string: str1)
'''
'''
filter_num = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_num:", filter_num("geeks101"))

do_exclaim = lambda s: s + "!"
print("do_exclaim:", do_exclaim("i am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum:", find_sum(230))
'''
'''
lst1 = ["1", "5", "7", "48", "59", "-61", "-27", "38", "69", "-11"]
print("sorted list numerically:", sorted(lst1, key=lambda x: int(x)))

print("filtered positive and even numbers:",
      list(filter(lambda x: (int(x) % 2 == 0 and int(x) > 0), lst1)))

print("operating on each item using lambda and map():",
      list(map(lambda x: str(int(x) + 10), lst1)))
'''
'''
def f1():
    global s
    s += "GFG"
    print(s)
    s = "looks for geeksforgeeks python section"
    print(s)

s = "python is great"
f1()
print(s)
'''
'''
a = 1

def f():
    print('inside f(): ', a)

def g():
    a = 2
    print('inside g(): ', a)

def h():
    global a
    a = 3
    print("inside h(): ", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
'''
'''
a = 10
b = 15

def add():
    c = a + b
    print(c)

add()
'''
'''
a = 15

def change():
    global a
    b = a + 5
    a = b
    print(a)

change()
'''
'''
x = 15

def change():
    global x
    x = x + 5
    print("value of x inside a function:", x)

change()
print("value of x outside a function", x)
'''
'''
arr = [10, 20, 30]

def fun():
    global arr
    arr = [20, 30, 40]

print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)
'''
'''
def add():
    x = 15
    def change():
        global x
        x = 20
    print('before changing x:', x)
    print("making change")
    change()
    print("after making changes:", x)

add()
print("value of x:", x)
'''
'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # storing the function in a variable
    greeting = func("""HI, I created a function by a function passed as an argument""")
    print(greeting)

yell = shout

print(yell("hello"))

greet(shout)
greet(whisper)
'''
'''
def create_adder(x):
    def adder(y):
        return x + y

    return adder

add_15 = create_adder(15)

print(add_15(10))
'''
'''
def outerFunction(text):
    def innerFunction():
        print(text)

    return innerFunction


if __name__ == '__main__':
    my_function = outerFunction('hey!')
    my_function()
'''
'''
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

yell = shout

def greet(func):
    # storing the function in a variable
    greeting = func("""I am a function created as an argument.""")
    print(greeting)

print(yell("hello!"))

greet(shout)
greet(whisper)
'''
'''
def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)

print(add_15(10))
'''
'''
def hello_decorator(func):

    def inner1():
        print("hello this is before function is executed")

        func()

        print("this is after wrapper function is called")

    return inner1

def func_to_be_used():
    print("this is inside the function!!")

function_to_be_used = hello_decorator(func_to_be_used)

function_to_be_used()
'''
'''
import math
import time

# decorator to calculate duration taken by any function

def calculate_time(func):

    def inner1(*args, **kwargs):

        begin = time.time()

        func(*args, **kwargs)

        end = time.time()

        print("total time taken taken in:", func.__name__, end - begin)

    return inner1

@calculate_time
def factorial(num):

    time.sleep(2)

    print(math.factorial(num))

factorial(5)
'''
'''
def hello_decorator(func):
    def inner1(*args, **kwargs):

        print("before execution")

        return_value = func(*args, **kwargs)

        print("after execution")

        return return_value

    return inner1

@hello_decorator

def sum_of_two_number(a, b):
    print("inside function")

    return a + b

a, b = 1, 2
print("the sum of two number is:", sum_of_two_number)
'''
'''
def decor1(func):
    def square():
        x = func()
        return x * x
    return square

def decor(func):
    def twice():
        x = func()
        return 2 * x
    return twice

@decor1
@decor
def num():
    return 10

print(num())
'''
'''
def decorator_fun(func):
    print("inside the decorator")

    def inner(*args, **kwargs):
        print("inside inner function")
        print("decorated the function")

        func()

    return inner

@decorator_fun
def funct_to():
    print("inside actual function")

funct_to()
'''
'''
friends = ['vedant', "bhavya", "swappi", 'mayank']
for friend in friends:
    print("hey " + friend)
'''
'''
def decorator(*args, **kwargs):
    print("inside the decorator")

    def inner(func):
        print("inside the function")
        print("i like ", kwargs['like'])

        func()
        
    return inner

@decorator(like='geeksforgeeks')
def my_func():
    print("inside actual func")
'''
'''
for i in range(10):
    print("hello world")
'''
'''
def decorator_fun(x, y):
    def Inner(func):

        def wrapper(*args, **kwargs):
            print("I like geeksforgeeks")
            print("Summation of number is {}.".format(x + y))

            func(*args, **kwargs)
        return wrapper
    return Inner

def my_func(*args):
    for ele in args:
        print(ele)

decorator_fun(12, 15)(my_func)('geeks', 'for', 'geeks')
'''
'''
def decodecorator(dataType, message1, message2):
    def decorator(fun):
        print(message1)

        def wrapper(*args, **kwargs):
            print(message2)
            if all([type(arg) == dataType for arg in args]):
                return fun(*args, **kwargs)
            return "Invalid Input"

        return wrapper

    return decorator


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def stringJoin(*args):
    st = ''
    for i in args:
        st += i
    return st


@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
    summ = 0
    for arg in args:
        summ += arg
    return summ


print(stringJoin("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))
'''
'''
def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)

print(fact(5))
'''
'''
memory = {}

def memo_fact(f):

    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print("result saved in memory")
        else:
            print("returning from saved memory")
        return memory[num]

    return inner

@memo_fact
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num - 1)

print(facto(5))
'''
'''
def lucky_number(name):
    number = len(name) * 9
    print("the lucky number of {0}: {1}".format(name, number))

lucky_number("jay")
lucky_number("vedant")
'''
'''
def attempt(n):
    x = 1
    while x <= n:
        print("attempt:", str(x))
        x += 1
    print("done")

attempt(5)
'''
'''
def count_down(n):
    while n >= 0:
        print("count:", n)
        n -= 1
    print("boom!!")

count_down(5)
'''
'''
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()
'''
'''
teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + "vs" + away_team)
    print()
'''
'''
for x in range(1, 10, 3):
    print(x)
'''
'''
for x in range(10):
    for y in range(x):
        print(y)
'''
'''
def votes(params):
	for vote in params:
	    print("Possible option:" + vote)

votes(["yes","no","maybe"])
'''
'''
class Dog:

    attr1 = "mammal"
    atrr2 = "dog"

    def fun(self):
        print("I am a ", self.attr1)
        print("I am a ", self.atrr2)

Rogder = Dog()

print(Rogder.attr1)
Rogder.fun()
'''
'''
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello my name is",self.name)

p = Person("Nikhil")
p.say_hi()
'''
'''
class Pokemon:

    Category = "Pokemon"

    def __init__(self, type, level):
        self.type = type
        self.level = level

Bulbasaur = Pokemon("Grass", 16)
Charizard = Pokemon("Fire", 35)

print("Bulbasaur Details: ")
print("Balbasaur:", Bulbasaur.Category)
print("Balbasaur Type:", Bulbasaur.type)
print("Balbasaur level:", Bulbasaur.level)

print("\n")

print("Charizard Details: ")
print("Charizard:", Charizard.Category)
print("Charizard Type:", Charizard.type)
print("Charizard level:", Charizard.level)
'''
'''
list1 = ["orange", "mango", "banana", "pineapple"]
list1.insert(0, "kiwi")
print(list1)
'''
'''
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds - hours * 3600) // 60
    seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, seconds

result = convert_seconds(5000)
print(type(result))
print(result)
'''
'''
animals = ["lion", "tiger", "zebra", "octopus"]
chars = 0
for animal in animals:
    chars += len(animal)

print("total character : {}, average character: {}".format(chars, chars/len(animal)))
'''
'''
winners = ["ashley","dylan","harley"]
for index, winner in enumerate(winners):
    print("{} - {}".format(index+1, winner))
'''
'''
def email_add(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(email,name))
    return result

print(email_add([("vedantpant@gmail.com", "vedant pant"),("bhavaychaudhary@gmail.com", "bhavay chaudhary")]))
''"
multiples = []
for multiple in range(1,70):
    if multiple % 7 == 0:
        multiples.append(multiple)

print("multiples of 7 are:", multiples)
'''
'''
file_count = {"jpg": 10, "txt": 3, "pdf": 2, "csv":4}
file_count["py"] = 3
file_count["pdf"] = 13
# del file_count["jpg"]
print(file_count)
for key,value in file_count.items():
    print("there are {} amount of files of .{} extension".format(value, key))
'''
'''
def letter_count(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(letter_count("hello vedant how are you?"))
'''
'''
def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
'''
'''
def groups_per_user(group_dictionary):
	user_groups = {}
	for group, users in group_dictionary.items():
		for user in users:
			user_groups[user] = user_groups.get(user,[]) + [group]
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
'''

"""The format_address function separates out parts of the address string into new strings: 
house_number and street_name, and returns: "house number X on street named Y". The format of the input string is: numeric house number, 
followed by the street name which may contain numbers, but never by themselves, and could be several words long. 
For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.
"""
'''
def format_address(address_string):
	# Declare variables
	house_number = ""
	street_name = ""
	# Separate the address string into parts
	address_string = address_string.split()
	# Traverse through the address parts
	for parts in address_string:
	# Determine if the address part is the
	# house number or part of the street name
		if parts.isdigit():
			house_number += parts
	# Does anything else need to be done
	# before returning the result?
		else:
			street_name += parts
			street_name += " "
	# Return the formatted string
	return "house number {} on street named {}".format(house_number,street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"
'''
'''
def highlight_word(sentence, word):
	return (sentence.replace(word, word.upper()) if word in sentence else sentence)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
'''
'''
def combine_lists(list1, list2):
	new_list = []
	new_list = Drews_list + Jamies_list[::-1]
	return new_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
'''
'''
class Person:

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("hello my name is:", self.name)

p = Person('Vedant')
p.say_hi()
'''
# print(dir())
# print(help())
'''
class apple:
    flavour = ""
    color = ""

fruit = apple()

fruit.color = "green"
fruit.flavour = "sour"

print(fruit.color)
print(fruit.flavour.upper())

vegetable = apple()
vegetable.color = "red"
vegetable.flavour = "sweet"

print(vegetable.color)
print(vegetable.flavour)
'''
'''
class piglet:
    name = "vedant"
    def speak(self):
        print("hi my name is {}, oink!.".format(self.name))

hamlet = piglet()
hamlet.name = "striver"
hamlet.speak()
'''
'''
class Apple:

    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "this apple is {} in color and is {} in flavor".format(self.color,self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)
'''
# print("hello world")
'''
for i in range(2):
    print("hello world")
'''
'''
def to_sec(hours, minutes ,seconds):
    """this function converts in to seconds the given hours, minute and seconds"""
    return hours*3600 + minutes*60 + seconds

print(to_sec(3,5,70))
'''
'''
class Fruit:
    def __init__(self, flavor, taste):
        self.flavor = flavor
        self.taste = taste

class Apple(Fruit):
    pass

class Grape(Fruit):
    pass

about_apple = Apple("tangy", "good")
about_grape = Grape("sour", "okay")

print(about_grape.flavor)
print(about_apple.taste)
'''
'''
class Animal:
    sound = ""
    def __init__(self, name):
        self. name = name

    def speak(self):
        print("{sound} sound is made by {name}".format(sound=self.sound, name=self.name))

class Piglet(Animal):
    sound = "oink"

hamlet = Piglet("Hamlet")
hamlet.speak()

class Cow(Animal):
    sound = "moo"

gretchel = Cow("Gretchel")
gretchel.speak()
'''
'''
class Repository:
    def __init__(self):
        self.package = {}

    def add_package(self,package):
        self.package[package.name] = package

    def package_size(self):
        result = 0\]
        for package in self.packages.values():
            result += package.size
        return result
'''
'''
class GeeksforGeeks:

    def __init__(self):
        self.geek = "geeksforgeeks"

    def print_Geek(self):
        print(self.geek)

obj = GeeksforGeeks()

obj.print_Geek()
'''
'''
class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("first number = " + str(self.first))
        print("second number = " + str(self.second))
        print("addition of two number = " + str(self.answer))

    def calculation(self):
        self.answer = self.first + self.second

obj1 = Addition(1000, 2000)

obj2 = Addition(2, 3)

obj1.calculation()

obj2.calculation()

obj1.display()

obj2.display()
'''
'''
import datetime
now = datetime.datetime.now()
print(type(now))
print(now.year)
print(now + datetime.timedelta(days = 28))
'''
'''
list = [1, 2, 3, 4, 5]
list.sort(reverse=True)
print(list)
'''
'''
name = ["Carlos", "Vedant", "Bhavay", "Swapnil", "Ray", "Mike", "Ben"]
name.sort(key=len)
print(name)
'''
'''
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine,users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
    def __init__(self, event_date,event_type,machine_name,user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users= current_users(events)
print(users)
'''
'''
class Employee:

    #initializing
    def __init__(self):
        print("employee created.")

    #deleting (calling destructor)
    def __del__(self):
        print("destructor called, employee deleted.")

obj = Employee()
del obj
'''
'''
class Employee:

    # Initialization
    def __init__(self):
        print("employee created")

    # caling destructor
    def __del__(self):
        print("destructor created")

def Create_obj():
    print("Making object...")
    obj = Employee()
    print("function end...")
    return obj

print("Calling Create obj() function")
obj = Create_obj()
print("program end....")
'''
'''
class A:
    def __init__(self,bb):
        self.b = bb

class B:
    def __init__(self):
        self.a = A(self)
    def __del__(self):
        print("die")

def fun():
    b = B()

fun()
'''
'''
class RecursiveFunction:
    def __init__(self,n):
        self.n = n
        print("Recursive Function initialized with n:", n)

    def run(self, n = None):
        if n is None:
            n = self.n
        if n <= 0:
            return
        print("running recursive function with n =", n)
        self.run(n-1)

    def __del__(self):
        print("Recursive function object destroyed")

obj = RecursiveFunction(5)

obj.run()

del obj
'''
'''
class Person(object):

    # constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # to check if person is an employee
    def Display(self):
        print(self.name, self.id)

emp = Person("satyam", 103)

emp.Display()

class Employee(Person):

    def print(self):
        print("Employee class called")

Emp_details = Employee("Vedant", 23092)

Emp_details.Display()

Emp_details.print()
'''
'''
class Person(object):

    # constructor
    def __init__(self,name, idNumber):
        self.name = name
        self.idNumber = idNumber

    # to get name
    def Display(self):
        print(self.name, self.idNumber)

    #to check if this person is an employee
    def isEmployee(self):
        return False

class Employee(Person):

    def __init__(self, name, idNumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init of parent class
        Person.__init__(self, name, idNumber)

    # here we return True
    def isEmployee(self):
        return True


# emp = Person("geek1")
# print(emp.getname(), emp.isEmployee())

emp = Employee("geek2", 923005, 200000, "Intern")
emp.Display()
emp.isEmployee()
'''
'''
class Base_1:
    def __init__(self):
        self.str1 = "geek1"
        print("Base1")

class Base_2:
    def __init__(self):
        self.str2 = "geek2"
        print("Base2")

class Derived(Base_1, Base_2):
    def __init__(self):
        Base_1.__init__(self)
        Base_2.__init__(self)
        print("derived")

    def printStrs(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStrs()
'''
'''
class Base(object):
    def __init__(self, name, isPermitted):
        self.name = name
        self.__isPermitted = True

    def getName(self):
        return self.name

class Child(Base):
    def __init__(self, name, age, isPermitted):
        self.age = age
        Base.__init__(self, name, isPermitted=True)

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self, name, age, adress, isPermitted):
        self.adress = adress
        Child.__init__(self, name, age, isPermitted=True)

    def getAdress(self):
        return self.adress

gc = GrandChild("vedant", 25, 'Noida', isPermitted=True)
print(gc.isPermited)
'''
'''
class Parent:
    def func1(self):
        print("this function is in parent class")

class Child(Parent):
    def func2(self):
        print("this function is in child class")

obj1 = Child()
obj1.func1()
obj1.func2()
'''
'''
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

class Son(Mother, Father):
    def parent(self):
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)

s1 = Son()
s1.mothername = "Divya"
s1.fathername = "Manish"
s1.parent()
'''
'''
class Grandfather(object):

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Father(Grandfather):

    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Grandfather.__init__(self, grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername,grandfathername)

    def print_name(self):
        print("Grandfather name: ", self.grandfathername)
        print("Father name: ", self.fathername)
        print("Son name: ", self.sonname)

s1 = Son('Hariom', 'Vedant', 'Manish')
print(s1.grandfathername)
s1.print_name()
'''
'''
class School:
    def func1(self):
        print("this function is in school")

class Student1(School):
    def func2(self):
        print("this function is in student 1")

class Student2(School):
    def func3(self):
        print("this function is in student 2")

class Student3(Student1, School):
    def func4(self):
        print("this function is in student 3")

object = Student3()
object.func1()
object.func2()
'''
