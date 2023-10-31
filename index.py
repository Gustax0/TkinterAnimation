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
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        root.geometry(f"800x600")
        root.update_idletasks() 
        x_offset = (self.screen_width - root.winfo_width()) // 2
        y_offset = (self.screen_height - root.winfo_height()) // 2
        root.geometry(f"+{x_offset}+{y_offset}") 
        root.resizable(True, True)
        root.title("Animando")

    def Botao(self):
        button_center_x = root.winfo_width() // 2
        button_center_y = root.winfo_height() // 2 + (root.winfo_height() // 5)
        botao = Button(
            root, text="Animar", bd=0, fg="#f54245", bg="#f27e80", command=self.Animar
        )
        botao.place(x=button_center_x, y=button_center_y, anchor=CENTER)

    def Imagens(self):
        self.idle = Image.open("assets/mario_idle.png")
        self.idle = self.idle.resize((self.idle.width, self.idle.height))
        self.idle_tk = ImageTk.PhotoImage(self.idle)
        sprite_x = root.winfo_width() // 2 - self.idle.width // 2
        sprite_y = root.winfo_height() // 2 - self.idle.height // 2
        self.idle_label = tk.Label(root, image=self.idle_tk)
        self.idle_label.place(x=sprite_x, y=sprite_y)

    def Animar(self):
        self.Pular()
        root.after(1000, self.Cair) 

    def Pular(self):
        jumping = Image.open("assets/mario_jumping.png")
        jumping = jumping.resize((jumping.width, jumping.height))
        jumping_tk = ImageTk.PhotoImage(jumping)
        self.idle_label.config(image=jumping_tk)
        self.idle_label.image = jumping_tk

    def Cair(self):
        falling = Image.open("assets/mario_falling.png")
        falling = falling.resize((falling.width, falling.height))
        falling_tk = ImageTk.PhotoImage(falling)
        self.idle_label.config(image=falling_tk)
        self.idle_label.image = falling_tk

if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
