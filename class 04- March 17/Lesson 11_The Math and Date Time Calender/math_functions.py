import math

#1. Built-in math functions, no need to import math
print("abs(-5) = ",abs(-5))
print("pow(2,3) = ",pow(2,3))
print("round(3.124556,2) = ",round(3.124556,2))
print("max(1,2,3,4,56,6) = ",max(1,2,3,4,56,6))
print("min(1,2,3,4,56,6) = ",min(1,2,3,4,56,6))

#2.math Module Functions (Need import math):
print("\n🔹 math module functions: ")

#1.Trigonometric
print("math.sin(math.pi/2) = ",math.sin(math.pi/2))
print("math.cos(0) = ",math.cos(0))
print("math.tan(math.pi/2) =",math.tan(math.pi/2))

#2. Square root & power
print("math.sqrt(9) =",math.sqrt(9))
print("math.factorial(5) =",math.factorial(5))

#3. Logarithmic & exponential
print("math.log(10) = ",math.log(10))   #natural log
print("math.log10(100) =",math.log10(100)) #base-10 log
print("math.exp(2) =",math.exp(2)) #e^2

#4. Rounding
print("math.ceil(4.7) = ",math.ceil(4.7))
print("math.floor(4.7) =",math.floor(4.7))

#5. Constants
print("math.pi =",math.pi)
print("math.e = ",math.e)
print("math.tau =",math.tau)

#6. Special values
print("math.inf = ",math.inf)
print("math.nan =",math.nan)
