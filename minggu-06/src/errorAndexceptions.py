#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True print('Hello world')
File "<stdin>", line 1
while True print('Hello world')


# In[2]:


10 * (1/0)


# In[3]:


4 + spam*3


# In[4]:


'2' + 2


# In[5]:


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


# In[6]:


except (RuntimeError, TypeError, NameError):
    pass


# In[7]:


class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


# In[8]:


import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


# In[9]:


for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


# In[10]:


try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x =', x)
    print('y =', y)


# In[11]:


def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# In[12]:


raise NameError('HiThere')


# In[13]:


raise ValueError


# In[14]:


try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# In[15]:


raise RuntimeError from exc


# In[16]:


def func():
     raise ConnectionError
try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


# In[17]:


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None


# In[18]:


try:
     raise KeyboardInterrupt
finally:
    print('Goodbye, world!')


# In[19]:


def bool_return():
    try:
        return True
    finally:
        return False
bool_return()


# In[20]:


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)


# In[21]:


divide(2, 0)


# In[22]:


divide("2", "1")


# In[23]:


for line in open("myfile.txt"):
    print(line, end="")


# In[24]:


with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


# In[ ]:




