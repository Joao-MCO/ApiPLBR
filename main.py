import requests
import pandas as pd
import Liga
      
api = "http://localhost:3000/"
res = requests.get(api)

liga = res.json()['data']

ovr = Liga.Liga(liga)
man = Liga.Mandante(liga)
vis = Liga.Visitante(liga)
