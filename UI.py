import customtkinter as ctk
import Frames
import Header
import Bottom
import tkinter

class App:

    def __init__(self, ovr, man, vis):
        root = ctk.CTk()
        root.geometry("640x640")

        titulo = ctk.CTkLabel(master=root, text=ovr[0].nome)
        titulo.pack(pady=12, padx=10)

        radio_var = tkinter.IntVar(value=0)
        radiobutton_1 = ctk.CTkRadioButton(root, text="22/23",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=0)
        radiobutton_1.pack()
        radiobutton_2 = ctk.CTkRadioButton(root, text="21/22",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=1)
        radiobutton_2.pack()
        radiobutton_3 = ctk.CTkRadioButton(root, text="20/21",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=2)
        radiobutton_3.pack()
        radiobutton_4 = ctk.CTkRadioButton(root, text="19/20",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=3)
        radiobutton_4.pack()
        radiobutton_5 = ctk.CTkRadioButton(root, text="18/19",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=4)
        radiobutton_5.pack()

        
        chamaTudo(self, root, ovr[0], man[0], vis[0])

        root.mainloop()

def chamaTudo(self, root,ovr,man,vis):
        self.geral = ctk.CTkFrame(master=root)
        self.geral.pack(pady=20, padx=60, fill="both", expand=True)
        Header.Header(self.geral, ovr)
        dentro = ctk.CTkScrollableFrame(master=self.geral)
        dentro.pack(pady=20, padx=60, fill="both", expand=True)
        Frames.FrameUm(dentro, ovr)
        Frames.FrameDois(dentro, man, 1)
        Frames.FrameDois(dentro, vis, 2)
        Bottom.Bottom(self.geral, ovr)


        


