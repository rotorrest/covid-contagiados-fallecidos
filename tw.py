import requests
import os
import pandas as pd

from dotenv import load_dotenv
from tqdm import tqdm
from fake_headers import Headers

from core.graphs import Graph

def create_graphs():
  
  load_dotenv()
  URL_positivos = os.getenv('URL_positivos')
  URL_fallecidos = os.getenv('URL_fallecidos')
  departamentos = ['AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','CAJAMARCA','CALLAO','CUSCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MOQUEGUA','PASCO','PIURA','PUNO','SAN MARTIN','TACNA','TUMBES','UCAYALI']
  header=Headers()

  #E
  response_positivos = requests.get(URL_positivos, headers=header.generate())
  response_fallecidos = requests.get(URL_fallecidos, headers=header.generate())

  Graph.folders()
  Graph.save_csv_from_response(response_fallecidos, "fallecidos")
  Graph.save_csv_from_response(response_positivos, "positivos")

  df_positivos = pd.read_csv('positivos.csv', sep=';') 
  df_fallecidos = pd.read_csv('fallecidos.csv', sep=';') 

  os.remove('positivos.csv')
  os.remove('fallecidos.csv')

  #T
  positivos = Graph.pivot_index(df_positivos, "FECHA_RESULTADO")
  fallecidos = Graph.pivot_index(df_fallecidos, "FECHA_FALLECIMIENTO")
  date_positivos = Graph.date_list(positivos)
  date_fallecidos = Graph.date_list(fallecidos)
      
  for i in tqdm(range(len(departamentos)), ncols=50):
    Graph.departamento_plot(departamentos, date_positivos, date_fallecidos, positivos, fallecidos, i)