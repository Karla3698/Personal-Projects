import tkinter as tk
from tkinter import ttk
import util.generic as utl
import webbrowser

class entretenimiento():

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Entretenimiento')
        self.ventana.geometry('650x500')
        self.ventana.config(bg='white')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 650, 500)

        apple = utl.leer_imagen("imagenes\ple.png", (80, 80))
        crunch = utl.leer_imagen("imagenes\crunchyroll.png", (80, 80))
        disney = utl.leer_imagen("imagenes\disney.png", (80, 80))
        hbo = utl.leer_imagen("imagenes\hbo.png", (80, 80))
        hulu = utl.leer_imagen("imagenes\hulu.png", (80, 80))
        netflix = utl.leer_imagen("imagenes\lix.png", (80, 80))
        para = utl.leer_imagen("imagenes\paramount-plus-logo.png", (80, 80))
        pluto = utl.leer_imagen("imagenes\pluto.png", (80, 80))
        amazon = utl.leer_imagen("imagenes\mazon.jpg", (80, 80))
        star = utl.leer_imagen("imagenes\star.png", (80, 80))

        def abrir_enlace():
            app = "https://www.apple.com/la/apple-tv-plus/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(app)

        def abrir_crunch():
            c = "https://www.crunchyroll.com/es/offer-premium?utm_source=google&utm_medium=paid_cr&utm_campaign=CR-Paid_Google_Web_Conversion_LATAM_ALL_Trademark_SVOD&utm_term=crunchyroll&referrer=google_paid_cr_CR-Paid_Google_Web_Conversion_LATAM_ALL_Trademark_SVOD&gclid=Cj0KCQjwpPKiBhDvARIsACn-gzDf01hqRWoQ6zjjEQgBGpwiAJZ9U5-pBZou4m4hT1HreYmhVjIM3D8aAqT8EALw_wcB"  # URL del hipervínculo que deseas abrir
            webbrowser.open(c)

        def abrir_disney():
            d = "https://www.disneyplus.com/es-gt?cid=DSS-Search-Google-71700000076092956-&s_kwcid=AL!8468!3!644679583637!e!!g!!disney&gclid=Cj0KCQjwpPKiBhDvARIsACn-gzCj_VTfNQUqSZYdO9b8WzCxfUvyfGDrI_JnzxoR-BCjEka9B5ibrFIaAokCEALw_wcB&gclsrc=aw.ds"  # URL del hipervínculo que deseas abrir
            webbrowser.open(d)

        def abrir_hbo():
            h = "https://www.hbomax.com/gt/es"  # URL del hipervínculo que deseas abrir
            webbrowser.open(h)

        def abrir_hulu():
            lu = "https://www.hulu.com/welcome?orig_referrer=https%3A%2F%2Fwww.google.com%2F"  # URL del hipervínculo que deseas abrir
            webbrowser.open(lu)

        def abrir_net():
            net = "https://www.netflix.com/gt/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(net)
        
        def abrir_mount():
            mount = "https://www.paramountplus.com/gt/?ftag=IPP-02-10aej0a&gclid=Cj0KCQjwpPKiBhDvARIsACn-gzAtG6YNsAVyybbMmHZ8zQer5_BtP7e6uZOx-QJKOHKOm1v17h0roXYaAo8gEALw_wcB"  # URL del hipervínculo que deseas abrir
            webbrowser.open(mount)

        def abrir_pluto():
            pl = "https://pluto.tv/"  # URL del hipervínculo que deseas abrir
            webbrowser.open(pl)

        def abrir_amazon():
            zon = "https://www.primevideo.com/offers/nonprimehomepage/ref=dvm_pds_brd_gt_hk_s_g_mkw_sELlfnqZs-dc_pcrid_645960032065?mrntrk=slid__pgrid_42306244048_pgeo_9069799_x__adext__ptid_kwd-2850171361"  # URL del hipervínculo que deseas abrir
            webbrowser.open(zon)

        def abrir_star():
            tar = "https://www.starplus.com/es-gt?cid=DSS-Search-Google-71700000086323555-&s_kwcid=AL!8468!3!541988575612!e!!g!!star%20plus&gclid=Cj0KCQjwpPKiBhDvARIsACn-gzAyEFG0UKkrxdRX6m67EMBBNbuSKalhFmSbiacUR9EpInK9sAOO1-4aAvFdEALw_wcB&gclsrc=aw.ds"  # URL del hipervínculo que deseas abrir
            webbrowser.open(tar)


        #posición imagenes
        titulo = tk.Label(self.ventana, text="Entretenimiento", font='Calibri  24', bg='white')
        titulo.place(x=230, y=50)

        a = tk.Button(self.ventana, image=apple, bg= 'white', command=abrir_enlace)
        a.place(x=50, y=150)
       
        dos = tk.Button(self.ventana, image=crunch, bg='white', command=abrir_crunch)
        dos.place(x=160, y=150)

        tres = tk.Button(self.ventana, image=disney, bg='white', command=abrir_disney)
        tres.place(x=270, y=150)

        cuatro = tk.Button(self.ventana, image=hbo, bg='white', command=abrir_hbo)
        cuatro.place(x=380, y=150)

        cinco = tk.Button(self.ventana, image=hulu, bg='white', command=abrir_hulu)
        cinco.place(x=490, y=150)

        seis = tk.Button(self.ventana, image=netflix, bg='white', command=abrir_net)
        seis.place(x=50, y=300)

        siete = tk.Button(self.ventana, image=para, bg='white', command=abrir_mount)
        siete.place(x=160, y=300)

        ocho = tk.Button(self.ventana, image=pluto, bg='white', command=abrir_pluto)
        ocho.place(x=270, y=300)

        nueve = tk.Button(self.ventana, image=amazon, bg='white', command=abrir_amazon)
        nueve.place(x=380, y=300)

        diez = tk.Button(self.ventana, image=star, bg='white', command=abrir_star)
        diez.place(x=490, y=300)
   
                


        
        # end frame_form_fill
        self.ventana.mainloop()