
def tabla_de_verdad(funcion, resultado, resultado1, resultado2, resultado3):
    # Fuerza 0/1 si vienen True/False
    r1 = int(resultado)
    r2 = int(resultado1)
    r3 = int(resultado2)
    r4 = int(resultado3)

        # -------- Tabla de 1 columna --------
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
            selec = input("coloque 1 para colocarle el not al al primer valor \ncoloque 2 para colocarle el not al al segundo valor \ncoloque 3 para colocarle el not a ambos valores \n")
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
                funcion = "-p and q" if selec == 1 else ("p and -q" if selec == 2 else "-p and -q")
            else:
                resultado  = not(valor1) or not(valor2)
                resultado1 = not(valor1) or valor2
                resultado2 = valor1 or not(valor2)
                resultado3 = valor1 or valor2
                funcion = "-p or q" if selec == 1 else ("p or -q" if selec == 2 else "-p or -q")
        if idx == 1:
            funcion1 = funcion
            r00, r01, r10, r11 = int(resultado), int(resultado1), int(resultado2), int(resultado3)
        else:
            funcion2 = funcion
            resultado21, resultado22, resultado23, resultado24 = int(resultado), int(resultado1), int(resultado2), int(resultado3)
    titulo = f"{funcion1} / {funcion2}"
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
    Además indica si p y q son lógicamente equivalentes (p ≡ q).
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