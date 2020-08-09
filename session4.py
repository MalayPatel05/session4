# -*- coding: utf-8 -*-
"""
@author: Malay Patel
"""
import random
from cmath import isclose,sqrt
from decimal import Decimal

num_type = ['int','float','complex','Decimal','Qualean']

class Qualean:
    '''Qualean class that is inspired by Boolean+Quantum concepts. 
    We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an random value. 
    The moment you assign it a real number, it immediately finds an random number random.uniform(-1, 1) 
    and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.
    Qualean is derived class of float. All mathematical and conditional operation on Qualean object are similar to those of float'''

    def __init__(self,value=None,_disable_rndm=0):
            self.userinput=value
            self.value = (value,_disable_rndm)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,attrib):
        value,_disable_rndm = attrib
        if (_disable_rndm or (type(value).__name__ in num_type) and (value in [1,0,-1])):
            value=float(value)
            if _disable_rndm:
                self.userinput=value
                self._rand_num=None
                self._rand_num_rndd=None
                self._value = value
            else:
                if value == 0:                    
                    self._rand_num=None
                    self._rand_num_rndd=None
                    self._value = 0.0
                else:                    
                    self._rand_num=random.uniform(-1,1)
                    self._rand_num_rndd=round(self._rand_num,10)
                    self._value=value*self._rand_num_rndd
        else:
            raise ValueError("Input value should be 1, 0 or -1")

    def __repr__(self):
        '''Return values to recreate Qualean object'''
        return f'Qualean Value:{self.value}, User Input:{self.userinput}, Random Number:{self._rand_num}, Rounded Random Number:{self._rand_num_rndd}'

    def __and__(self,other):
        '''if self is false, then retrun self, else return other'''
        if not(self.value):
            return self.value
        elif isinstance(other,Qualean):
            return other.value
        else:
            return other
    
    def __or__(self,other):
        '''if self is false, then retrun other, else return self'''
        if self.value:
            return self.value
        elif isinstance(other,Qualean):
            return other.value
        else:
            return other
            
    def __add__(self,other):
        '''returns self+other,returns complex value if other is complex number otherwise returns Qualean object'''
        if not(type(other).__name__ in num_type):
            raise TypeError(f'\'+\' not supported between isntance of Qualean and {type(other).__name__}')
        elif isinstance(other,Qualean):
            return Qualean((self.value+other.value),1)
        elif isinstance(other,complex):
            return complex((other.real+self.value),other.imag)
        else:
            return Qualean((self.value+float(other)),1)

    def __mul__(self,other):
        '''returns self*other,returns complex value if other is complex number otherwise returns Qualean object'''
        if not(type(other).__name__ in num_type):
            raise TypeError(f'\'*\' not supported between isntance of Qualean and {type(other).__name__}')
        elif isinstance(other,Qualean):
            return Qualean(round(self.value*other.value,10),1)
        elif isinstance(other,complex):
            return complex(other.real*self.value,other.imag*self.value)
        else:
            return Qualean((self.value*float(other)),1)      

    def __str__(self):
        '''Return value of Qualean object'''
        return f'{self.value}'

    def __eq__(self,other):
        '''returns self==other
        compares self and other upto 10th decimal place'''
        if isinstance(other,Qualean):
            return isclose(self.value,other.value,rel_tol=1e-10)
        elif type(other).__name__ in num_type:
            return isclose(self.value,other,rel_tol=1e-10)
        else:
            raise TypeError(f'\'==\' not supported between isntance of Qualean and {type(other).__name__}')

    def __float__(self):
        '''returns object value as float'''
        return self.value

    def __ge__(self,other):
        '''returns self>=other, compares self and other upto 10th decimal place'''
        if isinstance(other,Qualean):
            return (self.value>other.value or isclose(self.value,other.value,rel_tol=1e-10))
        elif isinstance(other,complex) or not(type(other).__name__ in num_type):
            raise TypeError(f'\'>=\' not supported between isntance of Qualean and {type(other).__name__}')
        else:
            return (self.value>other or isclose(self.value,other,rel_tol=1e-10))

    def __gt__(self,other):
        '''returns self>other'''
        if isinstance(other,Qualean):
            return self.value>other.value
        elif isinstance(other,complex) or not(type(other).__name__ in num_type):
            raise TypeError(f'\'>\' not supported between isntance of Qualean and {type(other).__name__}')
        else:
            return self.value>other

    def __le__(self,other):
        '''returns self<=other, compares self and other upto 10th decimal place'''
        if isinstance(other,Qualean):
            return (self.value<other.value or isclose(self.value,other.value,rel_tol=1e-10))
        elif isinstance(other,complex) or not(type(other).__name__ in num_type):
            raise TypeError(f'\'=<\' not supported between isntance of Qualean and {type(other).__name__}')
        else:
            return (self.value<other or isclose(self.value,other,rel_tol=1e-10))

    def __lt__(self,other):
        '''returns self<other'''
        if isinstance(other,Qualean):
            return self.value<other.value
        elif isinstance(other,complex) or not(type(other).__name__ in num_type):
            raise TypeError(f'\'<\' not supported between isntance of Qualean and {type(other)}.__name__')
        else:
            return self.value<other

    def __invertsign__(self):
        '''returns Qualean obejct with inverted sign of self'''
        return Qualean(-self.value,1)

    def __sqrt__(self):
        '''returns square root of self'''
        if self.value>=0:
            return Qualean(float(Decimal(self.value).sqrt()),1)
        else:
            return complex(0,Decimal(abs(self.value)).sqrt())

    def __bool__(self):
        '''return self!=0'''
        return self.value!=0