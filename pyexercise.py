import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(((sy.cos(x))*(sy.sin(x))*(sy.exp(x))), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[3,2,1,9,8,7,6,5,4,1], [1,2,8,4,9,6,7,5,1,6],[9,4,5,2,7,8,6,1,3,4],[-4,5,9,3,8,5,6,8,-1,5],[9,-5,3,7,4,8,2,6,9,1],[7,3,8,1,9,4,-5,8,2,7],[7,9,5,1,8,6,3,4,8,2],[8,2,1,4,7,6,9,2,5,1],[4,8,3,7,2,1,9,3,5,8],[6,4,8,2,5,1,9,3,7,5]] )
    b = np.array([8,5,4,7,9,6,3,2,1,5])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1402082
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
