#intertools : product, permutations, combinations, acumulate, grouby, and infitine iterators
"""from itertools import product
a = [1,2]
b = [3,]
prod=product(a,b, repeat = 2)
print(list(prod))

from itertools import permutations 
a = [1,2,3]
perm = permutations(a)
print(list(perm))

 #to set a length of the permutations : 
a = [1,2,3]
perm = permutations(a,2)
print(list(perm))

from itertools import combinations 
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))


from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))
combwr=combinations_with_replacement(a,2)
print(list(combwr))"""


from itertools import accumulate
a=[1,3,4,5]
acc=accumulate(a)
print(a)
print(list(acc))



from itertools import accumulate
import operator
a=[1,3,4,5]
acc=accumulate(a, func=operator.mul)
print(a)
print(list(acc))

from itertools import accumulate
import operator
a=[1,2,5,3,4]
acc=accumulate(a, func=max)
print(a)
print(list(acc))
