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
        root.geometry(f"800x600+{self.screen_width // 2 - 400}+{self.screen_height // 2 - 300}")
        root.resizable(True, True)
        root.title("Animando")

    def Botao(self):
        button_center_x = self.screen_width // 2
        button_center_y = self.screen_height // 2 + 200
        botao = Button(
            root, text="Animar", bd=0, fg="#f54245", bg="#f27e80", command=self.Animar
        )
        botao.place(x=button_center_x, y=button_center_y)

    def Imagens(self):
        self.idle = Image.open("assets/mario_idle.png")
        width, height = self.idle.size
        factor = min(self.screen_width / width, self.screen_height / height)
        new_width = int(width * factor)
        new_height = int(height * factor)
        self.idle = self.idle.resize((new_width, new_height), Image.ANTIALIAS)
        self.idle_tk = ImageTk.PhotoImage(self.idle)
        self.idle_label = tk.Label(root, image=self.idle_tk)
        self.idle_label.place(x=(self.screen_width - new_width) // 2, y=(self.screen_height - new_height) // 2)

    def Animar(self):
        self.Pular()
        time.sleep(1)
        self.Cair()

    def Pular(self):
        jumping = Image.open("assets/mario_jumping.png")
        width, height = jumping.size
        factor = min(self.screen_width / width, self.screen_height / height)
        new_width = int(width * factor)
        new_height = int(height * factor)
        jumping = jumping.resize((new_width, new_height), Image.ANTIALIAS)
        jumping_tk = ImageTk.PhotoImage(jumping)
        self.idle_label.config(image=jumping_tk)
        self.idle_label.image = jumping_tk

    def Cair(self):
        falling = Image.open("assets/mario_falling.png")
        width, height = falling.size
        factor = min(self.screen_width / width, self.screen_height / height)
        new_width = int(width * factor)
        new_height = int(height * factor)
        falling = falling.resize((new_width, new_height), Image.ANTIALIAS)
        falling_tk = ImageTk.PhotoImage(falling)
        self.idle_label.config(image=falling_tk)
        self.idle_label.image = falling_tk

if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
