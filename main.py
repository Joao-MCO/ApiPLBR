import requests
import pandas as pd
import Liga
import tkinter as tk
import UI
      
api = "http://localhost:3000/"
res = requests.get(api)

liga = res.json()['data']

ovr = Liga.Liga(liga)
man = Liga.Mandante(liga)
vis = Liga.Visitante(liga)

root = tk.Tk()
myapp = UI.App(root)
myapp.mainloop()