import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time

root = tk.Tk()

class App:
    def __init__(self):
        self.Interface()
        self.Botao()
        self.Imagens()

    def Interface(self):
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.geometry("%dx%d" % (self.width / 1.5, self.height / 1.5))
        root.resizable(True, True)
        root.title("Animando")

    def Botao(self):
        botao = Button(
            root, text="Animar", bd=0, fg="#f54245", bg="#f27e80", command=self.Animar
        )
        botao.place(x=640, y=360)

    def Imagens(self):
        self.idle = Image.open("assets/mario_idle.png")
        self.idle_tk = ImageTk.PhotoImage(self.idle)
        self.idle_frame = tk.Frame(root)
        self.idle_frame.place(x=510, y=100)
        self.idle_label = tk.Label(self.idle_frame, image=self.idle_tk)
        self.idle_label.pack(fill=tk.BOTH, expand=tk.NO)
        self.idle_label.image = self.idle_tk

    def Animar(self):
        self.Pular()
        time.sleep(1)
        self.Cair()

    def Pular(self):
        jumping = Image.open("assets/mario_jumping.png")
        jumping_tk = ImageTk.PhotoImage(jumping)
        self.idle_label.config(image=jumping_tk)
        self.idle_label.image = jumping_tk

    def Cair(self):
        falling = Image.open("assets/mario_falling.png")
        falling_tk = ImageTk.PhotoImage(falling)
        self.idle_label.config(image=falling_tk)
        self.idle_label.image = falling_tk

if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
