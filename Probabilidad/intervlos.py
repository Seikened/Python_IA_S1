import scipy.stats as stats
import math

def intervalo_confianza(tipo, estadistico, valor, tamano_muestra, nivel_confianza, desviacion_estandar=None):
    """
    Calcula el intervalo de confianza.
    """
    alpha = 1 - nivel_confianza
    limite = None

    if tipo == "media":
        if estadistico == "z":
            z = stats.norm.ppf(1 - alpha/2)
            limite = z * (desviacion_estandar / math.sqrt(tamano_muestra)) # type: ignore
        elif estadistico == "t-student":
            df = tamano_muestra - 1  # Grados de libertad
            t = stats.t.ppf(1 - alpha/2, df)
            s = valor / math.sqrt(tamano_muestra)
            limite = t * s
    elif tipo == "proporcion" and estadistico == "z":
        z = stats.norm.ppf(1 - alpha/2)
        limite = z * math.sqrt((valor * (1 - valor)) / tamano_muestra)
    elif tipo in ["desviacion_estandar", "varianza"] and estadistico == "chi_cuadrada":
        df = tamano_muestra - 1
        chi2_inferior = stats.chi2.ppf(alpha/2, df)
        chi2_superior = stats.chi2.ppf(1 - alpha/2, df)
        if tipo == "desviacion_estandar":
            return math.sqrt((df * valor**2) / chi2_superior), math.sqrt((df * valor**2) / chi2_inferior)
        else:
            return (df * valor) / chi2_superior, (df * valor) / chi2_inferior

    return valor - limite, valor + limite

def preguntar_datos():
    """
    Pregunta al usuario qué datos tiene y decide qué tipo de prueba se debe usar.
    """
    print("¿Qué datos tienes?")
    tiene_media = input("¿Tienes la media muestral? (s/n): ").lower() == "s"
    tiene_proporcion = input("¿Tienes la proporción? (s/n): ").lower() == "s"
    tiene_desv_estandar = input("¿Tienes la desviación estándar? (s/n): ").lower() == "s"
    tiene_varianza = input("¿Tienes la varianza? (s/n): ").lower() == "s"
    
    if tiene_media:
        tiene_desv_poblacional = input("¿Tienes la desviación estándar de la población? (s/n): ").lower() == "s"
        if tiene_desv_poblacional:
            return "media", "z"
        else:
            return "media", "t-student"
    elif tiene_proporcion:
        return "proporcion", "z"
    elif tiene_desv_estandar:
        return "desviacion_estandar", "chi_cuadrada"
    elif tiene_varianza:
        return "varianza", "chi_cuadrada"
    else:
        print("No has proporcionado suficientes datos para decidir una prueba.")
        return None, None

# Usando la función
tipo, estadistico = preguntar_datos()
if tipo and estadistico:
    valor = float(input(f"Introduce el valor de {tipo}: "))
    tamano_muestra = int(input("Introduce el tamaño de la muestra: "))
    nivel_confianza = float(input("Introduce el nivel de confianza (ej. 0.95 para 95%): "))

    # Si es media con z, necesitamos la desviación estándar de la población
    desviacion_estandar = None
    if tipo == "media" and estadistico == "z":
        desviacion_estandar = float(input("Introduce la desviación estándar de la población: "))

    # Calculamos el intervalo de confianza
    inferior, superior = intervalo_confianza(tipo, estadistico, valor, tamano_muestra, nivel_confianza, desviacion_estandar)
    print(f"Intervalo de confianza para {tipo} con {estadistico}: ({inferior:.2f}, {superior:.2f})")
else:
    print("Por favor, vuelve a intentarlo proporcionando datos válidos.")

