from random import randint
import time
import sys
import threading

count_seg = 0 #contador de segundos
count_min = 0 #contador minutos
stop = False


def timer():
    global count_min, count_seg, stop
    while True:
        if stop == True:
            break
        while pause == True:
            time.sleep(1)
            count_seg += 1
            if count_seg == 59:
                count_seg = 0
                count_min += 1

#------variables a nivel general----------
count_games = 0 #cuenta el numero de juegos
pause = False #Booleano para continuar o parar temporalmente el tiempo
frequency = [0,0,0,0]#frecuencia con la q se gana 1 a 4 respectivamente en cada posicion 
time_min1 = 0#menor tiempo que se demoro en ganar | minutos
time_min2 = 0#menor tiempo que se demoro en ganar | segundos
time_max1 = 0#Mayor tiempo en q se demoro ganar | minutos
time_max2 = 0#Mayor tiempo en q se demoro ganar |segundos
average = [0,0]#Contiene el Promedio de tiempo 
total_games = 0#suma del tiempo de juego
win_games = 0#juegos ganados
lose_games = 0#juegos perdidos
totaltime1 = 0#suma de todo el tiempo | 
totaltime2 = 0#suma todo el tiempo | segundos
hilo = threading.Thread(target = timer)#declaracion del hilo donde se correra el tiempo
hilo.start()#llamada al hilo del tiempo
end = False

print("""
                                    Bienvenido a Adivina el numero
                    Lo que debes hacer es ahora es darme 3 numeros del 1 al 9
                    y si coinciden o no te mostrar uno de estos mensajes
                    V = El numero es correcto y esta en la posicion correcta
                    A = El numero es correcto pero no esta en la posicion debida
                    R = El numero no es correcto
                    Tienes 4 intentos, presiona espacio para empezar o cualquier
                    tecla para cerrar el juego y luego enter""")#mensaje de inicio

play = input()#señal de inicio de juego
if play == " ":
    while True:
        #------variables de juego por ronda-------
        #Numeros del juego 
        count_games += 1#cuenta el numero de juegos
        randoms = [randint(1,9),randint(1,9),randint(1,9)]#-------------------------------------------
        attempts = 0 #contador de intentos
        win = False#el usuario perdio o gano la partida?
        #----------------generar numeros aleatorios pero q sean diferentes entre si-------------------
        while randoms[1] == randoms[0] or randoms[1] == randoms[2] :
            randoms[1] = randint(1,9)
        while randoms[2] == randoms[0]:
            randoms[2] = randint(1,9)
        #intentos del juego
        again = 0
        count_trys = 0
        #Juego en si
        pause = True#Arranca el tiempo
        print("empezo a correr el tiempo")
        #-----------pedir los numeros del usuario--------------------
        while again != 3 and count_trys != 4:
            count_trys += 1
            trys = [int(input("dime tu primer numero: ")),int(input("dime tu segundo numero: ")),int(input("dime el tercer numero: "))]
            #pedir los numeros hasta q coopere
            for i in range(len(trys)):
                while trys[i] < 0 or trys[i] > 9:
                    trys = [int(input("dime tu primer numero: ")),int(input("dime tu segundo numero: ")),int(input("dime el tercer numero: "))]
            #---------mensajes dependiendo de lo q conteste------------
            again = 0#reiniciar again para confirmar correctamente
            for i in range(len(trys)):
                if trys[i] == randoms[i]:
                    again += 1
                    print("V",end=" ")
                else:
                    r = 0#esta es una variable auxiliar para imprimir R correctamente
                    for x in range(len(randoms)):
                        if trys[i] == randoms[x]:
                            print("A",end=" ")
                        else:
                            r += 1
                    if r == 3:
                        print("R",end=" ")
            if again == 3:
                win = True
                win_games += 1
            print("\nLe quedan", 4 - count_trys, "intentos")
        pause = False#detengo el tiempo
        #------operaciones del juego general--------
        #frecuencia
        if count_trys == 1:
            frequency[0] += 1
        elif count_trys == 2:
            frequency[1] += 1
        elif count_trys == 3:
            frequency[2] +=1
        else:
            frequency[3] += 1
        #tiempo minimo
        if count_games == 1:
            time_min1 = count_min
            time_min2 = count_seg
        else:
            if count_min < time_min1:
                time_min1 = count_min
            if count_seg < time_min2:
                time_min2 = count_seg
        #tiempo maximo
        if count_games == 1:
            time_max1 = count_min
            time_max2 = count_seg
        else:
            if count_min > time_max1:
                time_max1 = count_min
            if count_seg > time_max2:
                time_max2 = count_seg
        #promedio tiempo
        average[0] += count_min
        average[1] += count_seg
        #total juegos 
        #--es igual al count_games
        #juegos ganado
        #--ya subi el contador en la victoria
        #juegos perdidos
        if win == False:
            lose_games +=1
        #total tiempo
        totaltime1 += count_min
        totaltime2 += count_seg
        if win:
            if count_min == 0:
                print(f"Muy bien adivinaste en {count_trys} intento y {count_seg} segundos")
            else:
                print(f"Muy bien adivinaste en {count_trys} intento y Min.Seg {count_min}:{count_seg}")
        else:
            print(f"Fallaste, se agotaron tus intentos, los números ocultos eran {randoms[0]} {randoms[1]} {randoms[2]}")
        #jugar de nuevo?
        play_again = input("deseas jugar otra vez?(si|no) ")
        if play_again == "SI" or play_again == "Si" or play_again == "si":
            count_min = 0
            count_seg = 0
            continue
        elif play_again == "NO" or play_again == "No" or play_again == "no": 
            stop = True
            end = True
            break
        else:
            print("No se que dijiste don comedias asi q simplemente considerare q no quieres seguir jugando")
            stop = True
            break
if end:
    print(f"""
    ● La frecuencia de intentos ganadores ( Ganadores en 1 intento: {frequency[0]} , 2 Intentos: {frequency[1]}, 3 Intentos: {frequency[2]},
      4 Intentos: {frequency[3]} )
    ● Tiempo minimo: {time_min1}:{time_min2}
    ● Tiempo Maximo: {time_max1}:{time_max2}
    ● Promedio de Tiempo de juego: {average[0]//count_games}:{average[1]//count_games}
    ● Total Juegos: {count_games}
    ● Cantidad de Juegos Ganados: {win_games}
    ● Cantidad de Juegos Perdidos: {lose_games}
    ● Total Minutos: {totaltime1}, Segundos: {totaltime2} de juego.
    """)
else:
    SystemExit(0)