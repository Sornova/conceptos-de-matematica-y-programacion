# Entrega de trabajo

import time
import random

# =========================
#        FUNCIONES
# =========================

def tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3):
    # Fuerza 0/1 si vienen True/False
    r1 = int(resultado)
    r2 = int(resultado1)
    r3 = int(resultado2)
    r4 = int(resultado3)

    tabla = (
        "-------------------------------\n"
        f"|    p    |    q    | {funcion} |\n"
        "|------------------------------\n"
        f"|    0    |    0    |    {r1}    |\n" 
        "|------------------------------\n"
        f"|    0    |    1    |    {r2}    |\n"
        "|------------------------------\n"
        f"|    1    |    0    |    {r3}    |\n"
        "|------------------------------\n"
        f"|    1    |    1    |    {r4}    |\n"
        "-------------------------------"
    )

    print(tabla)


def tabla_de_verdad1(funcion1, resultado, resultado1, resultado2, resultado3, resultado21, resultado22, resultado23, resultado24, funcion2=None):

    if funcion2 is None:
        funcion2 = funcion1

    r1 = int(resultado)
    r2 = int(resultado1)
    r3 = int(resultado2)
    r4 = int(resultado3)

    r21 = int(resultado21)
    r22 = int(resultado22)
    r23 = int(resultado23)
    r24 = int(resultado24)

    tabla = (
        "-------------------------------------------\n"
        f"|    p    |    q    | {funcion1} | {funcion2} |\n"
        "|------------------------------------------\n"
        f"|    0    |    0    |    {r1}    |    {r21}      |\n"
        "|------------------------------------------\n"
        f"|    0    |    1    |    {r2}    |    {r22}      |\n"
        "|------------------------------------------\n"
        f"|    1    |    0    |    {r3}    |    {r23}      |\n"
        "|------------------------------------------\n"
        f"|    1    |    1    |    {r4}    |    {r24}      |\n"
        "-------------------------------------------\n"
    )
    print(tabla)


def cal_tabla_verdad(funcion=None, resultado=None, resultado1=None, resultado2=None, resultado3=None):

    r00 = r01 = r10 = r11 = 0
    resultado21 = resultado22 = resultado23 = resultado24 = 0
    funcion1 = ""
    funcion2 = ""

    for idx in (1, 2):
        if idx == 1:
            print("\n-- Primera expresión --")
        else:
            print("\n-- Segunda expresión --")

        operador = input("Operador:\n1 = And \n2 = or \n3 = not\n")
        operador = int(operador)
        valor1 = 1
        valor2 = 1

        if operador == 1:
            resultado  = not(valor1) and not(valor2)
            resultado1 = not(valor1) and valor2
            resultado2 = valor1 and not(valor2)
            resultado3 = valor1 and valor2
            funcion = "p and q"

        elif operador == 2:
            resultado  = not(valor1) or not(valor2)
            resultado1 = not(valor1) or valor2
            resultado2 = valor1 or not(valor2)
            resultado3 = valor1 or valor2
            funcion = "p or q"

        elif operador == 3:
            selec = input(
                "coloque 1 para colocarle el not al al primer valor \n"
                "coloque 2 para colocarle el not al al segundo valor \n"
                "coloque 3 para colocarle el not a ambos valores \n"
            )
            operador2 = input("Operador:\n1 = And \n2 = or \n")
            selec = int(selec)
            operador2 = int(operador2)

            if selec == 1:
                valor1 = 0
            elif selec == 2:
                valor2 = 0
            elif selec == 3:
                valor1 = 0
                valor2 = 0

            if operador2 == 1:
                resultado  = not(valor1) and not(valor2)
                resultado1 = not(valor1) and valor2
                resultado2 = valor1 and not(valor2)
                resultado3 = valor1 and valor2
                funcion = "-p and q" if selec == 1 else ( "p and -q" if selec == 2 else "-p and -q")
            else:
                resultado  = not(valor1) or not(valor2)
                resultado1 = not(valor1) or valor2
                resultado2 = valor1 or not(valor2)
                resultado3 = valor1 or valor2
                funcion = "-p or q" if selec == 1 else ( "p or -q" if selec == 2 else "-p or -q")

        if idx == 1:
            funcion1 = funcion
            r00, r01, r10, r11 = int(resultado), int(resultado1), int(resultado2), int(resultado3)
        else:
            funcion2 = funcion
            resultado21, resultado22, resultado23, resultado24 = int(resultado), int(resultado1), int(resultado2), int(resultado3)

    tabla_de_verdad1(funcion1, r00, r01, r10, r11, resultado21, resultado22, resultado23, resultado24, funcion2=funcion2)


def numero_binario(nmr):
    if nmr == 0:
        return "0"
    result_bin_lst = []
    while nmr > 0:
        resto = nmr % 2
        nmr = nmr // 2
        result_bin_lst.append(str(resto))
    result_bin_lst.reverse()
    return "".join(result_bin_lst)


