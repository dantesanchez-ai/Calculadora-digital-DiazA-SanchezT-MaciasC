"""
Calculadora Multifuncional Interactiva - Versión Avanzada
Proyecto de Tecnología Digital

Equipo:
- Estudiante 1: [Jorge Diaz Abarca] - Estructura Principal y Gestión de Datos
- Estudiante 2: [Dante Joaquin Sanchez] - Funciones Matemáticas
- Estudiante 3: [Luis Ignacio Masias] - Conversores y Sistema de Historial

Fecha: Febrero 2026
Universidad de Guadalajara - Campus GDL
"""

import os
from datetime import datetime

# Variable global para almacenar historial (lista de strings)
historial = []

# ============================================
# SECCIÓN 1: FUNCIONES MATEMÁTICAS (Estudiante 2)
# ============================================

def sumar(a, b):
    """Suma dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la suma
    """

    return a + b


def restar(a, b):
    """
    Resta dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la resta
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Args:
        a (float): Primer número
        b (float): Segundo número

    Returns:
        float: Resultado de la multiplicación
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Resultado de la división
        None: Si b es cero

    Raises:
        None: Retorna None en lugar de lanzar excepción
    """
    if b == 0:
        return None
    # Verificar que b no sea cero
    # Si b == 0, retornar None
    # Si no, retornar a / b
    else:
        return a/b


def modulo(a, b):
    """
    Calcula el módulo (residuo) de dos números.

    Args:
        a (float): Dividendo
        b (float): Divisor

    Returns:
        float: Residuo de la división
    """
    return a%b


def potencia(a, b):
    """
    Calcula a elevado a la potencia b.

    Args:
        a (float): Base
        b (float): Exponente

    Returns:
        float: Resultado de a^b
    """
    return a**b


# ============================================
# SECCIÓN 2: CONVERSIÓN DE SISTEMAS NUMÉRICOS (Estudiante 2)
# ============================================

def decimal_a_binario(numero):
    """
    Convierte un número decimal a binario usando algoritmo manual.
    Args:
        numero (int): Número decimal

    Returns:
        str: Representación binaria como string
    """
    # Caso especial: si numero == 0, retornar "0"
    if numero == 0:
        return "0"
    # 1. Crear string vacío para resultado
    resultado = ""
    # 2. Mientras numero > 0:
    # - residuo = numero % 2
    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado
    #    - agregar residuo al inicio del string
    #    - numero = numero // 2
        numero = numero // 2
    # 3. Retornar el string
    return resultado


def decimal_a_hexadecimal(numero):
    """
    Convierte un número decimal a hexadecimal.

    Args:
        numero (int): Número decimal

    Returns:
        str: Representación hexadecimal como string
    """
    
    if numero == 0:
        return "0"
    
    caracteres_hex = "0123456789ABCDEF"
    resultado = ""
    # TODO: Implementar
    # Pueden usar el método similar a binario
    # Recordar: 10=A, 11=B, 12=C, 13=D, 14=E, 15=F

    while numero > 0:
        # 1. Sacamos el residuo dividiendo entre 16
        residuo = numero % 16
        
        # 2. Buscamos el caracter que le corresponde a ese residuo y lo ponemos al inicio
        resultado = caracteres_hex[residuo] + resultado
        
        # 3. Dividimos el número entre 16 para la siguiente vuelta
        numero = numero // 16
    return resultado


def binario_a_decimal(binario):
    """
    Convierte un número binario (string) a decimal.

    Args:
        binario (str): Número binario como string

    Returns:
        int: Número decimal
    """
    # TODO: Implementar
    # Algoritmo:
    # 1. Inicializar decimal = 0
    decimal = 0
    longitud = len(binario)
    # 2. Para cada dígito en binario (de derecha a izquierda):
    for posicion in range(longitud):
    #    - decimal += dígito * (2 ^ posición)
        digito = int(binario[-(posicion + 1)])
        # Aplicamos la fórmula multiplicando por 2 elevado a la posición actual
        decimal += digito * (2 ** posicion)
    # 3. Retornar decimal
    return decimal


def hexadecimal_a_decimal(hexadecimal):
    """
    Convierte un número hexadecimal (string) a decimal.

    Args:
        hexadecimal (str): Número hexadecimal como string

    Returns:
        int: Número decimal
    """
    decimal = 0
    longitud = len(hexadecimal)
    caracteres_hex = "0123456789ABCDEF"

    # Convertimos el texto a mayúsculas por si el usuario escribe "1a" en lugar de "1A"
    hex_mayusculas = hexadecimal.upper()
    
    for posicion in range(longitud):
        # 1. Leemos el carácter de derecha a izquierda
        caracter = hex_mayusculas[-(posicion + 1)]
        
        # 2. Buscamos qué valor numérico tiene ese carácter (del 0 al 15)
        valor = caracteres_hex.index(caracter)
        
        # 3. Aplicamos la fórmula: valor * (16 elevado a la posición)
        decimal += valor * (16 ** posicion)
    return decimal


