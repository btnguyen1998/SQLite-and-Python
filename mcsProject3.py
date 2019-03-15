import math

class Triangle(object):
    s = 2
    def __init__(self,ax,ay,bx,by,cx,cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy


    def print_points(self):
        return "Triangle((%d, %d), (%d, %d), (%d, %d))" % (self.ax, self.ay, self.bx, self.by, self.cx, self.cy)

    def L1(self):
        return math.sqrt((self.bx-self.ax)**2+(self.by-self.ay)**2)

    def L2(self):
        return math.sqrt((self.cx-self.bx)**2+(self.cy-self.by)**2)

    def L3(self):
        return math.sqrt((self.ax-self.cx)**2+(self.ay-self.cy)**2)

    def Perimeter(self):
        return self.L1()+self.L2()+self.L3()

    def S(self):
        return self.Perimeter()/2

    def Area(self):
        return math.sqrt(self.S()*(self.S()-self.L1())*(self.S()-self.L2())*(self.S()-self.L3()))

    def Barycenter(self):
        return (self.ax+self.bx+self.cx)/3, (self.ay+self.by+self.cy)/3

    def LongestSide(self):
        side1 = self.L1()
        side2 = self.L2()
        side3 = self.L3()

        if side1 > side2 and side1 > side2:
            return self.L1()
        elif side2 > side1 and side2 > side3:
            return self.L2()
        else:
            return self.L3()

    def SmallSides(self):
        side1 = self.L1()
        side2 = self.L2()
        side3 = self.L3()

        if side1 > side3 and side1 > side3:
            return self.L2()**2+self.L3()**2
        elif side2 > side1 and side2 > side3:
            return self.L1()**2+self.L3()**2
        elif side3 > side1 and side3 > side2:
            return self.L1()**2+self.L2()**2
        else:
            pass

    def IsRightTriangle(self):
        long = math.floor(self.LongestSide()**2)
        long2 = self.LongestSide()**2
        long3 = math.ceil(self.LongestSide()**2)

        small = math.floor(self.SmallSides())
        small2 = self.SmallSides()
        small3 = math.ceil(self.SmallSides())

        if long == small or long == small2 or long == small3:
            return True
        elif long2 == small or long2 == small2 or long3 == small3:
            return True
        elif long3 == small or long2 == small2 or long == small3:
            return True
        else:
            return False

def main():

        P = Triangle(3,-5,15,4,-6,10)
        print(P.print_points())
        print("")
        print("AREA:", P.Area())
        print("")
        print("PERIMETER:", P.Perimeter())
        print("")
        print("BARYCENTER:", P.Barycenter())
        print("")
        print("LONGEST SIDE:", P.LongestSide())
        print("")
        print("RIGHT TRIANGLE:", P.IsRightTriangle())
        print("")
        print("Additonal Info if needed")
        print("")
        print("Side A:", P.L1())
        print("Side B:", P.L2())
        print("Side C:", P.L3())
        print("SemiPerimeter:", P.S())
        print("Sum of Squares of Other Two Sides:", P.SmallSides())
        print("Square of Longest Side:", P.LongestSide()**2)


main()