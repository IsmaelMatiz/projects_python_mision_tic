dis,vel,tim = input().split()
dis = int(dis)
vel = int(vel)
tim = int(tim)
if dis < 0 or vel < 0 or tim < 0:
    print("VALORES NEGATIVOS")
else:
    tim = (tim / 60)/60
    dis /= 1000
    dis /= tim
    per = vel + vel * 0.25
    if dis <= vel:
        print("OK")
    elif dis < per:
        print("MULTA")
    elif dis >= per:
        print("CURSO SENSIBILIZACION")