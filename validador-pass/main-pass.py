from validador import validar_password

def main():
    print("--- Validador de Seguridad ---")
    password = input("Ingresa una contraseña para probar: ")
    resultado = validar_password(password)
    
    if resultado["isValid"]:
        print("Contraseña válida.")
    else:
        print(f"Inválido: {resultado['errors']}")

if __name__ == "__main__":
    main()