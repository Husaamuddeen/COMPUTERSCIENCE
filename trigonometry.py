#import the class for triangle objects
from Triangle import Triangle
import time
import math, turtle


is_triangle_found = False
#function for finding the missing values of a triangle
def findtriangle():
    #integer for converting radians into degrees
    degrees = 180/math.pi
    #take user input for values (0, = none)
    print("Enter the values of your triangle that you know")
    print("\nIf you are missing a value, enter 0\n\n")
    a = float(input("Enter length a: "))
    b = float(input("Enter length b: "))
    c = float(input("Enter length c: "))
    A = float(input("Enter angle A: "))
    B = float(input("Enter angle B: "))
    C = float(input("Enter angle C: "))
    area = float(input("Enter the area: "))
    perimeter = float(input("Enter the perimeter: "))


#function to find a missing length (a)
    def length(a,b,c,A,B,C):
        #find a using the formula perimeter = a + b + c
        if b != 0 and c != 0 and perimeter != 0:
            a = perimeter-(b+c)
        #find a using the cosine rule (a^=b^+c^-2bccos(A))
        elif b != 0 and c != 0 and A != 0:
            a = math.sqrt(b**2+c**2-2*b*c*math.cos(math.radians(A)))
        #find a using the sine rule (a = b/sin(B)*sin(A))
        elif b != 0 and B != 0 and A != 0:
            a = b/math.sin(math.radians(B))*math.sin(math.radians(A))
        #find a using the sine rule (a = b/sin(B)*sin(A))
        elif c != 0 and C != 0 and A != 0:
            a = c/math.sin(math.radians(C))*math.sin(math.radians(A))
        #find a using the formula for area (area = 0.5absin(C)) rearranged to a = area/(0.5bsin(C))
        elif area != 0 and b != 0 and C != 0:
            a = area/(0.5*b*math.sin(math.radians(C)))
        #find a using the formula for area (area = 0.5acsin(B)) rearranged to a = area/(0.5csin(B))
        elif area != 0 and c != 0 and B != 0:
            a = area/(0.5*c*math.sin(math.radians(B)))
        #find a using my own formula (last resort) (a = a factor of ac(area/0.5sin(B)) which ads to (perimeter - b)
        elif b != 0 and B != 0 and area != 0 and perimeter != 0:
            #ac is a*c found using the formula for area of a triangle
            ac = int(area/(0.5*math.sin(math.radians(B))))
            #list for the factors of ac
            factors = []
            #loop to find all the factors of ac and append to factors
            for i in range (1,ac+1):
                if ac % i == 0:
                    factors.append(i)
            #find how many factors there are
            length = len(factors)
            #loop for finding a pair of factors that add to make the perimeter - b
            for i in range(0,length):
                for x in range(0,length):
                    if factors[i]+factors[x] == perimeter - b and factors[i]*factors[x] == ac:
                        a = factors[i]
                        c = factors[x]
        #find a using my own formula (last resort) (a = a factor of ab(area/0.5sin(C)) which ads to (perimeter - c)
        elif c != 0 and C != 0 and area != 0 and perimeter != 0:
            #ab is a*b found using the formula for area of a triangle
            ab = int(area/(0.5*math.sin(math.radians(C))))
            #list for the factors of ab
            factors = []
            #loop to find all the factors of ab and append to factors
            for i in range (1,ab+1):
                if ab % i == 0:
                    factors.append(i)
            #find how many factors there are
            length = len(factors)
            #loop for finding a pair of factors that add to make the perimeter - c
            for i in range(0,length):
                for x in range(0,length):
                    if factors[i]+factors[x] == perimeter - c and factors[i]*factors[x] == ab:
                        a = factors[i]
                        b = factors[x]
        #return the value of length a
        return a


