import customtkinter as ctk
import Frames
import Header
import Bottom

class App:
    def __init__(self, ovr, man, vis):
        root = ctk.CTk()
        root.geometry("640x640")

        titulo = ctk.CTkLabel(master=root, text=ovr.nome)
        titulo.pack(pady=12, padx=10)

        geral = ctk.CTkFrame(master=root)
        geral.pack(pady=20, padx=60, fill="both", expand=False)
        
        Header.Header(geral, ovr)
        Frames.FrameUm(geral, ovr)
        Bottom.Bottom(geral, ovr)

        root.mainloop()



        


