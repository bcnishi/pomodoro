import timer_functions as tf
import tasks as tk

menu = ("""
=================================
=         POMODORO DORO \U0001F345      =
=                               =
=           Timer (1)           =
=     Tarefas Registradas (2)   =
=     Relatório de Dados (3)    =
=            Sair (4)           =
=                               =
================================= """)

while True:
    print(menu) #Main Menu
    choice = input("\nDigite a opção desejada: ")
    if choice == '1': #Timer Menu
        print("""
=================================
=            TIMER \u23F0           =
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
                        print("\nTimer Concluído! Agora hidrate-se \U0001F6B0 e coma algo bem gostoso \U0001F355!")
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
                        print("\nTimer Concluído! Agora hidrate-se \U0001F6B0 e coma algo bem gostoso \U0001F355!")
                break
            else:
                print("Opção inválida. Digite novamente.")
                continue
    elif choice == '2': #Task Menu
        print("""
=================================
=      TAREFAS REGISTRADAS \U0001F4D3   =
=                               =
=       Listar Tarefas (1)      =
=        Editar Tarefa (2)      =
=       Remover Tarefa (3)      = 
=                               =
================================= """)

        while choice not in range(1,5):
            try:
                choice = int(input("\nDigite a opção desejada: "))
                if choice not in range(1,5):
                    print("Opção inválida. Por favor, digite novamente.")
            except:
                print("Opção inválida. Por favor, digite novamente.")
                continue            
        if choice == 1:
            tk.list_task()
        elif choice == 2:
            tk.edit_task()
        elif choice == 3:
            tk.del_task()
    elif choice == '3': #Reports
        tk.reports()
    elif choice == '4': #Exit
        print("""\nAdorei passar esse tempo com você! Até a próxima! \U0001F60A                                                                                                  
                                ((                              
                              ((                                               
                            (((                                 
                             (((                                  
                               ((                                                                          
                (((((((((((((((((((((((((((((((                                                             
              %%%%%%%%%%%%(((((((((((((%%%%%%%((((                                                          
           %%%%%%%%%%%%%%((((((((((((((((((%%%%###%%                                                       
         %%%%%%%%%%%%(((((%%%%((((%%%%%((((%%%%#####%                                                     
       %%%%%%%%%%%%%(((%%%%%%(((%%%%%%%%%(((%%%%######%                                                    
      %%%%%%%%%%%%%(%%%%%%%%%%((%%%%%%%%%%(%%%%%%######%                                                  
     %%%%%%%%%%%%%%%%%%%%%%%%%(%%%%%%%%%%%%%%%%%%%######%                                                  
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#####%                                                 
     %%%%%%%%             OBRIGADO!!             %%%####%                                                 
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                 
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                              
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                            
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                 
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                    
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                                                        
               %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% """)
        break
    else:
        print("Opção inválida. Digite novamente.")
        continue