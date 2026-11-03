print("Seleccione su medida de conversion")
x = input("1.Pulgadas a Centimetro \n2.Milimetro a Pulgadas \n3.Fahrenheit a Celcius \n4.Celcius a Fahremheit\n")

match x:
    case "1":
        print("Pulgadas a milimetros")
        mm = 25.4
        P = float(input("Pon las pulgadas aqui, debes poner . y no , "))
        S = P * mm
        S = round(S , 2)
        print(S, "mm")
    case "2":
        print("Milimetros a pulgadas")
        pulgadas = 25.4
        milimetros = float(input("Pon los milimetros aqui, debes poner . y no , "))
        S = milimetros / pulgadas
        S = round(S , 2)
        print(S, "p")
    case "3":
        print("Fahrenheit a Celcius")
        Celcius = 32
        Fahrenheit = float(input("Pon los Fahrenheit aqui, debes poner . y no , "))
        Solution = Fahrenheit - Celcius
        S = Solution * 5 / 9
        S = round(S, 2)
        print(S, "C")
    case "4":
        print("Celcius a Fahrenheit ")
        F = 32
        C = float(input("Pon los Celcius aqui, debes poner . y no , "))
        S = C * 9 / 5 + F 
        S = round(S,2)
        print (S ,"F")
    case _:
        print("Incorrecto")
        


