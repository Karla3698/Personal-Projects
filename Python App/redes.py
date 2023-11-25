import tkinter as tk
from tkinter import ttk
import util.generic as utl
import webbrowser

class redes():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Redes sociales')
        self.ventana.geometry('650x750')
        self.ventana.config(bg='white')
        #self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 650, 750)

        f = utl.leer_imagen("imagenes\Facebook_f_logo_(2019).svg.png", (80, 80))
        d = utl.leer_imagen("imagenes\discord.png", (80, 80))
        l = utl.leer_imagen("imagenes\linkedin-logo-3.png", (80, 80))
        i = utl.leer_imagen("imagenes\insta.png", (80, 80))
        tw = utl.leer_imagen("imagenes\purple-twitch-logo-png-18.png", (80, 80))
        q = utl.leer_imagen("imagenes\quora.png", (80, 80))
        r = utl.leer_imagen("imagenes\eddit.png", (80, 80))
        s = utl.leer_imagen("imagenes\snap.png", (80, 80))
        tel = utl.leer_imagen("imagenes\Telegram_logo.svg.png", (80, 80))
        tik = utl.leer_imagen("imagenes\iktok.png", (80, 80))
        tw = utl.leer_imagen("imagenes\w.png", (80, 80))
        we = utl.leer_imagen("imagenes\wechat-logo.png", (80, 80))
        wa = utl.leer_imagen("imagenes\WhatsApp-logo.png", (80, 80))
        you = utl.leer_imagen("imagenes\Youtube_logo.png", (80, 80))
        p = utl.leer_imagen("imagenes\pinterest.png", (80, 80))

        def abrir_enlace():
            app = "https://es-la.facebook.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(app)

        def abrir_crunch():
            c = "https://discord.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(c)

        def abrir_disney():
            d = "https://gt.linkedin.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(d)

        def abrir_hbo():
            h = "https://www.instagram.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(h)

        def abrir_hulu():
            lu = "https://www.twitch.tv/?lang=es"  # URL del hipervínculo que deseas abrir
            webbrowser.open(lu)

        def abrir_net():
            net = "https://es.quora.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(net)
        
        def abrir_mount():
            mount = "https://www.reddit.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(mount)

        def abrir_pluto():
            pl = "https://www.snapchat.com/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(pl)

        def abrir_amazon():
            zon = "https://web.telegram.org/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(zon)

        def abrir_star():
            tar = "https://www.tiktok.com/es/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(tar)

        def abrir_tw():
            t = "https://twitter.com/?lang=es"  # URL del hipervínculo que deseas abrir
            webbrowser.open(t)
        
        def abrir_we():
            we = "https://www.wechat.com/es/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(we)

        def abrir_wa():
            wa = "https://www.whatsapp.com/?lang=es"  # URL del hipervínculo que deseas abrir
            webbrowser.open(wa)

        def abrir_you():
            y = "https://www.youtube.com/?hl=es-419&gl=GT"  # URL del hipervínculo que deseas abrir
            webbrowser.open(y)

        def abrir_pi():
            pi = "https://www.pinterest.ca/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(pi)

        #posición imagenes
        titulo = tk.Label(self.ventana, text="Entretenimiento", font='Calibri  24', bg='white')
        titulo.place(x=230, y=50)

        a = tk.Button(self.ventana, image=f, bg= 'white', command=abrir_enlace)
        a.place(x=50, y=150)
       
        dos = tk.Button(self.ventana, image=d, bg='white', command=abrir_crunch)
        dos.place(x=160, y=150)

        tres = tk.Button(self.ventana, image=l, bg='white', command=abrir_disney)
        tres.place(x=270, y=150)

        cuatro = tk.Button(self.ventana, image=i, bg='white', command=abrir_hbo)
        cuatro.place(x=380, y=150)

        cinco = tk.Button(self.ventana, image=tw, bg='white', command=abrir_hulu)
        cinco.place(x=490, y=150)

        seis = tk.Button(self.ventana, image=q, bg='white', command=abrir_net)
        seis.place(x=50, y=300)

        siete = tk.Button(self.ventana, image=r, bg='white', command=abrir_mount)
        siete.place(x=160, y=300)

        ocho = tk.Button(self.ventana, image=s, bg='white', command=abrir_pluto)
        ocho.place(x=270, y=300)

        nueve = tk.Button(self.ventana, image=tel, bg='white', command=abrir_amazon)
        nueve.place(x=380, y=300)

        diez = tk.Button(self.ventana, image=tik, bg='white', command=abrir_star)
        diez.place(x=490, y=300)

        once = tk.Button(self.ventana, image=tw, bg='white', command=abrir_tw)
        once.place(x=50, y=450)

        doce = tk.Button(self.ventana, image=we, bg='white', command=abrir_we)
        doce.place(x=160, y=450)

        trece = tk.Button(self.ventana, image=wa, bg='white', command=abrir_wa)
        trece.place(x=270, y=450)

        catorce = tk.Button(self.ventana, image=you, bg='white', command=abrir_you)
        catorce.place(x=380, y=450)

        quince = tk.Button(self.ventana, image=p, bg='white', command=abrir_pi)
        quince.place(x=490, y=450)

   
                


        
        # end frame_form_fill
        self.ventana.mainloop()