def validar_binario_str(bin_str):
    if not isinstance(bin_str, str) or len(bin_str) == 0:
        raise ValueError("Entrada inválida: se espera una cadena binaria no vacía (str).")
    for c in bin_str:
        if c not in ("0", "1"):
            raise ValueError("Entrada inválida: la cadena debe contener solo '0' y '1'.")


def es_par_binario(bin_str):
    validar_binario_str(bin_str)
    ultimo_bit = bin_str[-1]
    return 1 if ultimo_bit == "0" else 0


def es_impar_binario(bin_str):
    return 1 - es_par_binario(bin_str)


def tabla_doble_implicacion():
    """
    Genera la tabla de verdad de p <-> q (p si y solo si q)
    y destaca las filas donde el resultado es verdadero.
    Además indica si p y q son equivalentes lógicas (p ≡ q).
    """
    print("\n=== Tabla de verdad de p ⇔ q ===")
    print("--------------------------------------------")
    print("|  p  |  q  |  p⇔q  |  Marcar (verdadero)  |")
    print("--------------------------------------------")

    equivalentes = True  # Para ver si p y q tienen siempre el mismo valor

    for p in (0, 1):
        for q in (0, 1):
            p_bool = bool(p)
            q_bool = bool(q)

            # p ⇔ q es verdadero cuando ambos tienen el mismo valor
            eq_bool = (p_bool and q_bool) or ((not p_bool) and (not q_bool))
            eq = int(eq_bool)

            # Para equivalencia lógica, p y q deberían coincidir SIEMPRE
            if p != q:
                equivalentes = False

            marca = "*" if eq == 1 else ""
            print(f"|  {p}  |  {q}  |   {eq}   |        {marca:2}              |")

    print("--------------------------------------------")

    if equivalentes:
        print("Conclusión: p y q son equivalentes lógicas (p ≡ q).")
    else:
        print("Conclusión: p y q NO son equivalentes lógicas (hay filas donde difieren).")


def clasificar_proposicion_compuesta():
    """
    Permite elegir una proposición compuesta estándar
    y la clasifica como tautología, contradicción o contingencia.
    Además muestra la tabla de verdad.
    """
    print("\n=== Clasificador de Proposiciones Compuestas ===")
    print("Elija una proposición:")
    print("1 - p ∨ ¬p")
    print("2 - p ∧ ¬p")
    print("3 - p ⇒ q")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = "p ∨ ¬p"

        def formula(p, q):
            p_bool = bool(p)
            return int(p_bool or (not p_bool))  # q no se usa

    elif opcion == "2":
        nombre = "p ∧ ¬p"

        def formula(p, q):
            p_bool = bool(p)
            return int(p_bool and (not p_bool))  # q no se usa

    elif opcion == "3":
        nombre = "p ⇒ q"

        def formula(p, q):
            p_bool = bool(p)
            q_bool = bool(q)
            return int((not p_bool) or q_bool)
    else:
        print("Opción inválida.")
        return

    print(f"\nTabla de verdad para: {nombre}")
    print("-------------------------------------")
    print("|  p  |  q  |  ", nombre, " |")
    print("-------------------------------------")

    resultados = []

    for p in (0, 1):
        for q in (0, 1):
            r = formula(p, q)
            resultados.append(r)
            print(f"|  {p}  |  {q}  |      {r}       |")

    print("-------------------------------------")

    # Clasificación
    if all(r == 1 for r in resultados):
        print("Clasificación: TAUTOLOGÍA (siempre verdadera).")
    elif all(r == 0 for r in resultados):
        print("Clasificación: CONTRADICCIÓN (siempre falsa).")
    else:
        print("Clasificación: CONTINGENCIA (verdadera en algunas filas y falsa en otras).")


# =========================
#        PROGRAMA
# =========================

