from collections import Counter, defaultdict, namedtuple
from contextvars import copy_context


number = [1,1,1,1,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6]
print(Counter(number))

a = ['a', 'a', 'a', 'b', 'b','b', 'b','b', 'b', 'c', 'c', 'c', 'c','c', 'c','c', 'c', ]
print(Counter(a).most_common())

sentence = "Radha in nibu mein buni ki dhara"
s = Counter(sentence.lower().split())
print(s)


a = ['a', 'a', 'a', 'b', 'b','b', 'b','b', 'b', 'c', 'c', 'c', 'c','c', 'c','c', 'c', ]

c = Counter(a)

print(c.most_common())

print(list(c))
#**********************
## Default Dict


d = defaultdict(lambda: 29)
d["Name"] = "Raghib"
print(d['Name'])
print(d['Age'])