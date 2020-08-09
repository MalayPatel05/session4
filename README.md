
class Qualean(builtins.object)
 |  Qualean class that is inspired by Boolean+Quantum concepts. 
 |  We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1) but it internally picks an random value. 
 |  The moment you assign it a real number, it immediately finds an random number random.uniform(-1, 1) 
 |  and multiplies with it and stores that number internally after using Bankers rounding to 10th decimal place.
 |  Qualean is derived class of float. All mathematical and conditional operation on Qualean object are similar to those of float
 |  
 |  Methods defined here:
 |  
 |  __add__(self, other)
 |      returns self+other,returns complex value if other is complex number otherwise returns Qualean object
 |  
 |  __and__(self, other)
 |      if self is false, then retrun self, else return other
 |  
 |  __bool__(self)
 |      return self!=0
 |  
 |  __eq__(self, other)
 |      returns self==other
 |      compares self and other upto 10th decimal place
 |  
 |  __float__(self)
 |      returns object value as float
 |  
 |  __ge__(self, other)
 |      returns self>=other, compares self and other upto 10th decimal place
 |  
 |  __gt__(self, other)
 |      returns self>other
 |  
 |  __init__(self, value=None, _disable_rndm=0)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __invertsign__(self)
 |      returns Qualean obejct with inverted sign of self
 |  
 |  __le__(self, other)
 |      returns self<=other, compares self and other upto 10th decimal place
 |  
 |  __lt__(self, other)
 |      returns self<other
 |  
 |  __mul__(self, other)
 |      returns self*other,returns complex value if other is complex number otherwise returns Qualean object
 |  
 |  __or__(self, other)
 |      if self is false, then retrun other, else return self
 |  
 |  __repr__(self)
 |      Return values to recreate Qualean object
 |  
 |  __sqrt__(self)
 |      returns square root of self
 |  
 |  __str__(self)
 |      Return value of Qualean object
 |  
 |  ----------------------------------------------------------------------

