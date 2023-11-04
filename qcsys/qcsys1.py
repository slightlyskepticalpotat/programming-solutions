# 4
a, b = map(float, input().split())
print(abs(a - b) == 90)

# 2
import math, numpy

l, d = map(int, input().split())
l *= 10 ** -9
d *= 10 ** -3
print(round(math.asin(l / d) * 180 / math.pi, 3))

# 24
import math, numpy

n, m = map(int, input().split())
mat = numpy.matrix([[int(i) for i in input().split()] for _ in range(n)])
print(mat)
print("state", math.isclose(numpy.linalg.norm(mat), 1))
mat2 = numpy.matmul(mat.getH(), mat)
print(mat2)
print("transformation", numpy.allclose(mat2, numpy.identity(mat.shape[0])))
mat3 = mat.getH()
print(mat3)
print("observable", numpy.all(mat == mat3))

# 12
import numpy

m, n = map(int, input().split())
a, b = numpy.matrix([int(i) for i in input().split()]), numpy.matrix([int(i) for i in input().split()])
print((numpy.matmul(a, b.getH()).item(0, 0)) ** 2)

# 6
import math, numpy

exec(f"v = {input().strip().replace('np', 'numpy')}")
print(v)
print(numpy.linalg.norm(v))
print(math.isclose(numpy.linalg.norm(v), 1))

# 4, easier version
import numpy

a, b, c, d = map(int, input().split())
print(numpy.matmul(numpy.zeros((a, b)), numpy.zeros((c, d))))
print(numpy.matmul(numpy.zeros((a, b)), numpy.zeros((c, d))).shape)

# 23
import numpy

exec(f"m = {input().strip().replace('np', 'numpy')}")
m = numpy.matrix(m)
print(m)
m = numpy.matmul(m.getH(), m)
print(numpy.allclose(m, numpy.identity(m.shape[0])))

# 19
import numpy

n, k = map(int, input().split())
k, m = map(int, input().split())
m1 = numpy.array([numpy.array([complex(i) for i in input().split()]) for j in range(n)])
m2 = numpy.array([numpy.array([complex(i) for i in input().split()]) for j in range(k)])
print(m1)
print(m2)
print(numpy.matmul(m1, m2))

# 13
import numpy

exec(f"v = {input().strip().replace('np', 'numpy')}")
print(v)
print(numpy.linalg.norm(v))

# 8
import math

a, b = map(int, input().split())
print(str(math.sqrt(a ** 2 + b ** 2)) + "e^" + str(math.atan(b / a)) + "i")

# 4
import math

a, b = map(int, input().split())
print(math.sqrt(a ** 2 + b ** 2))