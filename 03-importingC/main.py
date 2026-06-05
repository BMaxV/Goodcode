import ctypes
myClib = ctypes.CDLL("./mysharedobject.so")

# show this works with helloworld
myClib.helloworld()

#showing you can fork here if you want.
l = []
r = myClib.pyfork()
l.append(1)

# calling addNum() C function
# it returns addition of two numbers
varAdd = myClib.addNum(20, 30)

#show the forked process as well that the C function works.
print("Addition : ", varAdd)
print(l)
