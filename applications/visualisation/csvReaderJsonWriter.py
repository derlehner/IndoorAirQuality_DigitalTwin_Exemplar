
import pandas as pd

csvFilePath='co2data.csv'
jsonFilePath='co2data.json'

def csv_to_json(csvFilePath, jsonFilePath):
 
 df=pd.read_csv(csvFilePath)
 df.to_json(jsonFilePath,orient='records')
  
csv_to_json(csvFilePath,jsonFilePath)
