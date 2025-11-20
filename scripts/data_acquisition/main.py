import pandas as pd

df = pd.read_csv(r"D:\CURSOS\Universidad Nacional\modulo 6\entregas proyecto\Heart_Failure_Analysis\data\heart.csv")
print(df.info()) #No se detectaron datos faltantes
print(df.head()) 
