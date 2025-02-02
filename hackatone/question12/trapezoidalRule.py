import math


def trapezoidal_rule(f, a, b, n):
  
    h = compute_step_size(a, b, n)
    integral = initial_integral_value(f, a, b)

    for i in range(1, n):
        integral += compute_function_value(f, a, i, h)

    return finalize_integral(integral, h)


def compute_step_size(a, b, n):
    """
    Computes the step size for the trapezoidal rule.
    """
    return (b - a) / n


def initial_integral_value(f, a, b):
    """
    Computes the initial integral value using the endpoints.
    """
    return 0.5 * (f(a) + f(b))


def compute_function_value(f, a, i, h):
    """
    Computes the function value at the ith point.
    """
    return f(a + i * h)


def finalize_integral(integral, h):
    """
    Finalizes the integral by multiplying by the step size.
    """
    return integral * h


if __name__ == '__main__':
    f = lambda x: (x * math.exp(-x) + math.log(x**2)) * (2*x**3 + 2*x**2 - 3*x - 5)
    result = trapezoidal_rule(f, 0.5, 1, 100000)
    print(f"Approximate integral: {result}")
