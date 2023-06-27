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

        frame = ctk.CTkScrollableFrame(root, width=1280, height=960, fg_color="#B1DD9E")
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        frame.pack(pady = 10, padx=30)

        logo = ctk.CTkImage(light_image=Image.open("./assets/moneyball.png"),size=(500,180))
        label_title = ctk.CTkLabel(frame,text="", image=logo)
        label_title.grid(pady=30,padx=60, row=0, column=0)

        radio_var = tkinter.IntVar(value=0)
        radiobutton_1 = ctk.CTkRadioButton(frame, text="22/23",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, frame, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=0)
        radiobutton_1.grid(row = 1, column = 0,padx = 10,pady= 3)
        radiobutton_2 = ctk.CTkRadioButton(frame, text="21/22",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, frame, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=1)
        radiobutton_2.grid(row = 2, column = 0,padx = 10,pady= 3)
        radiobutton_3 = ctk.CTkRadioButton(frame, text="20/21",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, frame, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=2)
        radiobutton_3.grid(row = 3, column = 0,padx = 10,pady= 3)
        radiobutton_4 = ctk.CTkRadioButton(frame, text="19/20",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, frame, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=3)
        radiobutton_4.grid(row = 4, column = 0,padx = 10,pady= 3)
        radiobutton_5 = ctk.CTkRadioButton(frame, text="18/19",
                                             command=lambda : [self.geral.destroy(), chamaTudo(self, frame, ovr[radio_var.get()], man[radio_var.get()], vis[radio_var.get()])], variable= radio_var, value=4)
        radiobutton_5.grid(row = 5, column = 0,padx = 10,pady= 3)
     
        chamaTudo(self, frame, ovr[0], man[0], vis[0])

        root.mainloop()

def chamaTudo(self, root,ovr,man,vis):
        self.geral = ctk.CTkFrame(master=root, width=1280, fg_color="#6F8F72")
        self.geral.grid(pady=20, padx=60, row=6, column=0)
        Header.Header(self.geral, ovr)
        dentro = ctk.CTkScrollableFrame(master=self.geral,scrollbar_fg_color = "green",scrollbar_button_color="white", width=1280, height=480)
        dentro.pack(pady=20, padx=60, fill="both", expand=True)
        Frames.FrameUm(dentro, ovr, border_width=10, border_color = "black")
        Frames.FrameDois(dentro, man, 1, border_width=10, border_color = "black")
        Frames.FrameDois(dentro, vis, 2, border_width=10, border_color = "black")
        Bottom.Bottom(self.geral, ovr)


        


