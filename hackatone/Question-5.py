# scant method
import numpy as np

def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        return None

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol:
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

def largest_root_bisection(f, a, b, tol=1e-6, max_iter=100):
    roots = []
    subintervals = 20
    dx = (1.5 - 1) / subintervals

    for i in range(subintervals):
        a = 1 + i * dx
        b = a + dx

        if f(a) * f(b) < 0:  # Check if there might be a root
            root = bisection_method(f, a, b)
            if root is not None:
                roots.append(root)

    # Remove duplicates and find largest
    unique_roots = np.unique(np.round(roots, 6))
    largest_root = max(unique_roots)

    return largest_root


def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for _ in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        if abs(fx1) < tol:
            return x1

        # Secant method formula
        x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Check if the next point is within our interval of interest
        if not (1 <= x_next <= 1.5):
            return None

        x0, x1 = x1, x_next

        if abs(x1 - x0) < tol:
            return x1

    return None

def largest_root_secant(f, x0, x1, tol=1e-6, max_iter=100):
    roots = []
    x0_points = np.linspace(1, 1.4, 10)  # Starting points

    for x0 in x0_points:
        root = secant_method(f, x0, x0 + 0.1)
        if root is not None:
            roots.append(root)

    # Remove duplicates and sort
    unique_roots = np.unique(np.round(roots, 6))

    # Verify the largest root
    largest_root = max(unique_roots)
    return largest_root



if __name__ == '__main__':
    f = lambda x: np.cos(2*x**3+5*x**2-6)/(2*np.exp(-2*x))

    x0 = 1
    x1 = 1.5

    secant_root = largest_root_secant(f, x0, x1)
    print(f"The equation in secant method has the largest approximate root in {secant_root}")
    bisection_root = largest_root_bisection(f, x0, x1)
    print(f"The equation in secant method has the largest approximate root in {bisection_root}")