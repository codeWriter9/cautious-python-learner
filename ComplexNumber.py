'''
Created on 31-Jul-2019

@author: Sanjay Ghosh
'''
import math;
class Complex:
    """A class to hold complex number"""
    real = 0;
    imaginary = 0;
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary;
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary);
    
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary);
        
    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + self.imaginary * no.real);
    
    def __truediv__(self, no):
        denominator = no.real * no.real + no.imaginary * no.imaginary;
        real_numerator = self.real * no.real + self.imaginary * no.imaginary;
        imaginary_numerator = self.imaginary * no.real - self.real * no.imaginary;
        return Complex(real_numerator / denominator, imaginary_numerator / denominator);

    def mod(self):
        return Complex(math.sqrt(self.real * self.real + self.imaginary * self.imaginary), 0);
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result    

if __name__ == '__main__':
    c = map(float, input().split());
    d = map(float, input().split());
    x = Complex(*c);
    y = Complex(*d);    
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n');    