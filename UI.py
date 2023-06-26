import customtkinter as ctk

class App:
    def __init__(self, ovr, man, vis):
        root = ctk.CTk()
        root.geometry("640x480")

        frame = ctk.CTkFrame(master=root)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text=ovr.nome)
        label.pack(pady=12, padx=10)

        
        root.mainloop()



        


