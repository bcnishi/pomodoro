import pandas as pd
import numpy as np
import os
import time
import matplotlib
import matplotlib.pyplot as plt

def create():
    """Verify if the csv archive already exists, if so do nothing.
    If the archive doesn't exist, create the dataframe and write in a csv archive"""
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
            d = time.strftime("%d/%m/%Y", localtime) #gets today's date
            df.iloc[-1,1] = d #today's date
            df.iloc[-1,2] = p #pomodoro value
            df.iloc[-1,3] = b #break value
            df.iloc[-1,4] = c #cycle value
            df.iloc[-1,5] = (p+b)*c #total time
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
    df2 = pd.DataFrame({'Tarefas': [new],'Data':[np.NaN],'Pomodoro':[0],
                        'Descanso':[0],'Ciclos':[0],'Tempo_Total':[0]})
    df = df.append(df2, ignore_index = True)
    #print("\n",df)
    df[['Pomodoro','Descanso','Ciclos']] = df[['Pomodoro','Descanso','Ciclos']].astype(int)
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
        while r not in range(len(df['Tarefas'])): #Verify if task's index given by user is valid
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
        df.iloc[r,0] = e #assign the new task name
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
        #convert float values to int
        report[['len','min','max']] = report[['len','min','max']].fillna(0.0).astype(int)
        #convert minutes to HH:MM notation
        report['sum'] = pd.to_datetime(report['sum'], unit='m').dt.strftime('%H:%M')
        #rename columns
        report = report.rename(columns={'len':'Execuções','min':'Tempo mínimo (min)',
        'mean':'Tempo Médio (min)','max':'Tempo Máximo (min)','sum':'Total (H:M)'})
        print("\n",report)
    
        report2 = df.groupby('Data').Tempo_Total.agg([len, min, 'mean', max, np.sum])
        #sort by descending date
        report2 = report2.sort_values('Data', ascending=False)
        #convert float values to int
        report2[['len','min','max']] = report2[['len','min','max']].fillna(0.0).astype(int)
        #convert minutes to HH:MM notation
        report2['sum'] = pd.to_datetime(report2['sum'], unit='m').dt.strftime('%H:%M')
        #rename columns
        report2 = report2.rename(columns={'len':'Tarefas','min':'Tempo mínimo (min)',
        'mean':'Tempo Médio (min)','max':'Tempo Máximo (min)','sum':'Total (H:M)'})
        print("\n",report2)
        