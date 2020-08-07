import math
class Vector3D:
    def __init__(self, x=0, y=0, z=0):
         self.x = x
         self.y = y
         self.z = z

    def magnitude(self):
        return math.sqrt(vect.x**2 + vect.y**2 + vect.z**2)
    
    def __lt__(self, other):
        if self.magnitude < other.magnitude:
        return True

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()
    
