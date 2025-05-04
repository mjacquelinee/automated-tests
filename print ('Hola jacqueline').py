from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=r"C:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://pyton.org")
driver.close()


"""""
Persona = {"Nombre": "Mayra" , "Edad": 64, "Estatura" : 1.65, "Estudiante" : False}

print (Persona ["Nombre"])

Frutas = {"Manzana", "Fresa", "Naranja", "Mango"}

print(Frutas)

Frutas.discard ("Fresa")
print(Frutas)

if Edad < 18: 
    print("Eres menor de edad")
if Edad >= 18 and Edad < 60:
    print("Eres Adulto")
if Edad > 60:
    print("Eres Adulto Mayor")

   Frutas = ["Manzana", "Fresa", "Naranja", "Mango"]

    for Fruta in Frutas:
        print (Fruta)

Contador = 0
while Contador < 5 :
    print (Contador)
    Contador +=1


for numero in range (1,6):
    print(numero * 2)

    Frutas.append ("Platano")
    print (Frutas)

Frutas.insert(1, "Uva")
print (Frutas)



def saludo( nombre) :
    print(f"hola, {nombre}")

saludo("mayra")

def suma(a,b):
    return a+b
resultado= suma(3,4)
print(f"El resultado es : {resultado}")


nombre = input("ingresa tu nombre :")
edad = input("ingresa tu edad :")

print("tu nombre "+nombre+ "!")
print("Tienes" +edad+ "anos")

"""