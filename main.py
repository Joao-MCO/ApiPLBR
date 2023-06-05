import requests
import pandas as pd
import Liga
      
api = "http://localhost:3000/"
res = requests.get(api)

liga = res.json()['data']

ovr = Liga.Liga(liga)
man = Liga.Mandante(liga)
vis = Liga.Visitante(liga)

api += "times"
res = requests.get(api)
cl = res.json()['data']
clubes = []
for i in cl:
    clubes.append([i['id'], i['cleanName']])

df = pd.DataFrame(clubes)
pd.DataFrame.to_json(df, "times.json")