from time import sleep
import random
import colorama

list = ["piedra", "papel", "tijeras"]

Jugar = input("\033[1;34m\n[*] Elige entre (piedra, papel o tijeras): " + "\033[1;m")

Ataque = random.choice(list)


if Jugar=="piedra" and Ataque=="papel":
        print("Evaluando juego")
        sleep(2)
        print("Piedra gana!!!")

elif Jugar=="piedra" and Ataque=="tijeras":
      print("Evaluando juego")
      sleep(2)
      print("Piedra gana!!!")

elif Jugar=="piedra" and Ataque=="piedra":
      print("Evaluando juego")
      sleep(2)
      print("Empate!!!")

elif Jugar=="papel" and Ataque=="tijeras":
      print("Evaluando juego")
      sleep(2)
      print("tijeras gana!")

elif Jugar=="papel" and Ataque=="papel":
    print("Evaluando juego")
    sleep(2)
    print("Empate!!!")

elif Jugar=="tijeras" and Ataque=="tijeras":
    print("Evaluando juego")
    sleep(2)
    print("Empate!!!")

else:
  pass 
    
        
        