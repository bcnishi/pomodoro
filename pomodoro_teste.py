import timer_functions as tf
import tasks as tk

print("""
=================================
=             MENU              =
=                               =
=           Timer (1)           =
=   Gerenciador de Tarefas (2)  =
=     Relatório de Dados (3)    =
=                               =
================================= """)

while True:
    choice = input("\nDigite a opção desejada: ")
    if choice == '1':
        print("""\n
=================================
=         MENU DO TIMER         =
=                               =
=   Iniciar timer padrão (1)    =
=  Criar Timer customizável (2) =
=                               =
================================= """)

        #Default setting
        p = ['POMODORO',2] #pomodoro
        b = ['DESCANSO',2] #break

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
                        print("\nTimer Concluído! Agora hidrate-se e coma algo bem gostoso!")
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
                        print("\nTimer Concluído! Agora hidrate-se e coma algo bem gostoso!")
                break
            else:
                print("Opção inválida. Digite novamente.")
                continue
        break
    elif choice == '2':
        print("""
=================================
=        MENU DE TAREFAS        =
=                               =
=       Adicionar Tarefa (1)    =
=       Listar Tarefas (2)      =
=        Editar Tarefa (3)      =
=       Remover Tarefa (4)      = 
=                               =
================================= """)
        choice = -1
        menu = ['1','2','3','4']
        while choice not in menu:
            try:
                choice = input("\nDigite a opção desejada: ")
            except:
                print("Opção inválida. Por favor, digite novamente.")
                continue            
        if choice == '1':
            tk.add_task()
        elif choice == '2':
            tk.list_task()
        elif choice == '3':
            tk.edit_task()
        elif choice == '4':
            tk.del_task()
        break
    elif choice == '3':
        tk.reports()
        break
    else:
        print("Opção inválida. Digite novamente.")
        continue