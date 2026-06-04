# calculate area and perimeter of a rectangle
#input the value
length = int(input("enter length:"))
width = int(input("enter width :"))
#----------------------------------
#validate the input
if(length > 0 and width >0):
    area = length*width
    perimeter = 2*(length + width)
#displaying the area and perimeter
    print("Area =", area)
    print("perimeter =", perimeter)
#------------------------------
else:
    exit("the input is invalid")
