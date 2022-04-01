class CoOrdinates:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    #  Since Two Class Can Not Be Added We Have To Write in __add__ What Happen If We Add
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return (x, y)
    
p1 = CoOrdinates(2,5)
p2 = CoOrdinates(3,4)

print(p1 + p2) # (5, 9)
