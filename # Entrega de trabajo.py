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
    "\n 11 Generador Doble Implicacion"
    "\n 12 Clasificador de Proposiciones Compuestas"

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

    elif opcion == 9:

        print("\n=== Circuito Combinacional Básico (Par / Impar) ===")
        print("Este circuito decide si un número es PAR o IMPAR según su último bit en binario.\n")

        tipo = input("¿Cómo querés ingresar el número?\n 1 - En decimal\n 2 - En binario\n ---> ")

        if tipo == "1":
            decimal = int(input("Ingrese un número decimal no negativo: "))
            if decimal < 0:
                print("Solo se aceptan números no negativos.")
                continue
            bin_str = numero_binario(decimal)

        elif tipo == "2":
            bin_str = input("Ingrese el número en binario (solo 0 y 1): ")
            try:
                validar_binario_str(bin_str)
            except ValueError as e:
                print("Error:", e)
                continue

            decimal = int(bin_str, 2)

        else:
            print("Opción inválida.")
            continue

        par = es_par_binario(bin_str)
        impar = es_impar_binario(bin_str)

        print(f"\nNúmero decimal: {decimal}")
        print(f"Número binario: {bin_str}")

        if par == 1:
            print("Resultado del circuito: EL NÚMERO ES PAR (último bit = 0).")
        else:
            print("Resultado del circuito: EL NÚMERO ES IMPAR (último bit = 1).")


    elif opcion == 10:

            print("\n=== Evaluador de Implicaciones y Contrarrecíprocas ===")

            p_usuario = int(input("Ingrese valor de p (0 o 1): "))
            q_usuario = int(input("Ingrese valor de q (0 o 1): "))

            # Normalizamos a booleanos
            p_bool = bool(p_usuario)
            q_bool = bool(q_usuario)

            # p ⇒ q  es equivalente a  (not p) or q
            imp_usuario = (not p_bool) or q_bool

            # ¬q ⇒ ¬p  es equivalente a  (not (not q)) or (not p) = q or (not p)
            contra_usuario = q_bool or (not p_bool)

            print(f"\nPara p = {p_usuario}, q = {q_usuario}:")
            print(f"p ⇒ q        = {int(imp_usuario)}")
            print(f"¬q ⇒ ¬p      = {int(contra_usuario)}")

            # Ahora generamos la tabla de verdad completa
            print("\nTabla de verdad de p ⇒ q y ¬q ⇒ ¬p:")
            print("-------------------------------------------")
            print("|  p  |  q  |  p⇒q  |  ¬q⇒¬p  |")
            print("-------------------------------------------")

            equivalentes = True

            for p in (0, 1):
                for q in (0, 1):
                    p_b = bool(p)
                    q_b = bool(q)

                    imp = (not p_b) or q_b          # p ⇒ q
                    contra = q_b or (not p_b)       # ¬q ⇒ ¬p

                    if imp != contra:
                        equivalentes = False

                    print(f"|  {p}  |  {q}  |   {int(imp)}   |    {int(contra)}    |")

            print("-------------------------------------------")

            if equivalentes:
                print("Conclusión: p⇒q y ¬q⇒¬p son lógicamente equivalentes.")
            else:
                print("Conclusión: p⇒q y ¬q⇒¬p NO son lógicamente equivalentes.")


    elif opcion == 11:
        tabla_doble_implicacion()

    elif opcion == 12:
        clasificar_proposicion_compuesta()

    else:
        break

    




























































