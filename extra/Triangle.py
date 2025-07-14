class Triangle:
    def __init__(self, sidea, sideb, sidec, angleA, angleB, angleC, area, perimeter):
        self.a = sidea
        self.b = sideb
        self.c = sidec
        self.A = angleA
        self.B = angleB
        self.C = angleC
        self.area = area
        self.perimeter = perimeter
    def print_values(triangle):
        print("\n\nLength a   =   "+str(round(triangle.a,6))
              +"\nLength b   =   "+str(round(triangle.b,6))
              +"\nLength c   =   "+str(round(triangle.c,6))
              +"\nAngle A    =   "+str(round(triangle.A,6))
              +"\nAngle B    =   "+str(round(triangle.B,6))
              +"\nAngle C    =   "+str(round(triangle.C,6))
              +"\nArea       =   "+str(round(triangle.area,6))
              +"\nPerimeter  =   "+str(round(triangle.perimeter,6)))