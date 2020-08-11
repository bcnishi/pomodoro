import timer_functions as tf

print("""
=================================
=             MENU              =
=                               =
=   Iniciar timer padrão (1)    =
=  Criar Timer customizável (2) =
=                               =
================================= """)

#Default setting
p = ['POMODORO',2] #pomodoro
b = ['DESCANSO',1] #break

while True:
    choice = input("\nDigite a opção desejada: ")
    if choice == '1':
        c = tf.cycles()
        print("""\nConfigurações do timer:
Pomodoro: 25 min | Descanso: 5 min | Ciclos: {}""".format(c))
        for i in range(1,c+1):
            tf.start_timer(p,b)
            if i != c:
                print("Ciclo {} Concluído! Ciclos restantes: {}".format(i,c-i))
            else:
                print("Timer Concluído!")
        break
    elif choice == '2':
        custom = tf.timer_setting()
        cp = ['POMODORO',int(custom[0])] #pomodoro
        cb = ['DESCANSO',int(custom[1])] #break
        c = tf.cycles()
        print("""\nConfigurações do timer:
Pomodoro: {} min | Descanso: {} min | Ciclos: {}""".format(int(custom[0]),int(custom[1]),c))
        for i in range(1,c+1):
            tf.start_timer(cp,cb)
            if i != c:
                print("Ciclo {} Concluído! Ciclos restantes: {}".format(i,c-i))
            else:
                print("Timer Concluído!")
        break
    else:
        print("Opção inválida. Digite novamente.")
        continue