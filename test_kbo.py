from kbo import kbo
from ssfuncs import *

# Show that object instantiation works, and H is drawn
test = kbo(50, 0.1, 10, 30, 260, H = drawH(0.9, 13))

print test.a, test.e, test.inc, test.capom, test.argperi, test.H


# Show error handling on e value
test = kbo(50, 1.1, 10, 30, 260, H = drawH(0.9, 13))

print test.a, test.e, test.inc, test.capom, test.argperi

