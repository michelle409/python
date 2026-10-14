"""from collections import Counter
a= "aaabbbcccccc"
mycounter = Counter(a)
print(mycounter)

a= "aaabbbcccccc"
mycounter = Counter(a)
print(mycounter.items())

a= "aaabbbcccccc"
mycounter = Counter(a)
print(mycounter.keys())

a= "aaabbbcccccc"
mycounter = Counter(a)
print(mycounter.values())
print(mycounter)
print(mycounter.most_common(1)) #shows the most repeated element
print(mycounter.most_common(1)[0][0]) #shows only the element

#toconvert into a list :
print(list(mycounter.elements())) """

from collections import namedtuple
point = namedtuple('point', 'x,y')
pt = point(1,-4)
print(pt.x, pt.y)