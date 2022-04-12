#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


os.chdir('/server/accesslogs')
os.system('mkdir today')


# In[3]:


import os
dir(os)


# In[4]:


help(os)


# In[5]:


import shutil
shutil.copyfile('data.db', 'archive.db')


# In[6]:


shutil.move('/build/executables', 'installdir')


# In[7]:


import glob
glob.glob('*.py')


# In[8]:


import sys
print(sys.argv)


# In[9]:


import argparse

parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)


# In[10]:


sys.stderr.write('Warning, log file not found starting a new one\n')


# In[11]:


import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')


# In[12]:


re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


# In[13]:


'tea for too'.replace('too', 'two')


# In[14]:


import math
math.cos(math.pi / 4)


# In[15]:


math.log(1024, 2)


# In[16]:


import random
random.choice(['apple', 'pear', 'banana'])


# In[17]:


random.sample(range(100), 10)


# In[18]:


random.random()


# In[19]:


random.randrange(6)


# In[20]:


import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)


# In[21]:


statistics.median(data)


# In[22]:


statistics.variance(data)


# In[23]:


from urllib.request import urlopen
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())


# In[24]:


import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
"""To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()


# In[25]:


# dates are easily constructed and formatted
from datetime import date
now = date.today()
now


# In[26]:


now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")


# In[27]:


# dates support calendar arithmetic
birthday = date(1964, 7, 31)
age = now - birthday
age.days


# In[28]:


import zlib
s = b'witch which has which witches wrist watch'
len(s)


# In[29]:


t = zlib.compress(s)
len(t)


# In[30]:


zlib.decompress(t)


# In[31]:


zlib.crc32(s)


# In[32]:


from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[33]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[34]:


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests


# In[35]:


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests


# In[36]:


import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))


# In[37]:


import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)


# In[38]:


import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))


# In[39]:


import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')


# In[40]:


conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
locale.format("%d", x, grouping=True)


# In[41]:


locale.format_string("%s%.*f", (conv['currency_symbol'],
                    conv['frac_digits'], x), grouping=True)


# In[42]:


from string import Template
t = Template('${village}folk send $$10 to $cause.')
t.substitute(village='Nottingham', cause='the ditch fund')


# In[43]:


t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
t.substitute(d)


# In[44]:


t.safe_substitute(d)


# In[46]:


import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')


# In[47]:


t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


# In[48]:


import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header


# In[49]:


import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# In[50]:


import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# In[51]:


import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']


# In[52]:


del a
gc.collect()


# In[53]:


d['primary']


# In[54]:


from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)


# In[55]:


a[1:3]


# In[56]:


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())


# In[57]:


unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)


# In[58]:


import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores


# In[59]:


from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)
heappush(data, -5)
[heappop(data) for i in range(3)]


# In[60]:


from decimal import *
round(Decimal('0.70') * Decimal('1.05'), 2)


# In[61]:


round(.70 * 1.05, 2)


# In[62]:


Decimal('1.00') % Decimal('.10')


# In[63]:


1.00 % 0.10


# In[64]:


sum([Decimal('0.1')]*10) == Decimal('1.0')


# In[65]:


sum([0.1]*10) == 1.0


# In[66]:


getcontext().prec = 36
Decimal(1) / Decimal(7)


# In[ ]:




