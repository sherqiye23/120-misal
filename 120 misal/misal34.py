#34cü sual
#İki dəyişənli xətti cəbri tənliklər sisteminin həllinin Krammer (determinantlar) üsulu ilə həlli

import numpy
M2=numpy.array([[1.,0.,1.,0.],[-1.,1.,-2.,1.],[4.,0.,1.,-2.],[-4.,4.,0.,1.]])
V2=numpy.array([2.,-2.,0.,5.])

x=numpy.linalg.solve(M2,V2)
print(x)