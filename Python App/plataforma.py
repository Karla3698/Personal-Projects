import tkinter as tk
from tkinter import ttk
import util.generic as utl
import webbrowser


class plataforma():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Liceo Las Aguilas')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 500)


        def abrir_enlace():
            url = "https://mylcto.edu.gt/login/index.php"  # URL del hipervínculo que deseas abrir
            webbrowser.open(url)


            boton = tk.Button(ventana, text="Plataforma educativa", command=abrir_enlace)
            boton.pack()



                


        
        # end frame_form_fill
        self.ventana.mainloop()