# ============================================
# SECCIÓN 3: CONVERSIÓN DE UNIDADES (Estudiante 3)
# ============================================

def bytes_a_kilobytes(bytes_val):
    """
    Convierte bytes a kilobytes.

    Args:
        bytes_val (float): Cantidad en bytes

    Returns:
        float: Cantidad en kilobytes
    """
    return bytes_val / 1024


def kilobytes_a_megabytes(kb):
    """
    Convierte kilobytes a megabytes.

    Args:
        kb (float): Cantidad en kilobytes

    Returns:
        float: Cantidad en megabytes
    """
    # TODO: Implementar (1 MB = 1024 KB)
    return kb / 1024


def megabytes_a_gigabytes(mb):
    """
    Convierte megabytes a gigabytes.

    Args:
        mb (float): Cantidad en megabytes

    Returns:
        float: Cantidad en gigabytes
    """
    return mb /1024

def gigabytes_a_megabytes(gb):
    """Convierte gigabytes a megabytes."""
    return gb * 1024

def megabytes_a_kilobytes(mb):
    """Convierte megabytes a kilobytes."""
    return mb * 1024

def kilobytes_a_bytes(kb):
    """Convierte kilobytes a bytes."""
    return kb * 1024


# ============================================
# SECCIÓN 4: GESTIÓN DE HISTORIAL (Estudiante 3)
# ============================================

def agregar_al_historial(operacion, num1, num2, resultado):
    """
    Agrega una operación al historial.

    Args:
        operacion (str): Tipo de operación (ej: "Suma", "División")
        num1 (float): Primer número
        num2 (float): Segundo número
        resultado (float): Resultado de la operación
    """
    global historial

    # TODO: Implementar
    # 1. Crear string con formato: "operación: num1 op num2 = resultado"
    # 2. Agregar al final de la lista historial
    # 3. Si historial tiene más de 10 elementos, eliminar el primero

    # Ejemplo de formato:
    # fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # entrada = f"{fecha_hora} | {operacion}: {num1} + {num2} = {resultado}"
    # historial.append(entrada)

    pass


