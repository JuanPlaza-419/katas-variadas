def validar_password(password):
    errores = []
    
    # Regla 1: Longitud mínima
    if len(password) < 8:
        errores.append("La contraseña es demasiado corta")
        
    # Regla 2: Al menos un número
    if not any(char.isdigit() for char in password):
        errores.append("Debe contener al menos un número")

    # Regla 3: Al menos una letra
    if not any(char.isalpha() for char in password):
        errores.append("Debe contener al menos una letra")

    # Regla 4: Al menos una letra minúscula
    if not any(char.islower() for char in password):
        errores.append("Debe contener al menos una letra minúscula")

    # Regla 5: Al menos una letra mayúscula
    if not any(char.isupper() for char in password):
        errores.append("Debe contener al menos una letra mayúscula")

    # Regla 6: Carácter especial
    especiales = "=¡!¿?@#$%^*(),.\":}{|<>&"
    if not any(char in especiales for char in password):
        errores.append("Debe contener al menos un carácter especial")

    return {
        "isValid": len(errores) == 0,
        "errors": errores
    }