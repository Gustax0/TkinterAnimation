import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

root = tk.Tk()


class App:
    def __init__(self):
        root.bind("<KeyPress>", self.espaco)
        self.Interface()
        # self.Back()
        self.Imagens()
        self.Botao()

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
            root,
            text="Pular",
            bd=0,
            fg="#f54245",
            bg="#f27e80",
            font=("Helvetica 20 bold italic"),
            command=self.Animar,
        )
        botao.place(x=button_center_x, y=button_center_y, anchor=CENTER)

    def Imagens(self):
        self.idle = Image.open("assets/mario_idle.png")
        self.idle = self.idle.resize((self.idle.width, self.idle.height))
        self.idle_tk = ImageTk.PhotoImage(self.idle)
        self.sprite_x = root.winfo_width() // 2 - self.idle.width // 2
        self.sprite_y = root.winfo_height() // 2 - self.idle.height // 2
        self.idle_label = tk.Label(root, image=self.idle_tk)
        self.idle_label.place(x=self.sprite_x, y=self.sprite_y)

    def Animar(self):
        self.Pular(0)

    def espaco(self, event):
        if event.keysym == "space":
            self.Animar()

    def Pular(self, counter):
        if counter < 7:
            jumping = Image.open("assets/mario_jumping.png")
            jumping = jumping.resize((jumping.width, jumping.height))
            self.jumping_tk = ImageTk.PhotoImage(jumping)
            self.idle_label.config(image=self.jumping_tk)
            self.idle_label.image = self.jumping_tk
            self.sprite_y -= 15
            self.idle_label.place(x=self.sprite_x, y=self.sprite_y)
            root.after(50, self.Pular, counter + 1)
        else:
            self.Cair(0)

    def Cair(self, counter):
        if counter < 7:
            falling = Image.open("assets/mario_falling.png")
            falling = falling.resize((falling.width, falling.height))
            falling_tk = ImageTk.PhotoImage(falling)
            self.idle_label.config(image=falling_tk)
            self.idle_label.image = falling_tk
            self.sprite_y += 15
            self.idle_label.place(x=self.sprite_x, y=self.sprite_y)
            root.after(50, self.Cair, counter + 1)
        else:
            self.VoltarIdle()

    def VoltarIdle(self):
        self.idle_label.config(image=self.idle_tk)
        self.idle_label.image = self.idle_tk

    def Back(self):
        self.background = Image.open("assets/background.png")
        self.background_tk = ImageTk.PhotoImage(self.background)
        self.background_x = root.winfo_width() // 2 - self.background.width // 2
        self.background_y = root.winfo_height() // 2 - self.background.height // 2
        self.background_label = tk.Label(root, image=self.background_tk)
        self.background_label.place(x=self.background_x, y=self.background_y)


if __name__ == "__main__":
    app = App()
    root.mainloop()
else:
    print("Algum erro foi detectado")
