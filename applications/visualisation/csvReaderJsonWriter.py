
import pandas as pd
import json

csvFilePath='dataSet2.csv'
jsonFilePath='dataSet2.json'

def csv_to_json(csvFilePath, jsonFilePath):
 
 df=pd.read_csv(csvFilePath,sep=';',header='infer')
 df.to_json(jsonFilePath,orient='records')

  
csv_to_json(csvFilePath,jsonFilePath)
