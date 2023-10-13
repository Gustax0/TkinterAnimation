import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time

root = tk.Tk()


class App:
    def __init__(self):
        self.Interface()
        self.Botao()
        self.Pular
        self.Cair()
        self.Imagens()

    def Interface(self):
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()
        root.geometry("%dx%d" % (self.width / 1.5, self.height / 1.5))
        root.resizable(True, True)
        root.title("Animando")

    def Botao(self):
        botao = Button(
            root, text="Animar", bd=0, fg="#f54245", bg="#f27e80", command=self.Pular
        )
        botao.place(x=640, y=360)

    def Imagens(self):
        idle = Image.open("assets/mario_idle.png")
        idle_tk = ImageTk.PhotoImage(idle)
        idle_frame = tk.Frame(root)
        idle_frame.place(x=510, y=100)
        idle_label = tk.Label(idle_frame, image=idle_tk)
        idle_label.pack(fill=tk.BOTH, expand=tk.NO)
        idle_label.image = idle_tk

    def Pular(self):
        idle = Image.open("assets/mario_jumping.png")
        idle_tk = ImageTk.PhotoImage(idle)
        idle_frame = tk.Frame(root)
        idle_frame.place(x=510, y=70)
        idle_label = tk.Label(idle_frame, image=idle_tk)
        idle_label.pack(fill=tk.BOTH, expand=tk.NO)
        idle_label.image = idle_tk

    def Cair(self):
        idle = Image.open("assets/mario_falling.png")
        idle_tk = ImageTk.PhotoImage(idle)
        idle_frame = tk.Frame(root)
        idle_frame.place(x=510, y=100)
        idle_label = tk.Label(idle_frame, image=idle_tk)
        idle_label.pack(fill=tk.BOTH, expand=tk.NO)
        idle_label.image = idle_tk


if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
