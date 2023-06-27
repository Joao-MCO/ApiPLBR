import requests
import Liga
import UI

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