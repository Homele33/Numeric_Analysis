import math

def simpsons_rule(f, a, b, n):

    validate_even_subintervals(n)
    h = compute_step_size(a, b, n)
    integral = initialize_integral(f, a, b)

    for i in range(1, n):
        x_i = compute_x_i(a, i, h)
        integral += weighted_function_value(f, x_i, i)

    return finalize_integral(integral, h)


def validate_even_subintervals(n):
    """
    Ensures the number of subintervals is even.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")


def compute_step_size(a, b, n):
    """
    Computes the step size for Simpson's Rule.
    """
    return (b - a) / n


def initialize_integral(f, a, b):
    """
    Initializes the integral with the values at the endpoints.
    """
    return f(a) + f(b)


def compute_x_i(a, i, h):
    """
    Computes the x value at the ith subinterval.
    """
    return a + i * h


def weighted_function_value(f, x_i, i):
    """
    Computes the weighted function value based on the Simpson's Rule.
    Weights: 4 for odd indices, 2 for even indices.
    """
    if i % 2 == 0:
        return 2 * f(x_i)
    else:
        return 4 * f(x_i)


def finalize_integral(integral, h):
    """
    Finalizes the integral by multiplying with the step size divided by 3.
    """
    return integral * (h / 3)


if __name__ == '__main__':
    f = lambda x: (x * math.exp(-x) + math.log(x**2)) * (2*x**3 + 2*x**2 - 3*x - 5)
    # n = 300000
    a = 0.5
    b = 1.0
    for n in range(200000,1000000,100000):
        integral = simpsons_rule(f, a, b, n) 
        if(integral > simpsons_rule(f, a, b, n-100000)):
            continue 
    print(f"Numerical Integration of the definite integral in range [{a}, {b}] with {n} amount of subintervals is {integral}")
    

    print(f"Division into n = {n} sections")
    integral = simpsons_rule(f, a, b, n)
    print(f"Numerical Integration of the definite integral in range [{a}, {b}] is {integral}")