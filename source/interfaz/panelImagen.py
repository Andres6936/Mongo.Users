import tkinter as tk

from PIL import Image, ImageTk

class PanelImagen(tk.Frame):
    
    def __init__(self, parent):
        
        tk.Frame.__init__(self, parent)
        
        self.config(background='white')
        
        image = Image.open("data/Titulo.png")
        banner = ImageTk.PhotoImage(image)
        
        self.label = tk.Label(image=banner)
        self.label.imagen = banner
        self.label.grid(row=0)
