import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, master, ovr, **kwargs):
        super().__init__(master,**kwargs)

        titulo = ctk.CTkLabel(master=master, text=ovr.nome.upper(), font=("Comfortaa", 24))
        titulo.pack(pady=12, padx=10)

        aux = "Id " + str(ovr.id)
        id = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        id.pack(pady=1, padx=10)

        aux = str(ovr.pais)
        pais = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        pais.pack(pady=1, padx=10)

        aux = str(ovr.inicio) + " - " + str(ovr.fim)
        ano = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        ano.pack(pady=1, padx=10)

        aux = "Partidas: " + str(ovr.partidas)
        partidas = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        partidas.pack(pady=1, padx=10)