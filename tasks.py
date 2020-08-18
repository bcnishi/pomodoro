import pandas as pd
import numpy as np
import os
import time

def create():
    if os.path.exists("pomodoro.csv"):
        None
    else:
        df = pd.DataFrame({
            'Tarefas': ["Estudar python","Ler 1984","Trabalhar no projeto da Paolla",
            "Estudar python"],
            'Data': ["14/08/2020","14/08/2020","15/08/2020","16/08/2020"],
            'Pomodoro':[25,25,30,40],'Descanso':[5,5,10,15],'Ciclos':[1,2,3,2],
            'Tempo_Total':[30,60,120,110]})
        #df['Data'] = pd.to_datetime(df['Data']) 
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def run_task(p,b,c):
    print("\nVocê deseja vincular o timer à uma tarefa? Digite \"S\" para sim ou \"N\" para não.")
    while True:
        a = input()
        if a.lower() == 'n' or a.lower() == 'não' or a.lower() == 'nao':
            break
        elif a.lower() == 's' or a.lower() == 'sim':
            add_task()
            df = pd.read_csv("pomodoro.csv")
            localtime = time.localtime()
            d = time.strftime("%d/%m/%Y", localtime)
            df.iloc[-1,1] = d
            df.iloc[-1,2] = p
            df.iloc[-1,3] = b
            df.iloc[-1,4] = c
            df.iloc[-1,5] = (p+b)*c
            df['Ciclos'] = df['Ciclos'].astype(int)
            print("\n",df)
            df.to_csv("pomodoro.csv",index=False,encoding='utf-8')
            break
        else:
            print("Resposta inválida. Por favor, digite novamente.")
            continue

def add_task():
    create()
    df = pd.read_csv("pomodoro.csv")
    print("\nDigite a tarefa a ser adicionada. A tarefa deve conter, no mínimo, 3 caracteres.")
    while True:
        new = input()
        if len(new) >= 3 and not new.isspace():
            break
        else:
            print("Tarefa inválida. Por favor, digite novamente.")
            continue
    df2 = pd.DataFrame({'Tarefas': [new],'Data':[np.NaN],'Pomodoro':[np.NaN],
                        'Descanso':[np.NaN],'Ciclos':[np.NaN],'Tempo_Total':[np.NaN]})
    df = df.append(df2, ignore_index = True)
    #print("\n",df)
    df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def list_task():
    create()
    df = pd.read_csv("pomodoro.csv")
    print("\n",df)

def edit_task():
    create()
    df = pd.read_csv("pomodoro.csv")
    if len(df['Tarefas']) == 0:
        print("Não há tarefas registradas!")
    else:
        print("\n",df)
        print("\nDigite o número da tarefa a ser editada: ")
        r =-1
        while r not in range(len(df['Tarefas'])):
                try:
                    r = int(input())
                except:
                    print("Opção inválida. Por favor, digite novamente.")
                    continue
        print("Digite o novo nome da tarefa. A tarefa deve conter, no mínimo, 3 caracteres.")
        while True:
            e = input()
            if len(e) >= 3 and not e.isspace():
                break
            else:
                print("Tarefa inválida. Por favor, digite novamente.")
                continue
        #df['Tarefas'] = df['Tarefas'].replace(df.iloc[r,0],e) replace all tasks with same name
        df.iloc[r,0] = e
        print("\n",df)
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def del_task():
    create()
    df = pd.read_csv("pomodoro.csv")
    if len(df['Tarefas']) == 0:
        print("Não há tarefas registradas!")
    else:
        print("\n",df)
        r = -1
        print("\nDigite o número da tarefa que deseja remover:")  
        while r not in range(len(df['Tarefas'])):
            try:
                r = int(input())
            except:
                print("Opção inválida. Por favor, digite novamente.")
                continue
        df = df.drop(r)
        df = df.reset_index(drop=True)
        print("\n",df)
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def reports():
    create()
    df = pd.read_csv("pomodoro.csv")
    if len(df['Tarefas']) == 0:
        print("Não há tarefas registradas!")
    else:
        report = df.groupby('Tarefas').Tempo_Total.agg([len, min, 'mean', max, np.sum])
        report = report.rename(columns={'len':'Execuções','min':'Tempo mínimo (min)',
        'mean':'Tempo Médio (min)','max':'Tempo Máximo (min)','sum':'Total (min)'})
        report['Execuções'] = report['Execuções'].astype(int)
        print("\n",report)
        report2 = df.groupby('Data').Tempo_Total.agg([len, min, 'mean', max, np.sum])
        report2 = report2.rename(columns={'len':'Tarefas','min':'Tempo mínimo (min)',
        'mean':'Tempo Médio (min)','max':'Tempo Máximo (min)','sum':'Total (min)'})
        report2['Tarefas'] = report2['Tarefas'].astype(int)
        print("\n",report2)