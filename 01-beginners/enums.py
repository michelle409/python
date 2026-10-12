#ENUMS - Enums are readable names that are bound to a constant value.
#import first :
from enum import Enum
#then initialize : 
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
print(State.ACTIVE) #reference State.INACTIVE and State.ACTIVE, and they serve as constants


#to list all the possible values of an enum:
list(State) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]


# to count them :
len(State) # 2
