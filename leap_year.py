def leap_year():
    YEAR = int(input("Ingrese un año: "))
    B4 = YEAR % 4
    B400 = YEAR % 400
    CENTURY = YEAR % 100
    if B4 == 0 and CENTURY>0:
        print(f"El año {YEAR} es bisiesto")
    elif CENTURY == 0 and B400 == 0:
        print(f"El año {YEAR} es bisiesto")
    else:
        print(f"El año {YEAR} no es bisiesto")

