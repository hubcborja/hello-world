"""
Generador de Números de la Suerte Personalizado

Este script automatiza la selección de números aleatorios bajo criterios específicos:
- Filtros por dígitos específicos.
- Inyección de números del Almanaque Bristol (6, 14, 23, 33, 42).
- Relaciones matemáticas y visuales con números clave (7, 13, 17).

Generado en colaboración con Gemini (Google AI).
Fecha: Junio 2026
"""

import random

def generar_numeros_suerte_avanzado(digitos_deseados=None, numeros_bristol=None, filtrar_por_especiales=True, rango_min=1, rango_max=99, cantidad=3):
    """
    Genera números al azar basados en dígitos deseados, el almanaque Bristol y relaciones con 7, 13 y 17.
    """
    candidatos = set() # Usamos un set para evitar duplicados
    numeros_bristol = numeros_bristol or []
    
    # 1. Procesar el universo completo del rango asignado
    for num in range(rango_min, rango_max + 1):
        num_str = str(num)
        
        # Filtro de dígitos deseados
        cumple_digitos = True
        if digitos_deseados:
            cumple_digitos = any(str(d) in num_str for d in digitos_deseados)
            
        # Filtro de relación con 7, 13 o 17
        cumple_relacion = True
        if filtrar_por_especiales:
            es_multiplo = (num % 7 == 0) or (num % 13 == 0) or (num % 17 == 0)
            termina_en_clave = num_str.endswith('7') or num_str.endswith('3')
            contiene_clave = '7' in num_str or '13' in num_str or '17' in num_str
            
            cumple_relacion = es_multiplo or termina_en_clave or contiene_clave
            
        # Si cumple los filtros generales, se agrega
        if cumple_digitos and cumple_relacion:
            candidatos.add(num)
            
    # 2. Inyección y validación de los números de Bristol
    # Si un número de Bristol está en el rango, se incluye de forma prioritaria
    for num_b in numeros_bristol:
        if rango_min <= num_b <= rango_max:
            # Opción: Entra directo por ser de Bristol, asegurando que juegue en tu universo
            candidatos.add(num_b)

    # Convertimos a lista para poder ordenar y muestrear
    lista_candidatos = sorted(list(candidatos))
            
    if not lista_candidatos:
        return {
            "error": "No se encontraron números con esos criterios específicos.",
            "candidatos": [],
            "seleccionados": []
        }
        
    # Selección final al azar de la cantidad solicitada
    cantidad_a_tomar = min(cantidad, len(lista_candidatos))
    seleccionados = random.sample(lista_candidatos, cantidad_a_tomar)
    
    return {
        "candidatos_totales": lista_candidatos,
        "seleccionados": seleccionados
    }

# ==========================================
# CONFIGURACIÓN DE TU JUEGO (Modifica aquí)
# ==========================================

# Tus números del Almanaque Bristol
MIS_NUMEROS_BRISTOL = [6, 14, 23, 33, 42]

# Dígitos que quieres forzar que aparezcan (ej. que contengan 3 o 5). 
# Puedes dejarlo como None si solo quieres guiarte por Bristol y los especiales (7, 13, 17)
MIS_DIGITOS = [3]  

# Cuántos números sugeridos quieres obtener
CANTIDAD_NUMEROS = 3 

# Rango de juego
MIN_RANGO = 1
MAX_RANGO = 99

# Ejecución del script
resultado = generar_numeros_suerte_avanzado(
    digitos_deseados=MIS_DIGITOS,
    numeros_bristol=MIS_NUMEROS_BRISTOL,
    filtrar_por_especiales=True, 
    rango_min=MIN_RANGO,
    rango_max=MAX_RANGO,
    cantidad=CANTIDAD_NUMEROS
)

# Mostrar resultados en consola
if "error" in resultado:
    print(resultado["error"])
else:
    print(f"Lista de candidatos final (Filtrados + Bristol incluidos) ({len(resultado['candidatos_totales'])} números):")
    print(resultado["candidatos_totales"])
    print("\n" + "="*50)
    print(f"Tus {CANTIDAD_NUMEROS} números seleccionados al azar son:")
    print(resultado["seleccionados"])
    print("="*50)
