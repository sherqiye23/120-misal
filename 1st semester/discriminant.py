while True:
    x = input("Discriminant və kökləri hesablayassızsa hə, olmasa yox yazınız: ")
    if x == "hə":
        a = float(input("a nın qiymətini yazin: "))
        b = float(input("b nin qiymətini yazin: "))
        c = float(input("c nin qiymətini yazin: "))
        def discriminant(a, b, c):

           discriminant = b**2 - 4*a*c

           x1 = (-b + (discriminant**(1/2)))/(2*a)
           x2 = (-b - (discriminant**(1/2)))/(2*a)


           print("x1: ", x1)
           print("x2: ", x2)
           print("Discriminant: ", discriminant)

           if discriminant > 0:
            print("kökləri: ", x1 , x2)

           elif discriminant == 0:
            print("kökü", x1)
        
           elif discriminant < 0:
            print("kökü yoxdur.")
        discriminant(a, b, c)


    elif x == "yox":
        print("Salaaamat")
        break