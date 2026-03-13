def tramo_edad(edad):
    """
    Función para determinar un tramo de edad.
    Return: Retorna el tramo en que se encuentra el empleado.
    """
    
    
    if edad >= 18 and edad <= 35:
        return "Joven"
    elif edad > 35 and edad <= 50:
        return "Adulto"
    else:
        return "Adulto Mayor"
    
    
    
def cercania(distancia):
    """
    Función para determinar un tramo de distancia.
    Return: Retorna el tramo de distancia en que se encuentra el empleado.
    """
    
    
    if distancia >= 0 and distancia <= 5:
        return "Very Near"
    elif distancia > 5 and distancia <= 10:
        return "Near"
    elif distancia > 10 and distancia <= 15:
        return "Medium"
    else:
        return "Far"