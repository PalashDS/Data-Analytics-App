import pandas as pd
 
def run_analysis():
     data = pd.read_csv('data/Titanic-Dataset.csv')
     return {'mean': data['value'].mean()}