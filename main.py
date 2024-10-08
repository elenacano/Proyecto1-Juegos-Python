from src import piedra_papel_tijera as ppt
from src import ahorcado, tres_en_raya, preguntados


def mostrar_menu():
    print("\n\n╔══════════════════════════════════════════════╗")
    print("║                                              ║")
    print("║   🎮 BIENVENIDO AL SALÓN DE JUEGOS IRIS 🎮   ║")
    print("║                                              ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║        ⭐️  ELIGE TU JUEGO FAVORITO  ⭐️       ║")
    print("║                                              ║")
    print("║    1️⃣  - Piedra, Papel, Tijera                ║")
    print("║    2️⃣  - Ahorcado                             ║")
    print("║    3️⃣  - Preguntados                          ║")
    print("║    4️⃣  - Tres en Raya                         ║")
    print("║    5️⃣  - Salir                                ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")
    print("✨ ¡Elige una opción y comienza la diversión! ✨")




def main():
    
    while True:
        seleccion = 0
        mostrar_menu()
        try:
            juego_seleccionado = int(input("Seleccione el número del juego al que desea jugar: "))
        
            if juego_seleccionado == 5:
                print("Gracias por jugar con nosotros, hasta pronto 💗​\n")
                break

            elif juego_seleccionado == 1:
                seleccion = ppt.inicio_ppt()

            elif juego_seleccionado == 2:
                seleccion = ahorcado.inicio_ahorcado()

            elif juego_seleccionado == 3:
                seleccion = preguntados.inicio_preguntados()

            elif juego_seleccionado == 4:
                seleccion = tres_en_raya.inicio_tres_raya()

            else:
                print("\nPor favor ingrese un número entre 1 y 5.")

            if seleccion == 3:
                    print("Gracias por jugar con nosotros, hasta pronto 💗​\n")
                    break

        except ValueError:
            print("Por favor ingrese un número entre 1 y 5.\n")
            main()



if __name__ == "__main__":
    main()

