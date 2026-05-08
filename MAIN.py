from converter import *

def menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Kilómetros a Millas")
    print("4. Millas a Kilómetros")
    print("5. Kilogramos a Libras")
    print("6. Libras a Kilogramos")
    print("0. Salir")

def main():
    while True:
        menu()
        opcion = input("Elige una opción: ")
        if opcion == "0":
            print("¡Hasta luego!")
            break
        try:
            valor = float(input("Ingresa el valor: "))
            if opcion == "1":
                print(f"Resultado: {celsius_to_fahrenheit(valor):.2f} °F")
            elif opcion == "2":
                print(f"Resultado: {fahrenheit_to_celsius(valor):.2f} °C")
            elif opcion == "3":
                print(f"Resultado: {km_to_miles(valor):.2f} millas")
            elif opcion == "4":
                print(f"Resultado: {miles_to_km(valor):.2f} km")
            elif opcion == "5":
                print(f"Resultado: {kg_to_pounds(valor):.2f} libras")
            elif opcion == "6":
                print(f"Resultado: {pounds_to_kg(valor):.2f} kg")
            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: Por favor ingresa un número válido.")

if __name__ == "__main__":
    main()