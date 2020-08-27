class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
vec1 = Vector3D(1, 5, 3)
vec2 = Vector3D(4, 4, 1)
print(vec1 * vec2)