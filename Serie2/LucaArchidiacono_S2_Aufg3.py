import sympy as sp
import numpy as np

x1, x2, x3 = sp.symbols('x1 x2 x3')
f1 = x1+(x2**2)-(x3**2)-13
f2 = sp.log(x2/4)+sp.exp(0.5*x3-1)-1
f3 = ((x2-3)**2)-(x3**3)+1
f = sp.Matrix([f1, f2, f3])
X = sp.Matrix([x1,x2,x3])
Df = f.jacobian(X)

func = sp.lambdify([(x1, x2, x3)], f, "numpy")
jac = sp.lambdify([(x1, x2, x3)], Df, "numpy")
v = np.array([1.5, 3, 2.5])

print(jac(v))