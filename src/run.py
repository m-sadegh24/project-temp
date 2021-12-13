import numpy

import src.points as points
import src.arithmetic as arithmetic


print("run.py is running... \n")
print('\n'.join(dir()))

print('\n','-'*50)

print(points.point_inf(10, 20, 30, 40).__repr__())
print(points.point_inf(1, 2, 3, 4) > points.point_inf(0, 1, 2, 0))

print('\n','-'*50)

print(arithmetic.math.add(10, 20))

a = numpy.array([1, 2, 3])
print(a)
