
#Some features of python are not included by default. To get access to them, we must import libraries that contain
#these features/functions.

#BTW, a function is a piece of code that takes in an input or "argument" and does stuff with it.
#We'll talk more about this next week. We call (use) them by using function(input1, input2, input3, etc)

#Can import stuff from a library "foo" either as:
#"import foo" to import everything in foo (to access "bar" in "foo", use "foo.bar")
#"from foo import bar" to only import bar from foo (and then you access bar simply with "bar")
#"from foo import bar as baz" to import bar from foo under the name baz (access bar with "baz")

#Don't import every library for your program unless you need the libraries. Doing so adds unnecessary stuff
#program, making it confusing to use libraries and possibly causing poor performance.

import math
#from math import sin as foo
#from math import pi

#Warning, not everything you can import from a library is a function! (for instance, math.pi is a float)

print math.sin(90/(180/math.pi))
print math.cos(90/(180/math.pi))