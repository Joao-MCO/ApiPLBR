import customtkinter as ctk

class Bottom(ctk.CTkFrame):
    def __init__(self, master, ovr, **kwargs):
        super().__init__(master, **kwargs)

        aux = "Artilheiro: " + str(ovr.artilheiro) + " - " + str(ovr.aGols) + " gols"
        artilheiro = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        artilheiro.pack(pady=1, padx=10)

        aux = "Mais Assistências: " + str(ovr.assistente) + " - " + str(ovr.aAssistencia) + " assistências"
        assistente = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        assistente.pack(pady=1, padx=10)

        aux = "Mais Clean Sheets: " + str(ovr.topDefesa) + " - " + str(ovr.aDefesa) + " partidas"
        defensor = ctk.CTkLabel(master=master, text=aux.upper(), font=("Comfortaa", 18))
        defensor.pack(pady=1, padx=10)
        