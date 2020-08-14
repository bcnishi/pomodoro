import pandas as pd
import os

def create():
    if os.path.exists("pomodoro.csv"):
        None
    else:
        df = pd.DataFrame({'Tarefas': [], 'Data': [],'Pomodoro':[],'Ciclo':[], 'Tempo Total':[]})
        df.to_csv("pomodoro.csv",index=False,encoding='utf-8')
    
create()
