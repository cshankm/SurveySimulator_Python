from kbo import kbo
from ssfuncs import *

# Show that object instantiation works, and H is drawn
test = kbo(50, 0.1, 10, 30, 260, H = drawH(0.9, 13))

print test.a, test.e, test.inc, test.capom, test.argperi, test.H

#fuzz a by up to +- 10%
test.a = fuzz(test.a, 10)

print test.a

#fuzz a by up to +- 30 AU
test.a = fuzz(test.a, 30, type='abs')

print test.a

# Show error handling on e value
test = kbo(50, 1.1, 10, 30, 260, H = drawH(0.9, 13))

print test.a, test.e, test.inc, test.capom, test.argperi

