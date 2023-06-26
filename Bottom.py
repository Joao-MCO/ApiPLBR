import customtkinter as ctk

class Bottom(ctk.CTkFrame):
    def __init__(self, master, ovr, **kwargs):
        super().__init__(master, **kwargs)

        aux = "Artilheiro: " + str(ovr.artilheiro) + " - " + str(ovr.aGols) + " gols"
        artilheiro = ctk.CTkLabel(master=master, text=aux)
        artilheiro.pack(pady=1, padx=10)

        aux = "Mais Assistências: " + str(ovr.assistente) + " - " + str(ovr.aAssistencia) + " assistências"
        assistente = ctk.CTkLabel(master=master, text=aux)
        assistente.pack(pady=1, padx=10)

        aux = "Mais Clean Sheets: " + str(ovr.topDefesa) + " - " + str(ovr.aDefesa) + " partidas"
        defensor = ctk.CTkLabel(master=master, text=aux)
        defensor.pack(pady=1, padx=10)
        