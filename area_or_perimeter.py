#Finding area or perimeter of the shapes in the list given below by user choice.

shapes=["circle","triangle","square","rectangle"]
#triangle in the list is a "equilateral" triangle
print(shapes)
shape_user=input("Choose the shape you want from the list (data as santimeter): ")

while True:

    if shape_user =="circle" or shape_user=="circle":
        pi=3.14
        r=int(input("Enter the radius of the circle: "))
        opt=input("Choose one: area (1) perimeter(2) ")

        
        if opt=="1":
            area=pi*r*r
            area_circle="Area of the circle with {} radius: {}"
            print(area_circle.format(r,area))
            break

        elif opt=="2":
            peri=2*pi*r
            peri_circle="Perimeter of the circle with {} radius: {}"
            print(peri_circle.format(r,peri))
            break

        else:
            print("Invalid option!")
            break


    elif shape_user=="square" or shape_user=="square":
        a=int(input("Enter the one side of the square: "))

        opt=input("Choose one: area(1) perimeter(2) ")
        if opt=="1":
            area=a*a
            area_square="Area of the square: {}"
            print(area_square.format(area))
            break
        
        elif opt=="2":
            peri=4*a
            peri_square="Perimeter of the square: {}"
            print(peri_square.format(peri))
            break

        else:
            print("Invalid option!")
            break


    elif shape_user=="rectangle" or shape_user=="rectangle":
        long=int(input("Enter the long side of the rectangle: "))
        short=int(input("Enter the short side of the rectangle: "))

        opt=input("Choose one: area(1) perimeter(2) ")

        if opt=="1":
            area=long*short
            area_rect="Area of the rectangle: {}"
            print(area_rect.format(area))
            break

        elif opt=="2":
            peri=2*(long+short)
            peri_rect="Perimeter of the rectangle: {}"
            print(peri_rect.format(peri))
            break

        else:
            print("Invalid option!")
            break


    elif shape_user=="triangle" or shape_user==" triangle":
        side=int(input("Enter one side of the triangle: "))
        area= 0.43*side              #(√3 / 4)*kenar 

        opt=input("Choose one: area(1) perimeter(2) ")

        if opt=="1":
            area_tri="Area of the triangle: {}"
            print(area_tri.format(area))
            break

        if opt=="2":
            peri=3*side
            print(("Perimeter of the triangle: {}").format(peri))
            break

        else:
            print("Invalid option!")
            break
        
    else:
        print("Shape is out of the list! \n")
        print(shapes)
        print("Please choose one in the list: ")
        shape_user=input()
        continue

        


 


