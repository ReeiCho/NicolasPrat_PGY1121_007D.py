import os
import time
import numpy

def mostrar_menu():
    print("""MENU
    1.Comprar departamento
    2.Mostrar departamentos disponibles
    3.Ver listado de compradores
    4.Mostrar ganancias totales
    5.Salir
    """)

def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese opcion: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! OPCION INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO!")

lista_rut=[]
lista_pisos=[10,9,8,7,6,5,4,3,2,1]
lista_letras=['A','B','C','D','a','b','c','d']

tipo_a= 3800
tipo_b= 3000
tipo_c= 2800
tipo_d= 3500

def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su rut del comprador(sin puntos ni digito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                print("LA OPERACION SE REALIZO CORRECTAMENTE!")
                lista_rut.append(rut)
                time.sleep(3)
                mensaje_salida()
                time.sleep(3)
                edificio[validar_piso,validar_tipo_depto]+=1
                mensaje_salida()
                return rut
            else:
                print("ERROR! EL RUT DEBE SER MAYOR QUE 1000000 Y MENOR QUE 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO!")
            
def mensaje_salida():
    print("Gracias por su visita... /Nicolas Prat 14/07")

edificio=numpy.zeros((10,4),int)

def mostrar_departamentos():
    for x in range (10):
        print("Piso",lista_pisos[x])
        for y in range (4):
            print(lista_letras[y],edificio[x][y], end=" ")
            print()
    
        
def mostrar_disponibles():
    if 0 not in edificio:
        print("NO HAY DEPARTAMENTOS DISPONIBLES")
        time.sleep(3)
        return
    else:
        mostrar_departamentos()

def comprar_departamento():
    mostrar_disponibles()
    
def validar_piso():
    while True:
        piso=int(input("Ingrese piso: "))
        if piso in (1,2,3,4,5,6,7,8,9,10):
            return piso
        else:
            print("ERROR! Piso incorrecto!")
            

def validar_tipo_depto():
        while True:
            tipo_depto=input("Ingrese tipo de departamento: ")
            if tipo_depto not in lista_letras:
                print("ERROR! LOS TIPOS DE DEPARTAMENTO SON A,B,C,D")
            else:
                return tipo_depto
            
                
def precios_deptos():
    print("""
    TIPO A= 3800 UF
    TIPO B= 3000 UF
    TIPO C= 2800 UF
    TIPO D= 3500 UF""")
    time.sleep(2)
    

                 
def ventas_totales():
    total_a=(tipo_a*lista_letras['A']or['a'])
    total_b=(tipo_b*lista_letras['B']or['b'])
    total_c=(tipo_c*lista_letras['C']or['c'])
    total_d=(tipo_d*lista_letras['D']or['d'])
    total=total_a+total_b+total_c+total_d
    cantidad=lista_letras['A']+lista_letras['B']+lista_letras['C']+lista_letras['D']
    print(f"""
    TIPO DEPTO  |CANTIDAD  | TOTAL
    _____________________________
    TipoA = {tipo_a}UF |{lista_letras['A']or['a']}|{total_a}
    TipoB = {tipo_b}UF |{lista_letras['B']or['b']}|{total_b}
    TipoC = {tipo_c}UF |{lista_letras['C']or['c']}|{total_c}
    TipoD = {tipo_d}UF |{lista_letras['D']or['d']}|{total_d}
    ___________________________________________
    TOTAL    |{cantidad}  |{total}UF
    """)