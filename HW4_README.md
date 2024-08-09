# Interpolation Methods

## **Overview**

This Python script implements three interpolation methods:

- **Linear Interpolation**
- **Polynomial Interpolation**
- **Lagrange Interpolation**

It allows users to estimate values based on given data points.

## **Features**

- **Linear Interpolation:** Estimates values between two points.
- **Polynomial Interpolation:** Fits and uses a quadratic polynomial to estimate values from three points.
- **Lagrange Interpolation:** Uses Lagrange polynomials to estimate values based on multiple points.

## **Functions**

- **`linearInter(tuplesList, x)`**

  - Estimates the value at `x` using linear interpolation between points in `tuplesList`.

- **`polynomialInter(vectorX, x)`**

  - Estimates the value at `x` using a quadratic polynomial.

- **`lagrange_interpolation(x_values, y_values)`**
  - Generates a Lagrange interpolation function based on given `x_values` and `y_values`.

## **Usage**

Run the script and select an option:

1. **Linear Interpolation:** Estimate between two points.
2. **Polynomial Interpolation:** Estimate using a quadratic polynomial.
3. **Lagrange Interpolation:** Estimate using Lagrange polynomials.
4. **Exit:** Close the program.

## **Example**

```plaintext
Choose the option you want:
1. Linear Interpolation
2. Polynomial Interpolation
3. Lagrange Interpolation
4. Exit
1
Y: 0.5252  Estimate for 2.5

Choose the option you want:
1. Linear Interpolation
2. Polynomial Interpolation
3. Lagrange Interpolation
4. Exit
```
