import timer_functions as tf
import tasks as tk

#Main Menu
print("""
=================================
=         MENU PRINCIPAL        =
=                               =
=           Timer (1)           =
=   Gerenciador de Tarefas (2)  =
=     Relatório de Dados (3)    =
=                               =
================================= """)

while True:
    choice = input("\nDigite a opção desejada: ")
    if choice == '1':
#Timer Menu
        print("""
=================================
=         MENU DO TIMER         =
=                               =
=   Iniciar Timer Padrão (1)    =
=  Criar Timer Customizável (2) =
=                               =
================================= """)

        while True:
            choice = input("\nDigite a opção desejada: ")
            if choice == '1':#Default setting                               
                p = ['POMODORO',25] #pomodoro
                b = ['DESCANSO',5] #break
                c = tf.cycles()
                tk.run_task(p[1],b[1],c)
                print("""\nConfigurações do timer:
        Pomodoro: 25 min | Descanso: 5 min | Ciclos: {}""".format(c))
                for i in range(1,c+1):
                    tf.start_timer(p,b)
                    if i != c:
                        print("\nCiclo {} Concluído! Ciclos restantes: {}".format(i,c-i))
                    else:
                        print("\nTimer Concluído! Agora hidrate-se e coma algo bem gostoso!")
                break
            elif choice == '2': #Custom setting
                custom = tf.timer_setting()
                cp = ['POMODORO',int(custom[0])] #pomodoro
                cb = ['DESCANSO',int(custom[1])] #break
                c = tf.cycles()
                tk.run_task(cp[1],cb[1],c)
                print("""\nConfigurações do Timer:
        Pomodoro: {} min | Descanso: {} min | Ciclos: {}""".format(int(custom[0]),int(custom[1]),c))
                for i in range(1,c+1):
                    tf.start_timer(cp,cb)
                    if i != c:
                        print("\nCiclo {} Concluído! Ciclos restantes: {}".format(i,c-i))
                    else:
                        print("\nTimer Concluído! Agora hidrate-se e coma algo bem gostoso!")
                break
            else:
                print("Opção inválida. Digite novamente.")
                continue
        break
    elif choice == '2':
#Task Menu
        print("""
=================================
=        MENU DE TAREFAS        =
=                               =
=      Adicionar Tarefa (1)     =
=       Listar Tarefas (2)      =
=        Editar Tarefa (3)      =
=       Remover Tarefa (4)      = 
=                               =
================================= """)
        while choice not in range(1,5):
            try:
                choice = int(input("\nDigite a opção desejada: "))
            except:
                print("Opção inválida. Por favor, digite novamente.")
                continue            
        if choice == 1:
            tk.add_task()
        elif choice == 2:
            tk.list_task()
        elif choice == 3:
            tk.edit_task()
        elif choice == 4:
            tk.del_task()
        break
    elif choice == '3':
        tk.reports()
        break
    else:
        print("Opção inválida. Digite novamente.")
        continue