while True:
    print(
        "\nMENU DE OPERACIONES"
        "\n 0 Salir"
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

    opcion = input("Escriba su opcion (0,1,2,3,...) -------> ")

    if opcion == "0":
        print("Saliendo...")
        break

    # ================= OPCIÓN 1 =================
    if opcion == "1":
        print("\n=== Puertas Logicas Basicas ===")
        valor1 = int(input("Valor 1: Escriba 1 o 0 ----> "))
        valor2 = int(input("Valor 2: Escriba 1 o 0 ----> "))
        operador = int(input(
            "Operador:\n"
            "1 = And \n"
            "2 = or \n"
            "3 = not\n"
        ))

        if operador == 1:
            resultado = valor1 and valor2
            print(f"{valor1} and {valor2} = {resultado}")

        elif operador == 2:
            resultado = valor1 or valor2
            print("\n" * 2)
            print(f"{valor1} or {valor2} = {resultado}")

        elif operador == 3:
            selec = input(
                "coloque 1 para colocarle el not al primer valor \n"
                "coloque 2 para colocarle el not al segundo valor \n"
                "coloque 3 para colocarle el not a ambos valores \n"
            )

            operador2 = input("Operador:\n1 = And \n2 = or \n")

            selec = int(selec)
            operador2 = int(operador2)

            if selec == 1:
                valor1 = not(valor1)
            elif selec == 2:
                valor2 = not(valor2)
            elif selec == 3:
                valor1 = not(valor1)
                valor2 = not(valor2)
            else:
                print("opcion invalida")
                continue

            if operador2 == 1:
                resultado = valor1 and valor2
                print(f"{valor1} and {valor2} = {resultado}")
            elif operador2 == 2:
                resultado = valor1 or valor2
                print(f"{valor1} or {valor2} = {resultado}")
            else:
                print("opcion invalida")

    # ================= OPCIÓN 2 =================
    elif opcion == "2":
        print("\n=== Conversión de Números ===")
        nmr = int(input("escriba un numero decimal "))

        result_bin_lst = []

        if nmr == 0:
            binario = "0"
        else:
            while nmr > 0:
                resto = nmr % 2
                nmr = nmr // 2
                result_bin_lst.append(str(resto))

            result_bin_lst.reverse()
            binario = "".join(result_bin_lst)

        print("Binario:", binario)

    # ================= OPCIÓN 3 =================
    elif opcion == "3":
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

    # ================= OPCIÓN 4 =================
    elif opcion == "4":
        print("\n=== Generador de Tabla de Verdad ===")

        operador = int(input(
            "Operador:\n"
            "1 = And \n"
            "2 = or \n"
            "3 = not\n"
        ))

        valor1 = 1
        valor2 = 1

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
            tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)

        elif operador == 3:
            selec = input(
                "coloque 1 para colocarle el not al primer valor \n"
                "coloque 2 para colocarle el not al segundo valor \n"
                "coloque 3 para colocarle el not a ambos valores \n"
            )
            operador2 = input("Operador:\n1 = And \n2 = or \n")
            selec = int(selec)
            operador2 = int(operador2)

            if selec == 1:
                valor1 = 0
                funcion = "-p and q"
            elif selec == 2:
                valor2 = 0
                funcion = "p and -q"
            elif selec == 3:
                valor1 = 0
                valor2 = 0
                funcion = "-p and -q"
            else:
                print("opcion invalida")
                continue

            resultado = not(valor1) or not(valor2)
            resultado1 = not(valor1) or valor2
            resultado2 = valor1 or not(valor2)
            resultado3 = valor1 or valor2
            tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3)

    # ================= OPCIÓN 5 =================
    elif opcion == "5":
        cal_tabla_verdad()

    # ================= OPCIÓN 6 =================
    elif opcion == "6":
        valor1 = int(input("Ingrese el primer número: "))
        valor2 = int(input("Ingrese el segundo número: "))

        resultado_and = valor1 & valor2
        resultado_or = valor1 | valor2
        resultado_xor = valor1 ^ valor2

        print(f"{valor1} and {valor2} = {resultado_and}   bin: {numero_binario(resultado_and)}")
        print(f"{valor1} or {valor2}  = {resultado_or}   bin: {numero_binario(resultado_or)}")
        print(f"{valor1} xor {valor2} = {resultado_xor}   bin: {numero_binario(resultado_xor)}")

    # ================= OPCIÓN 7 =================
    elif opcion == "7":
        A = int(input("Ingrese el primer bit (0 o 1): "))
        B = int(input("Ingrese el segundo bit (0 o 1): "))

        # Lógica booleana
        Suma = (A and not B) or (not A and B)   # XOR implementado sin operador
        Carry = A and B

        print("Resultado de la suma:")
        print("Bit de suma (S):", int(Suma))
        print("Carry (C):", int(Carry))

    # ================= OPCIÓN 8 =================
    elif opcion == "8":
        nmr_random = random.randint(1, 31)
        numero_bin = numero_binario(nmr_random)

        print("Número en binario:", numero_bin)

        respuesta = int(input("Coloque el equivalente decimal del número anterior: "))

        if respuesta == nmr_random:
            print("Respuesta correcta")
        else:
            print(f"Respuesta incorrecta, era {nmr_random}")

    # ================= OPCIÓN 9 =================
    elif opcion == "9":
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

    # ================= OPCIÓN 10 =================
    elif opcion == "10":
        print("\n=== Evaluador de Implicaciones y Contrarrecíprocas ===")

        p_usuario = int(input("Ingrese valor de p (0 o 1): "))
        q_usuario = int(input("Ingrese valor de q (0 o 1): "))

        # Normalizamos a booleanos
        p_bool = bool(p_usuario)
        q_bool = bool(q_usuario)

        # p ⇒ q  es equivalente a  (not p) or q
        imp_usuario = (not p_bool) or q_bool

        # ¬q ⇒ ¬p  es equivalente a  q or (not p)
        contra_usuario = q_bool or (not p_bool)

        print(f"\nPara p = {p_usuario}, q = {q_usuario}:")
        print(f"p ⇒ q        = {int(imp_usuario)}")
        print(f"¬q ⇒ ¬p      = {int(contra_usuario)}")

        # Tabla de verdad completa
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

    # ================= OPCIÓN 11 =================
    elif opcion == "11":
        tabla_doble_implicacion()

    # ================= OPCIÓN 12 =================
    elif opcion == "12":
        clasificar_proposicion_compuesta()

    else:
        print("Opción inválida, intentá de nuevo.")
