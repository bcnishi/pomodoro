import time
import msvcrt

def timer_setting():

    cp_lista = ['20', '25', '30', '35','40','45','50','55','60']
    cb_lista = ['5', '10', '15', '20','25','30'] 

    while True:
        print("Escolha o tempo de POMODORO (min):", ', '.join(cp_lista))
        cp = input()
        if cp in cp_lista:
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")
        
    while True:    
        print("Escolha o tempo de DESCANSO (min):", ', '.join(cb_lista))        
        cb = input()
        if cb in cb_lista and int(cb)<=int(cp):
            break
        elif cb in cb_lista and int(cb)>int(cp):
            print("O tempo de DESCANSO deve ser menor ou igual ao tempo de POMODORO. Escolha novamente.")
        else:
            print("Opção inválida. Por favor, digite novamente.")
    return [cp,cb]

def cycles():
    print("Escolha o número de ciclos (mínimo: 1, máximo: 5):")
    c = 0
    while c <= 0 or c > 5:
        try:
            c = int(input())
        except:
            print("Opção inválida. Por favor, digite novamente.")
            continue
        if c <= 0 or c > 5:
            print("Opção inválida. Por favor, digite novamente.")
    return c

def start_timer(p,b):
    try: 
        run_timer(p)       
    except KeyboardInterrupt: #Ends the timer when CTRL+C is pressed
        print("\a") #Sound Alert
        pass
    try: 
        run_timer(b)
    except KeyboardInterrupt: #Ends the timer when CTRL+C is pressed
        print("\a") #Sound Alert   
        pass

def pause():
    """Function to pause the timer and then unpause when the "Space" key is pressed again"""
    print("Timer pausado. Para despausar aperte \"Espaço\".",end="\r")
    while True:
        time.sleep(1)
        if msvcrt.kbhit():
            if ord(msvcrt.getch()) == 32:
                break
    print("                                               ",end="\r")

def run_timer(t):
    """Timer run function"""
    print("""
========================================
=           OPÇÕES DO TIMER \u23F0         =
=                                      =
=           Pausar (Espaço)            =
=  Concluir Pomodoro/Descanso (Ctrl+C) =
=                                      =
========================================""")
    if t[0] == 'POMODORO':
        print("""\nDesconecte-se das redes sociais e concentre-se! 
Quando estiver pronto(a), aperte \"Enter\" para iniciar o POMODORO.\n""",end="\r")
    else:
        print("""\nO POMODORO acabou! Vamos descansar um pouco antes de continuar?  
Para iniciar o DESCANSO, aperte \"Enter\".\n""",end="\r")
    while ord(msvcrt.getch()) != 13:
        continue
    print("\n   {}".format(t[0]))
    print("\n    {}:00".format(t[1]),end="\r")
    time.sleep(1)
    for m in range(t[1]-1,-1,-1): #minutes loop
        for s in range(59,-1,-1): #seconds loop
            if t[0] == 'DESCANSO':
                if m == 1 and s == 0: #Notification at 1 min left to timer ends
                    localtime = time.localtime()
                    clock = time.strftime("%H:%M:%S", localtime) #Shows current time
                    print("Seu DESCANSO irá acabar em 1 min! (Hora: {})".format(clock))
                    print("Aproveite para beber água \U0001F6B0 ou ir ao banheiro \U0001F6BE!\n")
            print("    {:02d}:{:02d}".format(m,s), end="\r")
            time.sleep(1)
            if msvcrt.kbhit(): #Invoke pause function when 'Enter' is pressed
                if ord(msvcrt.getch()) == 32:
                    pause()    
    print("\a") #Sound Alert