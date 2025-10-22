from datetime import datetime
hoy = datetime.today()
try:
    year=int(input("Escribe tu año de nacimiento: "))
    if year < 0:
        raise Exception("El año no puede ser menor a 0")
    if year>hoy.year:
        raise Exception("No puedes haber nacido en el futuro")
except Exception as e:
    print(e)
else:
    years = hoy.year - year
    print(f"Naciste hace {years} años")
finally:
    print("Acaba sin error o con error")
