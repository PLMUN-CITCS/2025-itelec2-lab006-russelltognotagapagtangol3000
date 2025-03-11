import math

# Square root calculation
number = 16
sqrt_result = math.sqrt(number)

# Pi value
pi_value = math.pi

# Angle conversion and trigonometric calculations
angle_30_degrees = 30
angle_60_degrees = 60
angle_45_degrees = 45

angle_30_radians = math.radians(angle_30_degrees)
angle_60_radians = math.radians(angle_60_degrees)
angle_45_radians = math.radians(angle_45_degrees)

sin_result = round(math.sin(angle_30_radians), 15)
cos_result = round(math.cos(angle_60_radians), 15)
tan_result = round(math.tan(angle_45_radians), 15)

# Exponential and logarithm calculations
exp_result = math.exp(2)
log_result = math.log(10)  # Natural logarithm (base e)
log10_result = math.log10(100)  # Logarithm base 10

# Output with exact expected format
print(f"Square root of {number} is: {sqrt_result}")
print(f"Value of pi is: {pi_value}")
print(f"Sine of 30 degrees (in radians) is: {sin_result}")
print(f"Cosine of 60 degrees (in radians) is: {cos_result}")
print(f"Tangent of 45 degrees (in radians) is: {tan_result}")
print(f"Exponential of 2 is: {exp_result}")
print(f"Logarithm (base e) of 10 is: {log_result}")
print(f"Logarithm (base 10) of 100 is: {log10_result}")
