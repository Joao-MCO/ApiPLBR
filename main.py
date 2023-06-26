import requests
import Liga
import customtkinter as ctk
import UI
      
api = "http://localhost:3000/"
res = requests.get(api)

liga = res.json()['data']

ovr = Liga.Liga(liga)
man = Liga.Mandante(liga)
vis = Liga.Visitante(liga)

UI.App(ovr, man, vis)