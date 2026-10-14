#sets - alwyas on {}, unordered, mutable, no duplicates

#UNION OF SETS
ODDS={1,3,5,7,9}
EVENS={2,4,6,8}
PRIME={2,3,7,}
u=ODDS.union(EVENS)
print(u)

#intersection = 
i = ODDS.intersection(EVENS)
print(i)

#differenec of sets
seta= {1,2,3,4,5,6,7,8}
setb = {4,5,6,7}
d= seta.difference(setb)
print(d)

#symmetric diff - removes all the common elements from both the sets and prints evrything else 
seta= {1,2,3,4,5,6,7,8}
setb = {4,5,6,7}
e=seta.symmetric_difference(setb)
print(e)