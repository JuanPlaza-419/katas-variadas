from calculadora import sumatoria

def main():  
    entrada = input("Números a sumar: ")
    
    try:
        resultado = sumatoria(entrada)
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Error: Asegúrate de introducir solo números separados por comas.")

if __name__ == "__main__":
    main()