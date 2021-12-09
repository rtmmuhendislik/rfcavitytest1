import math
from scipy.fft import fft, ifft
import sympy
import matplotlib.pyplot as plt
import numpy as np
#import pyheadtail
#s=iw

t, s = sympy.symbols('t, s')
i = sympy.symbols('i', real=True, positive=True)

f = sympy.exp(-i*t)
f

sympy.integrate(f*sympy.exp(-s*t), (t, 0, sympy.oo))

sympy.laplace_transform(f, t, s)

F = sympy.laplace_transform(f, t, s, noconds=True)
F

def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

def invL(F):
    return sympy.inverse_laplace_transform(F, s, t)
invL(F)

sympy.Heaviside(t)


sympy.plot(sympy.Heaviside(t));

invL(F).subs({i: 2})


p = sympy.plot(f.subs({i: 2}), invL(F).subs({i: 2}),
               xlim=(-1, 4), ylim=(0, 3), show=False)
p[1].line_color = 'red'
p.show()

omega = sympy.Symbol('omega', real=True)
exp = sympy.exp
sin = sympy.sin
cos = sympy.cos
functions = [1,
         t,
         exp(-i*t),
         t*exp(-i*t),
         t**2*exp(-i*t),
         sin(omega*t),
         cos(omega*t),
         1 - exp(-i*t),
         exp(-i*t)*sin(omega*t),
         exp(-i*t)*cos(omega*t),
   #      exp(-i*omega*t)*sin(omega*t),

         ]
functions

Fs = [L(f) for f in functions]
Fs

from pandas import DataFrame

def makelatex(args):
    return ["$${}$$".format(sympy.latex(a)) for a in args]

DataFrame(list(zip(makelatex(functions), makelatex(Fs))))

F = ((s + 1)*(s + 2)* (s + 3))/((s + 4)*(s + 5)*(s + 6))
F

F.apart(s)

invL(F)

invL(F).simplify()

invL(F.apart(s))
