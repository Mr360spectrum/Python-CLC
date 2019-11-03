# Jamerson McGuire, Karter Ence, Xander Szykowny, MICHAEL calhoun
# Shape Size Calculations
# 9/11/2019

squSide1 = float(input("What is the first side length?"))
squSide2 = float(input("What is the second side length?"))
squPer = (squSide1 + squSide2) * 2
squArea = squSide1 * squSide2
print(str.format("The perimeter of the square is {0:.2f}", squPer))
print(str.format("The area of the square is {0:.2f}", squArea))
#ascii here
print("""
---------------
|             |
|             |
|             |
|             |
|             |
--------------- """)
cirRad = float(input("What is the radius of the circle?"))
cirCir = 2 * 3.14 * cirRad
print(str.format("The circumference of the circle is {0:.2f}", cirCir))
#ascii here
print('''
                      ,,ggddY""""Ybbgg,,
                 ,agd""'              `""bg,
              ,gdP"                       "Ybg,
            ,dP"                             "Yb,
          ,dP"         _,,ddP"""Ybb,,_         "Yb,
         ,8"         ,dP"'         `"Yb,         "8,
        ,8'        ,d"                 "b,        `8,
       ,8'        d"                     "b        `8,
       d'        d'        ,gPPRg,        `b        `b
       8         8        dP'   `Yb        8         8
       8         8        8)     (8        8         8
       8         8        Yb     dP        8         8
       8         Y,        "8ggg8"        ,P         8
       Y,         Ya                     aP         ,P
       `8,         "Ya                 aP"         ,8'
        `8,          "Yb,_         _,dP"          ,8'
         `8a            ""YbbgggddP""'           a8'
          `Yba                                 adP'
            "Yba                             adY"
              `"Yba,                     ,adP"'
                 `"Y8ba,             ,ad8P"'
                      ``""YYbaaadPP""''
''')
triBase = float(input("What is the base length of the triangle?"))
triHeight = float(input("What is the height of the triangle?"))
triArea = (triBase * triHeight) / 2
print(str.format("The area of the triangle it {0:.2f}", triArea))
#ascii here
print("""
         /\       
        /  \       
       /    \     
      /      \     
     /        \     
    /          \   
    ------------ """)


            
cubHeight = float(input("What is the height of the cube?"))
cubSide = float(input("What is the base of the cube?"))
cubLength = float(input("What is the length of the cube?"))
cubeVol = cubHeight * cubSide * cubLength
print(str.format("The volume of the cube is {0:.2f}", cubeVol))
#ascii here
print('''


                      _.-+.
                 _.-""     '.
             +:""            '.
             J \               '.
              L \             _.-+
              |  '.       _.-"   |
              J    \  _.-"       L
               L    +"          J
               +    |           |
                \   |          .+
                 \  |       .-'
                  \ |    .-'
                   \| .-'
                    +'   ''')
