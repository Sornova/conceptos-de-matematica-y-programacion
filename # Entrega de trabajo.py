# Entrega de trabajo

import time, random
from funciones import *





menu_opciones = print(

    "MENU DE OPERACIONES" 
    "\n 1 Puertas Logicas Basicas"
    "\n 2 Conversion de Numeros"
    "\n 3 Contador Binario"
    "\n 4 Generador de Tabla de Verdad"
    "\n 5 Comparador de Expresiones Booleanas"
    "\n 6 Calculadora de Operaciones Bit a Bit"
    "\n 7 Simulador de Sumador de 1 Bit"
    "\n 8 Juego de Adivinanza en Binario"
    "\n 9 Circuito Combinacional Basico"
    "\n 10 Evaluador de Implicaciones y Contrarreciprocas"

    )





opcion = input("Escriba su opcion (1,2,3,...) -------> ")

opcion = int(opcion)


while True:

    if opcion == 1:

        print("\n=== Puertas Logicas Basicas ===")
        valor1 = input("Valor 1: Escriba 1 o 0 ----> ")
        valor2 = input("Valor 2: Escriba 1 o 0 ----> ")
        operador = input(
            "Operador:\n" \
            "1 = And \n" \
            "2 = or \n" \
            "3 = not\n"
        )

        operador= int(operador)

        valor1= int(valor1)

        valor2= int(valor2)


        if operador == 1:

            resultado = valor1 and valor2

            print(f"{valor1} and {valor2} = {resultado}")



        elif operador == 2:
            
            resultado = valor1 or valor2

            print("\n" * 100)
            print(f"{valor1} or {valor2} = {resultado}")



        elif operador == 3:

            selec = input("coloque 1 para colocarle el not al al primer valor \n" \
            "coloque 2 para colocarle el not al al segundo valor \n" \
            "coloque 3 para colocarle el not a ambos valores \n")

            operador = input( "Operador:\n" "1 = And \n" "2 = or \n" )


            
            selec = int(selec)
            operador = int(operador)



            if selec == 1:
                valor1 = not(valor1)
            
            elif selec == 2:
                valor2 = not(valor2)

            elif selec == 3:
                valor1 = not(valor1)
                valor2 = not(valor2)
            
            else:

                print("\n" * 100)
                print("opcion invalida")



            if operador == 1:

                resultado = valor1 and valor2

                print("\n" * 100)
                print(f"{valor1} and {valor2} = {resultado}")

            elif operador == 2:
            
                resultado = valor1 or valor2

                print("\n" * 100)
                print(f"{valor1} or {valor2} = {resultado}")
            
            else:

                print("\n" * 100)
                print("opcion invalida")
        
            
    elif opcion == 2:

        print("\n=== Conversión de Números ===")

        nmr = int(input("escriba un numero decimal "))

        resultado = 0

        resto = 0

        result_bin_lst = []


        if nmr == 0:

            binario = 0


        while nmr > 0:

            resto = nmr % 2
            nmr = nmr // 2
            result_bin_lst.append(str(resto))

            
        #rota la lista para que el binario quede ordenado
        result_bin_lst.reverse()
        binario = "".join(result_bin_lst)
        print("Binario:", binario)    


    elif opcion == 3:

        print("\n=== Contador Binario ===")

        for nmr in range(16):

            if nmr == 0:
                binario = "0000"

            else:
                resultado = nmr          
                result_bin_lst = []     


                while resultado > 0:
                    resto = resultado % 2
                    resultado = resultado // 2
                    result_bin_lst.append(str(resto))

                result_bin_lst.reverse()       
                binario = "".join(result_bin_lst)

            if len(binario) < 4:
                binario = ("0" * (4 - len(binario))) + binario

            print(f"{nmr} -> {binario}")
            time.sleep(0.3)

        opcion = input("Escriba su opcion (1,2,3,...) -------> ")

        
    elif opcion == 4:

        print("\n=== Generador de Tabla de Verdad ===")

        operador = input(
            "Operador:\n" \
            "1 = And \n" \
            "2 = or \n" \
            "3 = not\n"
        )

        operador= int(operador)
        valor1= 1
        valor2= 1


        if operador == 1:

            resultado = not(valor1) and not(valor2)
            resultado1 = not(valor1) and valor2
            resultado2 = valor1 and not(valor2)
            resultado3 = valor1 and valor2
            funcion = "p and q"

            tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)



        elif operador == 2:
            
            resultado = not(valor1) or not(valor2)
            resultado1 = not(valor1) or valor2
            resultado2 = valor1 or not(valor2)
            resultado3 = valor1 or valor2

            funcion = "p or q"

            print("\n" * 100)
            tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)



        elif operador == 3:

            selec = input("coloque 1 para colocarle el not al al primer valor \n" \
            "coloque 2 para colocarle el not al al segundo valor \n" \
            "coloque 3 para colocarle el not a ambos valores \n")

            operador = input( "Operador:\n" "1 = And \n" "2 = or \n" )


            
            selec = int(selec)
            operador = int(operador)



            if selec == 1:
                valor1 = 0

                resultado = not(valor1) or not(valor2)
                resultado1 = not(valor1) or valor2
                resultado2 = valor1 or not(valor2)
                resultado3 = valor1 or valor2    

                funcion = "-p and q"
                tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)            
            

            elif selec == 2:
                valor2 = 0

                resultado = not(valor1) or not(valor2)
                resultado1 = not(valor1) or valor2
                resultado2 = valor1 or not(valor2)
                resultado3 = valor1 or valor2 

                funcion = "p and -q"
                tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)


            elif selec == 3:
                valor1 = 0
                valor2 = 0

                resultado = not(valor1) or not(valor2)
                resultado1 = not(valor1) or valor2
                resultado2 = valor1 or not(valor2)
                resultado3 = valor1 or valor2 

                funcion = "-p and -q"
                tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)


    elif opcion == 5:
        cal_tabla_verdad()
        opcion = input("Escriba su opcion (1,2,3,...) -------> ")

    elif opcion == 6:

        valor1 = int(input("Ingrese el primer número: "))
        valor2 = int(input("Ingrese el segundo número: "))

        resultado_and = valor1 & valor2
        and_bin = "0"

        resultado_or = valor1 | valor2
        or__bin = "0"

        resultado_xor = valor1 ^ valor2
        xor_bin = "0"

    

        print(f"{valor1} and {valor2} = {resultado_and}   bin: {numero_binario(resultado_and)}")
        print(f"{valor1} or {valor2}  = {resultado_or}   bin: {numero_binario(resultado_or)}")
        print(f"{valor1} xor {valor2} = {resultado_xor}   bin: {numero_binario(resultado_xor)}")


    elif opcion == 7:
        A = int(input("Ingrese el primer bit (0 o 1): "))
        B = int(input("Ingrese el segundo bit (0 o 1): "))

        # Lógica booleana
        Suma = (A and not B) or (not A and B)   # XOR implementado sin operador
        Carry = A and B

        print("Resultado de la suma:")
        print("Bit de suma (S):", int(Suma))
        print("Carry (C):", int(Carry))

    elif opcion == 8:

        nmr_random = random.randint(1,31)
        numero_bin = numero_binario(nmr_random)

        print(numero_bin)

        respuesta = int(input("Coloque el equivalente al numero anterior "))

        if respuesta == nmr_random:
            print("Respuesta correcta")

        else:
            print("Respuesta incorrecta")

    else:
        break





























































