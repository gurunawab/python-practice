s1 = 'gfg'
s2 = 'GfG'
print(s1)
print(s2)

s = """I am Learning
python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Greek'''
print(s)

s = "GeeksForGeeks"
print(s[0])
print(s[4])
print(s[-10])
print(s[-5])
print(s[1:4])
print(s[:3])
print(s[3:])
print(s[::-1])

s = "Python"
for i in s:
    print(i)

s = "geeksforGeeks"
s = "G" + s[1:]
print(s)

s = "GFG"
del s

s = "hello geeks"
s1 = "H" + s[1:]
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)
print(s2)

s = "Geeksforgeeks"
print(len(s))

from collections import Counter

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
ctn = Counter(nums)
print(ctn)

from collections import Counter
ctn1 = Counter([1, 2, 2, 3, 3, 3])
ctn2 = Counter({1: 1, 2: 2, 3: 3, 4: 4})
ctn3 = Counter('hello World')
print(ctn1)
print(ctn2)
print(ctn3)

from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
print(ctr[1])
print(ctr[2])
print(ctr[3])
print(ctr[4])

from collections import Counter
ctr = Counter([1, 2, 2])
ctr.update([2, 3, 3, 3])
print(ctr)

from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
items = list(ctr.elements())
print(items)

from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
common = ctr.most_common(2)
print(common)

from collections import Counter
ctr = Counter([1, 2, 2])
ctr[2] += 1
ctr[3] += 1
print(ctr)

from collections import Counter
ctr = Counter([1, 2, 2, 3, 3, 3])
ctr.subtract([2, 3, 3])
print(ctr)

from collections import OrderedDict
od = OrderedDict()
od['apple'] = 1
od['banana'] = 2
od['cherry'] = 3
print(list(od.items()))

from collections import OrderedDict

print("dict")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
for key, val in d.items():
    print(key, val)

print("ordered dict")
od = OrderedDict()
od['d'] = 4
od['b'] = 2
od['a'] = 1
od['c'] = 3
for key, val in od.items():
    print(key, val)

from collections import OrderedDict

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in d.items():
    print(k, v)

print("OrderedDict:")
od = OrderedDict([('d', 4), ('b', 2), ('a', 1), ('c', 3)])
for k, v in od.items():
    print(k, v)    

from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
od['c'] = 5

for k, v in od.items():
    print(k, v)

from collections import OrderedDict

od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])
print(od1 == od2)

from collections import OrderedDict

d1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
d2 = OrderedDict(reversed(list(d1.items())))

for k, v in d2.items():
    print(k, v)

from collections import OrderedDict
d = OrderedDict([{'b', 1}, ('b', 2), ('c', 3)])
res = d.popitem(last=True)
print(res)


from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
od.pop('c')

for k, v in od.items():
    print(k, v)

od['c'] = 3
for k, v in od.items():
    print(k, v)    