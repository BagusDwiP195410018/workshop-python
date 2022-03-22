#!/usr/bin/env python
# coding: utf-8

# In[1]:


def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope:", spam)


# In[2]:


class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>


# In[3]:


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'


# In[4]:


def __init__(self):
    self.data = []


# In[5]:


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i


# In[6]:


x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


# In[7]:


x.f()


# In[8]:


xf = x.f
while True:
    print(xf())


# In[9]:


class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name
d = Dog('Fido')
e = Dog('Buddy')
d.kind


# In[10]:


e.kind


# In[11]:


d.name


# In[12]:


e.name


# In[13]:


class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks


# In[14]:


class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks


# In[15]:


e.tricks


# In[16]:


class Warehouse:
    purpose = 'storage'
    region = 'west'
w1 = Warehouse()
print(w1.purpose, w1.region)


# In[17]:


w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)


# In[18]:


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)
class C:
    f = f1
    def g(self):
        return 'hello world'
    h = g


# In[19]:


class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append(x)
    def addtwice(self, x):
        self.add(x)
        self.add(x)


# In[20]:


class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>


# In[21]:


class DerivedClassName(modname.BaseClassName):


# In[22]:


class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>


# In[23]:


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    __update = update
class MappingSubclass(Mapping):
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)


# In[24]:


class Employee:
    pass
john = Employee()
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000


# In[25]:


for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')


# In[26]:


s = 'abc'
it = iter(s)
it


# In[27]:


next(it)


# In[28]:


next(it)


# In[29]:


next(it)


# In[30]:


next(it)


# In[31]:


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# In[32]:


rev = Reverse('spam')
iter(rev)


# In[33]:


for char in rev:
    print(char)


# In[34]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[35]:


for char in reverse('golf'):
    print(char)


# In[36]:


sum(i*i for i in range(10))


# In[37]:


xvec = [10, 20, 30]
yvec = [7, 5, 3]
sum(x*y for x,y in zip(xvec, yvec))


# In[45]:


unique_words = set(word for line in page  for word in line.split()
unique_words = ("The quick brown","fox jumped over","the lazy dog's","back 123
times." )


# In[ ]:


valedictorian = max((student.gpa, student.name) for student in graduates)


# In[50]:


page = ("The quick brown","fox jumped over","the lazy dog's","back 123times." )

class Graduate:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
    gpa = 0
    name = ""

graduates = (Graduate("Charlie Brown",8.09), Graduate("Snoopy",3.7),
Graduate("Lucy Brown",3.5))


# In[51]:


data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))


# In[ ]:




