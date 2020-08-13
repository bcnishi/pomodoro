import time
import msvcrt
import tkinter
from tkinter import messagebox

def timer_setting():

    cp_lista = ['20', '25', '30', '35','40','45','50','55','60']
    cb_lista = ['5', '10', '15', '20','25','30'] 

    while True:
        print("Escolha o tempo de pomodoro: ", cp_lista)
        cp = input()
        if cp in cp_lista:
            break
        else:
            print("Opção inválida. Por favor, digite novamente.")
        
    while True:    
        print("Escolha o tempo de descanso: ", cb_lista)        
        cb = input()
        if cb in cb_lista and int(cb)<=int(cp):
            break
        elif cb in cb_lista and int(cb)>int(cp):
            print("O tempo de descanso deve ser menor ou igual ao tempo de pomodoro. Escolha novamente.")
        else:
            print("Opção inválida. Por favor, digite novamente.")
    return [cp,cb]

def cycles():
    print("Digite o número de ciclos (min:1, max:5):")
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
        pass
    try: 
        run_timer(b)
    except KeyboardInterrupt: #Ends the timer when CTRL+C is pressed    
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
    =           OPÇÕES DO TIMER            =
    =                                      =
    =           Pausar (Espaço)            =
    =  Concluir pomodoro/descanso (Crtl+C) =
    =                                      =
    ========================================""")
    print('\nAperte "Enter" para iniciar o {}.\n'.format(t[0]),end="\r")
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
                    clock = time.strftime("%I:%M:%S", localtime) #Shows current time
                    root = tkinter.Tk()
                    root.withdraw()
                    messagebox.showinfo("Seu {} irá acabar em 1 min! (Hora: {})".format(t[0],clock),
                    "\nAproveite para beber água ou ir ao banheiro!")
                    #print("Falta 1 minuto para terminar o {} (Hora: {})\n".format(t[0],clock))
            print("    {:02d}:{:02d}".format(m,s), end="\r")
            time.sleep(1)
            if msvcrt.kbhit(): #Invoke pause function when 'Enter' is pressed
                if ord(msvcrt.getch()) == 32:
                    pause()    
    print("\a") #Sound Alert (Need to test if works on macOS)