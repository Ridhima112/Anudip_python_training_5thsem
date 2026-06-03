#program to calculate area and perimeter of triangle
#intput of sides
print("-------- Triangle -------")
side1 = int(input("enter first side (in cm) : "))
side2 = int(input("enter second side (in cm) : "))
side3 = int(input("enter third side (in cm) : "))
#-------------------------------------------------
print("-------------------------------------------")
print("first side :",side1,"cm")
print("second side :",side2,"cm")
print("third side :",side3,"cm")
#to calculate perimeter
perimeter = side1 + side2 + side3
#-------------------------------------------------
s = perimeter / 2
#displaying area
print("Area : " , (s*(s-side1)*(s-side2)*(s-side3))**0.5 , "sq.cm")
#Displaying perimeter
print("perimeter : ",perimeter, "cm")


