import pandas as pd
import numpy as np
import os

def create():
    if os.path.exists("pomodoro.csv"):
        None
    else:
        df = pd.DataFrame({
            'Tarefas': ["Estudar python","Estudar Métricas","Trabalhar no projeto da Paolla",
            "Estudar python"],
            'Data': ["14/08/2020","14/08/2020","15/08/2020","16/08/2020"],
            'Pomodoro':[25,25,30,40],'Ciclo':[1,2,3,2],'Tempo_Total':[25,50,90,80]})
        #df['Data'] = pd.to_datetime(df['Data']) 
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def add_task():
    df = pd.read_csv("pomodoro.csv")
    print("Digite a tarefa a ser adicionada. A tarefa deve conter, no mínimo, 3 caracteres.")
    while True:
        new = input()
        if len(new) >= 3 and not new.isspace():
            break
        else:
            print("Tarefa inválida. Por favor, digite novamente.")
            continue
    df2 = pd.DataFrame({'Tarefas': [new],'Data':[np.NaN],
                        'Pomodoro':[np.NaN],'Ciclo':[np.NaN],'Tempo_Total':[np.NaN]})
    df = df.append(df2, ignore_index = True)
    print(df)
    df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def list_task():
    print("\n")
    df = pd.read_csv("pomodoro.csv")
    tasks = df.Tarefas.drop_duplicates()
    print(tasks)

def edit_task():
    df = pd.read_csv("pomodoro.csv")
    if len(df['Tarefas']) == 0:
        print("Não há tarefas registradas!")
    else:
        print(df['Tarefas'])
        print("Digite o número da tarefa a ser editada: ")
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
        df['Tarefas'] = df['Tarefas'].replace(df.iloc[r,0],e)
        print(df)
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def del_task():
    df = pd.read_csv("pomodoro.csv")
    if len(df['Tarefas']) == 0:
        print("Não há tarefas registradas!")
    else:
        print(df[['Tarefas']])
        r = -1
        print("\nDigite o número da tarefa que deseja remover:")  
        while r not in range(len(df['Tarefas'])):
            try:
                r = int(input())
            except:
                print("Opção inválida. Por favor, digite novamente.")
                continue
            print("\n")
        df = df.drop(r)
        df = df.reset_index(drop=True)
        print(df)
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def reports():
    df = pd.read_csv("pomodoro.csv")
    report = df.groupby('Tarefas').Tempo_Total.agg([len,'mean', max, np.sum])
    print(report)
    report2 = df.groupby('Data').Tempo_Total.agg([len,'mean', max, np.sum])
    print(report2)