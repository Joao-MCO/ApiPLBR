import customtkinter as ctk

class Header(ctk.CTkFrame):
    def __init__(self, master, ovr, **kwargs):
        super().__init__(master, **kwargs)

        aux = "Id " + str(ovr.id)
        id = ctk.CTkLabel(master=master, text=aux)
        id.pack(pady=1, padx=10)

        aux = str(ovr.pais)
        pais = ctk.CTkLabel(master=master, text=aux)
        pais.pack(pady=1, padx=10)

        aux = str(ovr.inicio) + " - " + str(ovr.fim)
        ano = ctk.CTkLabel(master=master, text=aux)
        ano.pack(pady=1, padx=10)

        aux = "Partidas: " + str(ovr.partidas)
        partidas = ctk.CTkLabel(master=master, text=aux)
        partidas.pack(pady=1, padx=10)