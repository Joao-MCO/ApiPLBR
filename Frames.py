import customtkinter as ctk

class FrameUm(ctk.CTkFrame):
    def __init__(self, master, ovr, **kwargs):
        super().__init__(master, **kwargs)

        titulo = ctk.CTkLabel(master=master, text="Geral")
        titulo.pack()
        frame = ctk.CTkFrame(master=master, width=1280, height=480)
        frame.pack(pady=30, padx=60, fill="both", expand=True, anchor="w")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1) 

        golsT = ctk.CTkLabel(master=frame, text="GOLS")
        golsT.grid(row=0, column=0, padx=0, pady=5)
        golsR = ctk.CTkLabel(master=frame, text=ovr.gols)
        golsR.grid(row=0, column=1, padx=10, pady=5)

        escanteiosT = ctk.CTkLabel(master=frame, text="ESCANTEIOS")
        escanteiosT.grid(row=1, column=0, padx=0, pady = 5)
        escanteiosT = ctk.CTkLabel(master=frame, text=ovr.escanteios)
        escanteiosT.grid(row=1, column=1, padx=10, pady = 5)

        cartoesT = ctk.CTkLabel(master=frame, text="CARTÕES")
        cartoesT.grid(row=2, column=0, padx=0, pady=5)
        cartoesR = ctk.CTkLabel(master=frame, text=ovr.cartoes)
        cartoesR.grid(row=2, column=1, padx=10, pady=5)

        faltasT = ctk.CTkLabel(master=frame, text="FALTAS")
        faltasT.grid(row=3, column=0, padx=0, pady=5)
        faltasR = ctk.CTkLabel(master=frame, text=ovr.faltas)
        faltasR.grid(row=3, column=1, padx=10, pady=5)

        chutesT = ctk.CTkLabel(master=frame, text="CHUTES")
        chutesT.grid(row=4, column=0, padx=0, pady=5)
        chutesR = ctk.CTkLabel(master=frame, text=ovr.chutes)
        chutesR.grid(row=4, column=1, padx=10, pady=5)

        impedimentosT = ctk.CTkLabel(master=frame, text="IMPEDIMENTOS")
        impedimentosT.grid(row=5, column=0, padx=0, pady=5)
        impedimentosR = ctk.CTkLabel(master=frame, text=ovr.impedimentos)
        impedimentosR.grid(row=5, column=1, padx=10, pady=5)

        numeroT = ctk.CTkLabel(master=frame, text="NÚMERO DE JOGADORES")
        numeroT.grid(row=6, column=0, padx=0, pady=5)
        numeroR = ctk.CTkLabel(master=frame, text=ovr.numeroJogadores)
        numeroR.grid(row=6, column=1, padx=10, pady=5)

        ambosT = ctk.CTkLabel(master=frame, text="AMBOS MARCAM")
        ambosT.grid(row=7, column=0, padx=0, pady=5)
        ambosR = ctk.CTkLabel(master=frame, text=ovr.ambosMarcam)
        ambosR.grid(row=7, column=1, padx=10, pady=5)

class FrameDois(ctk.CTkFrame):
    def __init__(self, master, ovr, index ,**kwargs):
        super().__init__(master, **kwargs)

        if(index==1):
            titulo = ctk.CTkLabel(master=master, text="Mandante")
        else:
            titulo = ctk.CTkLabel(master=master, text="Visitante")
        
        titulo.pack()


        frame = ctk.CTkFrame(master=master, width=1280, height=480, border_color = "black")
        frame.pack(pady=30, padx=60, fill="both", expand=True, anchor="w")

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1) 

        golsT = ctk.CTkLabel(master=frame, text="GOLS")
        golsT.grid(row=0, column=0, padx=0, pady=5)
        golsR = ctk.CTkLabel(master=frame, text=ovr.gols)
        golsR.grid(row=0, column=1, padx=10, pady=5)

        escanteiosT = ctk.CTkLabel(master=frame, text="ESCANTEIOS")
        escanteiosT.grid(row=1, column=0, padx=0, pady = 5)
        escanteiosT = ctk.CTkLabel(master=frame, text=ovr.escanteios)
        escanteiosT.grid(row=1, column=1, padx=10, pady = 5)

        cartoesT = ctk.CTkLabel(master=frame, text="CARTÕES")
        cartoesT.grid(row=2, column=0, padx=0, pady=5)
        cartoesR = ctk.CTkLabel(master=frame, text=ovr.cartoes)
        cartoesR.grid(row=2, column=1, padx=10, pady=5)

        faltasT = ctk.CTkLabel(master=frame, text="FALTAS")
        faltasT.grid(row=3, column=0, padx=0, pady=5)
        faltasR = ctk.CTkLabel(master=frame, text=ovr.faltas)
        faltasR.grid(row=3, column=1, padx=10, pady=5)

        chutesT = ctk.CTkLabel(master=frame, text="CHUTES")
        chutesT.grid(row=4, column=0, padx=0, pady=5)
        chutesR = ctk.CTkLabel(master=frame, text=ovr.chutes)
        chutesR.grid(row=4, column=1, padx=10, pady=5)

        impedimentosT = ctk.CTkLabel(master=frame, text="IMPEDIMENTOS")
        impedimentosT.grid(row=5, column=0, padx=0, pady=5)
        impedimentosR = ctk.CTkLabel(master=frame, text=ovr.impedimentos)
        impedimentosR.grid(row=5, column=1, padx=10, pady=5)

        numeroT = ctk.CTkLabel(master=frame, text="VITORIAS")
        numeroT.grid(row=6, column=0, padx=0, pady=5)
        numeroR = ctk.CTkLabel(master=frame, text=ovr.vitorias)
        numeroR.grid(row=6, column=1, padx=10, pady=5)

        cleanT = ctk.CTkLabel(master=frame, text="CLEAN SHEETS")
        cleanT.grid(row=7, column=0, padx=0, pady=5)
        cleanR = ctk.CTkLabel(master=frame, text=ovr.cleanSheets)
        cleanR.grid(row=7, column=1, padx=10, pady=5)

        failedT = ctk.CTkLabel(master=frame, text="FAILED TO SCORE")
        failedT.grid(row=8, column=0, padx=0, pady=5)
        failedR = ctk.CTkLabel(master=frame, text=ovr.failedScore)
        failedR.grid(row=8, column=1, padx=10, pady=5)