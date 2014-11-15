import c4d
import random

#
# Create a Null object
#
parent = c4d.BaseObject(c4d.Onull)  # create new Null object instance
parent.SetName("Scattered Cubes")   # give is a recognizable name
doc.InsertObject(parent)            # at it to our document

# loop 1000 times
for i in xrange(1,1000):
  # random position coordinates
  x = (random.random() - 0.5) * 100
  y = (random.random() - 0.5) * 100
  z = 0
  obj = c4d.BaseObject(c4d.Ocube)               # create new object instance
  obj.SetRelPos(c4d.Vector(x,y,z))              # Set position of cube
  obj[c4d.PRIM_CUBE_LEN] = c4d.Vector(1, 1, 1)  # Set size of cube
  obj.InsertUnder(parent)                       # Insert object in document

c4d.EventAdd()                  # Send global event message
