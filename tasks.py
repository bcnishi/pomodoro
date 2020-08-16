import pandas as pd
import numpy as np
import os

def create():
    if os.path.exists("pomodoro.csv"):
        None
    else:
        df = pd.DataFrame({
            'Tarefas': ["Estudar python","Estudar Métricas","Trabalhar no projeto da Paolla"],
            'Data': ["14/08/2020","15/08/2020","16/08/2020"],
            'Pomodoro':[25,25,30],'Ciclo':[1,2,3], 'Tempo_Total':[25,50,90]})
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

def del_task():
    df = pd.read_csv("pomodoro.csv")
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
    df = df.reset_index()
    print(df.drop(r))
    df.to_csv("pomodoro.csv",index=False,encoding='utf-8')

def reports():
    df = pd.read_csv("pomodoro.csv")
    report = df.groupby('Tarefas').Tempo_Total.agg([len, 'mean', max, np.sum])
    print(report)
