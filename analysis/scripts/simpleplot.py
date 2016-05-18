import numpy as np
import matplotlib.pyplot as plt

def main():
    # Make some fake data.
    a = np.arange(-1, 1, .02)
    fx = []
    p_0 = []
    p_1 = []
    p_2 = []
    p_3 = []
    for x in a:
        fx.append(f(x))
        p_0.append(p0(x))
        p_1.append(p1(x))
        p_2.append(p2(x))
        p_3.append(p3(x))
    
    # Create plots with pre-defined labels.
    plt.plot(a, fx, 'k', label='f(x)')
    plt.plot(a, p_0, 'c--', label='One term')
    plt.plot(a, p_1, 'g--', label='Two terms')
    plt.plot(a, p_2, 'b--', label='Three terms')
    plt.plot(a, p_3, 'r--', label='Four terms')
    plt.title('Legendre Polynomials')
    plt.grid()
    
    legend = plt.legend(loc='upper left')
    
    # Put a nicer background color on the legend.
    legend.get_frame()
    
    plt.show()

def f(x):
    if x < 0:
        return 0
    else:
        return x

def p0(x):
    return 1/4
    
def p1(x):
    return p0(x) + 1/2 * x

def p2(x):
    return p1(x) + 5/16 * 1/2 * (3*x*x - 1)

def p3(x):
    return p2(x) - 3/32 * 1/8 * (35*x**4 - 30*x*x + 3)

if __name__ == "__main__":
    main()