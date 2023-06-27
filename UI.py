import customtkinter as ctk
import Frames
import Header
import Bottom
import tkinter
from PIL import Image

class App:

    def __init__(self, ovr, man, vis):
        root = ctk.CTk()
        root.geometry("1280x960")
        root.title("MoneyBallBrasil")
        root.tk_setPalette("green")
        #root.attributes("-fullscreen", "True")
   

          
        logo = ctk.CTkImage(light_image=Image.open("./assets/moneyball.png"),size=(500,180))
        label_title = ctk.CTkLabel(root,text="")
        label_title.pack(pady=30,padx=60,expand=False)
        label_title.grid_rowconfigure(0, weight=1)
        label_title.grid_columnconfigure(0, weight=1)

        label_logo = ctk.CTkLabel(label_title,text="" ,image=logo)
        label_logo.grid(row=0,column=0)




        radio_var = tkinter.IntVar(value=0)
        radiobutton_1 = ctk.CTkRadioButton(label_title, text="22/23",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=0)
        radiobutton_1.grid(row = 1, column = 1,padx = 10,pady= 3)
        radiobutton_2 = ctk.CTkRadioButton(label_title, text="21/22",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=1)
        radiobutton_2.grid(row = 2, column = 1,padx = 10,pady= 3)
        radiobutton_3 = ctk.CTkRadioButton(label_title, text="20/21",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=2)
        radiobutton_3.grid(row = 3, column = 1,padx = 10,pady= 3)
        radiobutton_4 = ctk.CTkRadioButton(label_title, text="19/20",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=3)
        radiobutton_4.grid(row = 4, column = 1,padx = 10,pady= 3)
        radiobutton_5 = ctk.CTkRadioButton(label_title, text="18/19",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, root, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=4)
        radiobutton_5.grid(row = 5, column = 1,padx = 10,pady= 3)



     
        chamaTudo(self, root, ovr[0], man[0], vis[0])

        root.mainloop()

def chamaTudo(self, root,ovr,man,vis):
        self.geral = ctk.CTkFrame(master=root)
        self.geral.pack(pady=20, padx=60, fill="both", expand=True)
        Header.Header(self.geral, ovr)
        dentro = ctk.CTkScrollableFrame(master=self.geral,scrollbar_fg_color = "green",scrollbar_button_color="white")
        dentro.pack(pady=20, padx=60, fill="both", expand=True)
        Frames.FrameUm(dentro, ovr)
        Frames.FrameDois(dentro, man, 1)
        Frames.FrameDois(dentro, vis, 2)
        Bottom.Bottom(self.geral, ovr)


        


