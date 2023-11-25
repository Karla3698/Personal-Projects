import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Mater panel')
        w, h = self.ventana.winfo_screenmmwidth(), self.ventana.winfo_screenheight()
        self.ventana.config(bg="red")
        self.ventana.resizable(width=0, height=0)   


        logo =utl.leer_imagen("imagenes\enido.png", (660, 880))
        dos =utl.leer_imagen("imagenes\dos.png", (647, 871))
        

        label = tk.Label( self.ventana, image=logo,bg='#3a7ff6' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        label_dos = tk.Label( self.ventana, image=dos,bg='#3a7ff6' )
        label_dos.place(x=0,y=0,relwidth=1, relheight=1)

        self.ventana.mainloop()
    