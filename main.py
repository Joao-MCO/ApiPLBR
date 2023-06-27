import requests
import Liga
import UI
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


ovr = []
man = []
vis = []
key = 3000
for i in range(5):
    api = "http://localhost:" + str(key+i) + "/"
    res = requests.get(api)
    liga = res.json()['data']
    ovr.append(Liga.Liga(liga))
    man.append(Liga.Mandante(liga))
    vis.append(Liga.Visitante(liga))

UI.App(ovr, man, vis)