# Class 2 - Find the Torsional Angle
# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

import math

class vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
               
    def __mul__(self, k):
        return vector(self.x * k, self.y * k, self.z * k)
    
    def __add__(self, other):
        s, o = self, other
        return vector(s.x + o.x, s.y + o.y, s.z + o.z)
   
    def __sub__(self, other):
        return self + other * -1
        
    # dot product
    def __mod__(self, other):
        s, o = self, other
        return (s.x * o.x) + (s.y * o.y) + (s.z * o.z)
    
    # modulus
    def __abs__(self):
        return math.sqrt(self % self)
    
    # cross product
    def __xor__(self, other):
        s, o = self, other
        x = (s.y * o.z) - (s.z * o.y)
        y = (s.z * o.x) - (s.x * o.z)
        z = (s.x * o.y) - (s.y * o.x)
        return vector(x, y, z)
    
def read_vector():
    return vector(*map(float, input().split()))
    
A = read_vector()
B = read_vector()
C = read_vector()
D = read_vector()

X = (B - A) ^ (C - B)
Y = (C - B) ^ (D - C)

phi = math.degrees(math.acos(X % Y / math.sqrt((X % X) * (Y % Y))))
print('%.2f' % phi)