#function to find a missing angle (A)
    def angle(a,b,c,A,B,C):
        #find A using the rule (a triangle has 180 degrees) therefore A + B + C = 180
        if B != 0 and C != 0:
            A = 180-(B+C)
        #find A using the cosine rule (cos(A)=b^+c^-a^/(2bc)
        elif a != 0 and b != 0 and c != 0:
            A = math.acos((b**2+c**2-a**2)/(2*b*c))*degrees
        #find A using the sine rule (sin(A) = sin(B)/b*a)
        elif b != 0 and B != 0 and a != 0:
            A = math.asin(((math.sin(math.radians(B)))/b)*a)*degrees
        #find A using the sine rule (sin(A) = sin(C)/c*a)
        elif c != 0 and C != 0 and a != 0:
            A = math.asin(((math.sin(math.radians(C)))/c)*a)*degrees
        #find A using the formula for area (area = 0.5bcsin(A)) rearranged to sin(A) = area/(0.5bc)
        elif area != 0 and b != 0 and c != 0:
            A = math.asin(area/(0.5*b*c))*degrees
        #return the value of angle A
        return A

  
#run the functions for each value that equals 0 (meaning that the value is unknown) to find the value
#this is in a loop so that the function has the values necessary (e.g: if value a cannot be found because value A in unknown, the next cycle of the loop will have the value of A)
#the arguments for each run of the function area rearranged to find the value of the correct attribute of the triangle
    for i in range(0,4):
        if a == 0:
            a = length(a,b,c,A,B,C)
        if b == 0:
            b = length(b,a,c,B,A,C)
        if c == 0:
            c = length(c,a,b,C,A,B)
        if A == 0:
            A = angle(a,b,c,A,B,C)
        if B == 0:
            B = angle(b,a,c,B,A,C)
        if C == 0:
            C = angle(c,a,b,C,A,B)
        if area == 0:
            #only one formula is needed for the area as all the other values should be known by now
            area = 0.5*b*c*math.sin(math.radians(A))
    #find the perimeter using the rule (the perimeter of a triangle = a + b + c)
    if perimeter == 0:
        perimeter = a+b+c

  
    #add the values of all the attributes to a triangle object (see triangle class in Triangle.py)
    triangle = Triangle(a,b,c,A,B,C,area,perimeter)
    #check to see if the triangle makes mathematical sense before running (0 degrees cannot exist in the triangle because it is not an angle, 180 degrees cannot be in a triangle because that would be a 2 sided object)
    if triangle.A >= 180 or triangle.B >= 180 or triangle.C >= 180 or triangle.A <= 0 or triangle.B <= 0 or triangle.C <= 0 or triangle.perimeter <= triangle.a or triangle.perimeter <= triangle.b or triangle.perimeter <= triangle.c or triangle.a > (triangle.b + triangle.c) or triangle.b > (triangle.a + triangle.c) or triangle.c > (triangle.a + triangle.b):
        print("\n\nInvalid triangle")
    else:
        #print the values of the triangle object
        triangle.print_values()
        #return the triangle object for drawing
        return triangle


