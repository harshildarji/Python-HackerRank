# Classes: Dealing with Complex Numbers
# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

from math import sqrt

class ComplexNumber(object):
    def __init__(self, x=0, y=0):
        self.real_p = x
        self.imag_p = y

    def __add__(self, other):
        s = ComplexNumber()
        s.real_p = self.real_p + other.real_p
        s.imag_p = self.imag_p + other.imag_p
        return s
    
    def __sub__(self, other):
        s = ComplexNumber()
        s.real_p = self.real_p - other.real_p
        s.imag_p = self.imag_p - other.imag_p
        return s

    def __mul__(self, other):
        s = ComplexNumber()
        s.real_p = self.real_p*other.real_p - self.imag_p*other.imag_p
        s.imag_p = self.real_p*other.imag_p + self.imag_p*other.real_p
        return s

    def __truediv__(self, other):
        s = ComplexNumber()
        s.real_p = (self.real_p*other.real_p + self.imag_p*other.imag_p) / (other.real_p**2 + other.imag_p**2)
        s.imag_p = (self.imag_p*other.real_p - self.real_p*other.imag_p) / (other.real_p**2 + other.imag_p**2)
        return s

    def __abs__(self):
        s = ComplexNumber()
        s.real_p = sqrt(self.real_p**2 + self.imag_p**2)
        return s

    def __str__(self):
        if self.imag_p >= 0:
            s = "{0:.2f}+{1:.2f}i".format(self.real_p, self.imag_p)
        else:
            s = "{0:.2f}{1:.2f}i".format(self.real_p, self.imag_p)
        return s

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
z1 = ComplexNumber(x1, y1)
z2 = ComplexNumber(x2, y2)
print(z1+z2)
print(z1-z2)
print(z1*z2)
print(z1/z2)
print(abs(z1))
print(abs(z2))
