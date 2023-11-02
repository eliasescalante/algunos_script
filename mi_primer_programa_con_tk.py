import tkinter as tk
from tkinter import *

#FUNCIONES

def es_bisiesto_(fecha):
  # indica si el año ingresado por parametro es bisiesto o no.
  # si es divisible por 400 o 4 y no por 100 entonces es bisiesto.
  # el argumento que recibe el parametro tiene que ser un numero con formato de año
    if es_divisible_por_400(fecha) or es_divisible_por_4_y_no_por_100(fecha):
        print("Es bisiesto")
        return "Es bisiesto"
    else:
        print ("No es Bisiesto")
        return "No es bisiesto"

def es_divisible_por_400(fecha):
  # indica si el año ingresado es divisible por 400 en caso que lo sea devuelve TRUE
    return fecha % 400 == 0

def es_divisible_por_4_y_no_por_100(fecha):
  # indica si el año es divisible por 4 y no es divisible por 100
    return fecha % 4 == 0 and not fecha % 100 == 0

def validando_el_ingreso(fecha):
  # valido el año ingresado para luego evaluar si es bisiesto o no.
    if fecha.isnumeric():
        anio = int(fecha)
        return es_bisiesto_(anio)
    else:
        print("el año ingresado no es valido...")
        return "el año ingresado no es valido..."

def validar():
    numero1 = numero.get()
    titulo2.config(text=validando_el_ingreso(numero1))

#INTERFAZ GRAFICA

# // VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Año Bisiesto")
ventana.geometry("300x200")
ventana.configure(bg="white")

# Variables para trabajar

numero = StringVar()
resultado=StringVar()

# Cuadro de entrada año
titulo1 = Label(ventana,text="Ingrese el año a evaluar: ",bg="white")
titulo1.pack()
entrada1 = Entry(ventana,textvariable=numero)
entrada1.pack()

# #cuadro de resultado
titulo2 = Label(ventana,text="Resultado: ",bg="white")
titulo2.pack()
salida1 = Message(ventana, textvariable=resultado ,width=58 )

# #creacion del boton
boton = Button ( ventana, text ="Evaluar", command=validar)
boton.pack()
# # Start the event loop
ventana.mainloop()