def mostrar_historial():
    """
    Muestra el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # 1. Verificar si historial está vacío
    # 2. Si está vacío, mostrar mensaje
    # 3. Si no, iterar sobre historial y mostrar cada operación numerada

    pass


def limpiar_historial():
    """
    Limpia el historial de operaciones.
    """
    global historial

    # TODO: Implementar
    # Vaciar la lista historial
    pass


# ============================================
# SECCIÓN 5: GESTIÓN DE ARCHIVOS (Estudiante 1)
# ============================================

def guardar_historial_archivo():
    """
    Guarda el historial en el archivo datos/historial.txt
    """
    global historial

    # TODO: Implementar
    # 1. Crear carpeta "datos" si no existe (usar os.makedirs())
    # 2. Abrir archivo "datos/historial.txt" en modo escritura ("w")
    # 3. Escribir cada línea del historial al archivo
    # 4. Cerrar archivo

    # Ejemplo:
    # if not os.path.exists("datos"):
    #     os.makedirs("datos")
    #
    # with open("datos/historial.txt", "w") as archivo:
    #     for linea in historial:
    #         archivo.write(linea + "\n")

    pass


def cargar_historial_archivo():
    """
    Carga el historial desde el archivo datos/historial.txt
    """
    global historial

    # TODO: Implementar
    # 1. Verificar si el archivo existe (os.path.exists())
    # 2. Si existe:
    #    - Abrir archivo en modo lectura ("r")
    #    - Leer todas las líneas
    #    - Agregar cada línea (sin \n) a la lista historial
    # 3. Si no existe, no hacer nada

    pass


# ============================================
# SECCIÓN 6: VALIDACIÓN (Estudiante 1)
# ============================================

def validar_numero(mensaje):
    """
    Solicita y valida un número al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        float: Número validado
    """
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Ingrese un número válido.")


def validar_numero_entero(mensaje):
    """
    Solicita y valida un número entero al usuario.

    Args:
        mensaje (str): Mensaje a mostrar

    Returns:
        int: Número entero validado
    """
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("❌ Error: Ingrese un número válido.")


# ============================================
# SECCIÓN 7: MENÚS (Estudiante 1)
# ============================================

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("   CALCULADORA MULTIFUNCIONAL v2.0")
    print("="*60)
    print("\nMENÚ PRINCIPAL:")
    print("1. Calculadora Básica")
    print("2. Conversor de Unidades de Datos")
    print("3. Calculadora de Sistemas Numéricos")
    print("4. Ver Historial")
    print("5. Limpiar Historial")
    print("6. Salir")
    print("-"*60)


def menu_calculadora_basica():
    """Menú y lógica de la calculadora básica"""
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo (residuo)")
    print("6. Potencia")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")

    if opcion == "7":
        return
    
    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("\n Error: Opción inválida. Por favor seleccione un número del 1 al 7.")
        return  # Esto hace que la función termine y lo regrese al menú principal

    # Solicitar números
    num1 = validar_numero("Ingrese el primer número: ")
    num2 = validar_numero("Ingrese el segundo número: ")

    # TODO: Implementar lógica según opción
    # - Si opcion == "1": resultado = sumar(num1, num2)
    # - Si opcion == "2": resultado = restar(num1, num2)
    # - etc.
    # - Mostrar resultado
    # - Llamar a agregar_al_historial()
    if opcion == "1":
        resultado = sumar(num1,num2) #operacion
        print(f"\n El resultado de {num1} + {num2} es: {resultado}") #Resultado
        agregar_al_historial("Suma", num1, num2, resultado) #agregar historial
    
    elif opcion == "2":
        resultado = restar(num1,num2) #operacion
        print(f"\n El resultado de {num1} - {num2} es: {resultado}") #Resultado
        agregar_al_historial("Resta", num1, num2, resultado) #agregar historial

    elif opcion == "3":
        resultado = multiplicar(num1,num2) #operacion
        print(f"\n El resultado de {num1} * {num2} es: {resultado}") #Resultado
        agregar_al_historial("Multiplicacion", num1, num2, resultado) #agregar historial
    
    elif opcion == "4":
        resultado = dividir(num1,num2) #operacion
        if resultado is None:
            print("\n EXPLOSION!!!! no se puede dividir entre cero.")
        else:
            print(f"\n El resultado de {num1} / {num2} es: {resultado}") #Resultado
            agregar_al_historial("Dividir", num1, num2, resultado) #agregar historial
    
    elif opcion == "5":
        resultado = divmod(num1,num2) #operacion
        print(f"\n El resultado de {num1} % {num2} es: {resultado}") #Resultado
        agregar_al_historial("Potencia", num1, num2, resultado) #agregar historial
    
    elif opcion == "6":
        resultado = potencia(num1,num2) #operacion
        print(f"\n El resultado de {num1} ** {num2} es: {resultado}") #Resultado
        agregar_al_historial("Potencia", num1, num2, resultado) #agregar historial

def menu_conversor_unidades():
    """Menú y lógica del conversor de unidades"""
    print("\n--- CONVERSOR DE UNIDADES ---")
    print("1. Bytes a kilobytes")
    print("2. Kilobytes a megabytes.")
    print("3. Megabytes a gigabytes.")
    print("4. Gigabytes_a_megabytes")
    print("5. Megabytes_a_kilobytes")
    print("6. Kilobytes_a_bytes")
    print("7. Volver al menú principal")

    opcion = input("\nSeleccione operación del 1 - 7: ")
    if opcion == "7":
        return
    if opcion not in ["1", "2", "3", "4","5","6"]:
        print("\n Error: Opción inválida. Por favor seleccione un número del 1 al 7.")
        return
    
    valor = validar_numero("Ingrese la cantidad a convertir: ")
    if opcion == "1":
        resultado = bytes_a_kilobytes(valor)
        print(f"\n {valor} Bytes equivalen a {resultado} Kilobytes.")
        agregar_al_historial("B -> KB", valor, 0, resultado)
        
    elif opcion == "2":
        resultado = kilobytes_a_megabytes(valor)
        print(f"\n {valor} Kilobytes equivalen a {resultado} Megabytes.")
        agregar_al_historial("KB -> MB", valor, 0, resultado)
        
    elif opcion == "3":
        resultado = megabytes_a_gigabytes(valor)
        print(f"\n {valor} Megabytes equivalen a {resultado} Gigabytes.")
        agregar_al_historial("MB -> GB", valor, 0, resultado)
        
    elif opcion == "4":
        resultado = gigabytes_a_megabytes(valor)
        print(f"\n {valor} Gigabytes equivalen a {resultado} Megabytes.")
        agregar_al_historial("GB -> MB", valor, 0, resultado)
        
    elif opcion == "5":
        resultado = megabytes_a_kilobytes(valor)
        print(f"\n {valor} Megabytes equivalen a {resultado} Kilobytes.")
        agregar_al_historial("MB -> KB", valor, 0, resultado)
        
    elif opcion == "6":
        resultado = kilobytes_a_bytes(valor)
        print(f"\n {valor} Kilobytes equivalen a {resultado} Bytes.")
        agregar_al_historial("KB -> B", valor, 0, resultado)
        
def menu_sistemas_numericos():
    """Menú y lógica de conversión de sistemas numéricos"""
    print("\n--- SISTEMAS NUMÉRICOS ---")
    print("1. Decimal a Binario")
    print("2. Decimal a Hexadecimal")
    print("3. Binario a Decimal")
    print("4. Hexadecimal a Decimal")
    print("5. Volver al menú principal")

    opcion = input("\nSeleccione operación: ")
    if opcion == "5":
        return
    
    if opcion not in ["1", "2", "3", "4"]:
        print("\n Error: Opción inválida. Por favor seleccione un número del 1 al 5.")
        return
    
    if opcion == "1":
        num_decimal = validar_numero_entero("Ingrese el número decimal a convertir: ")  #Pedimos el número usando validación de enteros
        resultado = decimal_a_binario(num_decimal) #Llamamos a tu función de la SECCIÓN 2
        print(f"\n El número decimal {num_decimal} en binario es: {resultado}") # Mostramos el resultado

        # Guardamos en el historial (pasamos 0 o None en el segundo número porque aquí solo usamos uno)
        agregar_al_historial("Dec -> Bin", num_decimal, 0, resultado)
    elif opcion =="2":
        num_decimal = validar_numero_entero("Ingrese el número decimal a convertir: ")
        # Llamamos a nuestra nueva función
        resultado = decimal_a_hexadecimal(num_decimal)
        print(f"\n El número decimal {num_decimal} en hexadecimal es: {resultado}")
        # Guardamos en el historial
        agregar_al_historial("Dec -> Hex", num_decimal, 0, resultado)
    
    elif opcion =="3":
        # Pedimos el número binario como texto normal
        texto_binario = input("Ingrese el número binario a convertir: ")
        
        # Llamamos a nuestra nueva función
        resultado = binario_a_decimal(texto_binario)
        
        # Mostramos el resultado
        print(f"\n El número binario {texto_binario} en decimal es: {resultado}")
        
        # Guardamos en el historial (aquí pasamos texto_binario como primer dato)
        agregar_al_historial("Bin -> Dec", texto_binario, 0, resultado)
   
    elif opcion=="4":
        #Pedimos el número hexadecimal como texto
        texto_hex = input("Ingrese el número hexadecimal a convertir: ")
        
        # Llamamos a nuestra nueva función
        resultado = hexadecimal_a_decimal(texto_hex)
        
        # Mostramos el resultado
        print(f"\n El número hexadecimal {texto_hex.upper()} en decimal es: {resultado}")
        
        # Guardamos en el historial
        agregar_al_historial("Hex -> Dec", texto_hex.upper(), 0, resultado)

        
# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Función principal del programa"""

    print("╔" + "═"*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  CALCULADORA MULTIFUNCIONAL - Versión Avanzada".center(58) + "║")
    print("║" + " "*58 + "║")
    print("║" + "  Con historial, funciones y persistencia de datos".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "═"*58 + "╝")

    # Cargar historial al iniciar
    cargar_historial_archivo()
    print("\n✅ Historial cargado desde archivo.")

    continuar = True

    while continuar:
        mostrar_menu_principal()

        opcion = input("\nSeleccione una opción (1-6): ")

        if opcion == "1":
            menu_calculadora_basica()

        elif opcion == "2":
            menu_conversor_unidades()

        elif opcion == "3":
            menu_sistemas_numericos()

        elif opcion == "4":
            mostrar_historial()

        elif opcion == "5":
            confirmacion = input("\n¿Está seguro de limpiar el historial? (s/n): ")
            if confirmacion.lower() == "s":
                limpiar_historial()
                print("✅ Historial limpiado.")

        elif opcion == "6":
            print("\n💾 Guardando historial...")
            guardar_historial_archivo()
            print("✅ Historial guardado en datos/historial.txt")
            print("\n¡Gracias por usar la Calculadora Multifuncional!")
            print("¡Hasta pronto! 👋")
            continuar = False

        else:
            print("\n❌ Opción inválida. Por favor seleccione 1-6.")

    print("\nPrograma terminado.")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