#function for drawing the triangle
def drawtriangle(triangle):
    turtle.screensize(800,600)
    turtle.bgcolor("black")
    #find the mean length of the sides to understand the scale of the triangle
    mean = (triangle.a+triangle.b+triangle.c)/3


    #function for drawing the shape (multiplier is used to make the triangle a reasonable scale)
    def pencil(triangle, multiplier):
        pencil = turtle.Turtle()
        pencil.penup()
        pencil.speed(6)
        pencil.color("#ffe985")
        pencil.width(3)
        pencil.fillcolor("#85ffc2")
        pencil.goto(-200,-200)
        pencil.settiltangle(180)
        pencil.pendown()
        pencil.begin_fill()
        pencil.forward(triangle.b*multiplier)
        pencil.left(180-triangle.A)
        pencil.forward(triangle.c*multiplier)
        pencil.left(180-triangle.B)
        pencil.forward(triangle.a*multiplier)
        pencil.left(180-triangle.C)
        pencil.end_fill()
        def draw_angle(a,C):
            pencil.forward(a)
            pencil.left(180-C)
            pencil.begin_fill()
            if C == 90:
                pencil.forward(30)
                pencil.left(90)
                pencil.forward(30)
                pencil.left(90)
                pencil.forward(30)
                pencil.left(90)
                pencil.forward(30)
            else:
                pencil.forward(50)
                pencil.left(90)
                pencil.circle(50,C)
                pencil.left(90)
                pencil.forward(50)
            pencil.left(180-C)
            pencil.end_fill()
        draw_angle(triangle.b*multiplier,triangle.A)
        draw_angle(triangle.c*multiplier,triangle.B)
        draw_angle(triangle.a*multiplier,triangle.C)
        pencil.end_fill()
        pencil.hideturtle()

  
    #function for labelling the sides of the triangle
    def label(triangle, multiplier):
        label = turtle.Turtle()
        label.hideturtle()
        label.pencolor("#85ffc2")
        label.penup()
        label.speed(20)
        label.goto(-200,-200)
        #function for labelling one side of the triangle (multiplier is used again). The turtle object goes halfway the length of the line of the triangle and writes the name of the side, then goes the rest of the half of the side

  
        def label_one_side(name, b, A):
            label.forward(b)
            label.right(90)
            if name == "b":
                label.forward(30)
            else:
                label.forward(20)
            label.write(name, font=("Courier", 14, "normal"))
            label.right(180)
            label.forward(20)
            label.right(90)
            label.forward(b)
            label.left(180-A)

    
        #repeat the function for all the sides of the triangle
        label_one_side("b", (triangle.b*multiplier), triangle.A)
        label_one_side("c", (triangle.c*multiplier), triangle.B)
        label_one_side("a", (triangle.a*multiplier), triangle.C)


        #write the values of the triangle object in the output as well as the console
        label.penup()
        label.goto(-300, 200)
        label.write(str("\n\nLength a    =   "+str(round(triangle.a,6))
                        +"\nLength b    =   "+str(round(triangle.b,6))
                        +"\nLength c    =   "+str(round(triangle.c,6))
                        +"\nAngle A      =   "+str(round(triangle.A,6))
                        +"\nAngle B      =   "+str(round(triangle.B,6))
                        +"\nAngle C      =   "+str(round(triangle.C,6))
                        +"\nArea           =   "+str(round(triangle.area,6))
                        +"\nPerimeter  =   "+str(round(triangle.perimeter,6))))

  
    #400/mean is used as the multiplier to draw the triangle at the correct scale
    pencil(triangle, (400/mean))
    #200/mean is used as the multiplier to make the turtle object go half the length of the triangle (200/400 = 1/2)
    label(triangle, (200/mean))


#main code that boots the whole program
#try except is used to catch value errors by the user input (incorrect data type or invalid triangle ((a > b + c) or any other order)

while is_triangle_found == False:
    try:
        triangle = findtriangle()
        #check to see if the triangle makes mathematical sense before running (0 degrees cannot exist in the triangle because it is not an angle, 180 degrees cannot be in a triangle because that would be a 2 sided object)
        if triangle.A >= 180 or triangle.B >= 180 or triangle.C >= 180 or triangle.A <= 0 or triangle.B <= 0 or triangle.C <= 0 or triangle.perimeter <= triangle.a or triangle.perimeter <= triangle.b or triangle.perimeter <= triangle.c or triangle.a > (triangle.b + triangle.c) or triangle.b > (triangle.a + triangle.c) or triangle.c > (triangle.a + triangle.b):
            print("\n\nInvalid triangle")
        else:
            drawtriangle(triangle)
            #find the type of triangle
            if triangle.a == triangle.b or triangle.a == triangle.c or triangle.b == triangle.c:
                if triangle.a == triangle.b and triangle.b == triangle.c:
                    print("\n\nThis is an equilateral triangle")
                elif round(triangle.A,5) == 90 or round(triangle.B,5) == 90 or round(triangle.C,5) == 90:
                    print("\n\nThis is a right angle isosceles triangle")
                else:
                    print("\n\nThis is an isosceles triangle")
            elif triangle.A == 90 or triangle.B == 90 or triangle.C == 90:
                print("\n\nThis is a right angle triangle")
            else:
                print("\n\nThis is a scalene triangle")
            is_triangle_found = True
    except ValueError as x:
        print("\n\nInvalid triangle ("+str(x)+")\n\n")
    except Exception as y:
        print("\n\nsomething went wrong mate\n\n"+str(y)+"\n\n")
time.sleep(20)