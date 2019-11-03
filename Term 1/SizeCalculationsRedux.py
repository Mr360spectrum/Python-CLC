# Karter Ence
# Shape Size Calculations
# 9/11/2019

# Get side lengths for square/rectangle
print("What is the length of the square?")
sqrLength = float(input(": "))
print("What is the width of the square?")
sqrWidth = float(input(": "))
# Calculate perimeter and area
sqrPer = (sqrLength +sqrWidth) * 2
sqrArea = sqrLength * sqrWidth
# Print the calculations
print(str.format("The perimeter of the square is {0:.2f}", sqrPer))
print(str.format("The area of the square is {0:.2f}", sqrArea))
# ASCII with side lengths
print(str.format("""
        {0:^10.2f}
 _________________________
|                         |
|                         |
|                         |
|                         |
|                         | {1:^10.2f}
|                         |
|                         |
|                         |
|                         |
|_________________________|
""", sqrLength, sqrWidth))

# Get the radius of the circle
print("What is the radius of the circle?")
radius = float(input(": "))
# Calculate the circumference
circumference = 2 * 3.14 * radius
print(str.format("The circumference of the circle is {0:.2f}", circumference))
# ASCII art with radius
print(str.format("""
           %%%    %%%
      %%%              %%%

  %%%                      %%%
        {0:^12.2f}     
 %%%                         %%%
     ----------| 
 %%%                         %%%

 %%%                        %%%

    %%%                  %%%

          %%%     %%%
""", radius))

# Get the base and height of the triangle
print("What is the base length of the triangle?")
triBase = float(input(": "))
print("What is the height of the triangle?")
triHeight = float(input(": "))
# Calculate the area of the triangle
triArea = (triBase * triHeight) / 2
print(str.format("The area of the triangle is {0:.2f}",triArea))
# ASCII are with base and height
print(str.format("""
       /|
      / |
     /  |
    /   |
   /    | {0:<12.2f}
  /     |
 /      |
/_______|
{1:^12.2f}  
""", triHeight, triBase))

# Get the measurements of the cube/rectangular prism
print("What is the height of the cube?")
cubeHeight = float(input(": "))
print("What is the length of the cube?")
cubeLength = float(input(": "))
print("What is the width of the cube?")
cubeWidth = float(input(": "))
# Calculate and print the volume
cubeVol = cubeHeight * cubeLength * cubeWidth
print(str.format("The volume of the cube is {0:.2f}", cubeVol))
# ASCII art with measurements
print(str.format("""
{0:^15.2f}
   +--------+
  /        /|
 /        / | {1:<15.2f}
+--------+  |
|        |  |
|        |  +
|        | /
|        |/{2:<14.2f}
+--------+
""", cubeLength, cubeHeight, cubeWidth))