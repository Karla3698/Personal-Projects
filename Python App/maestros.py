from tkinter import *
from tkinter import ttk
from datos import *
from tkinter import messagebox

class ventana(Frame):
    maestros = sql_conexion()

    def __init__(self, master = None):
        super().__init__(master, width=680, height=360)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")
        self.habilitarOperar("normal")
        self.habilitarGuardar("disabled")
        self.id=-1

    def habilitarCajas(self,estado):
        self.nombre.configure(state=estado)
        self.curso.configure(state=estado)
        self.jornada.configure(state=estado)
        self.cursos.configure(state=estado)

    def habilitarOperar(self, estado):
        self.Nuevo.configure(state=estado)
        self.Modificar.configure(state=estado)
        self.Eliminar.configure(state=estado)

    def habilitarGuardar(self, estado):
        self.Guardar.configure(state=estado)
        self.Cancelar.configure(state=estado)

    def limpiarCajas(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def llenaDatos(self):
        datos = self.maestros.consulta_maestro()        
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2]))
        
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )

    def fNuevo(self):         
        self.habilitarCajas("normal")  
        self.habilitarOperar("disabled")
        self.habilitarGuardar("normal")
        self.limpiarCajas()        
     

    def fGuardar(self): 
        if self.id ==-1:       
          
            self.maestros.inserta_maestro(self.nombre.get(),self.curso.get(),self.jornada.get(),self.cursos.get())            
            messagebox.showinfo("Insertar", 'Elemento insertado correctamente.')
        else:
            self.maestros.modifica_maestro(self.nombre.get(),self.curso.get(),self.jornada.get(),self.cursos.get())
            messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1            
        self.limpiaGrid()
        self.llenaDatos() 
        self.limpiarCajas() 
        self.habilitarGuardar("disabled")      
        self.habilitarOperar("normal")
        self.habilitarCajas("disabled")

    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,'text')
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')
        else:
            self.id= clave
            self.habilitarCajas("normal")
            valores = self.grid.item(slected,'values')
            self.limpiarCajas()            
            self.nombre.insert(0,valores[0])
            self.curso.insert(0,valores[1]) 
            self.jornada.insert(0,valores[2])
            self.cursos.insert(0,valores[3])     
            self.habilitarOperar("disabled")
            self.habilitarGuardar("normal")

    
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def fCancelar(self):
        r = messagebox.askquestion("Calcelar", "Esta seguro que desea cancelar la operación actual")
        if r == messagebox.YES:
            self.limpiarCajas() 
            self.habilitarGuardar("disabled")      
            self.habilitarOperar("normal")
            self.habilitarCajas("disabled")      

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=359)        
        self.Nuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.Nuevo.place(x=5,y=50,width=80, height=30 )        
        self.Modificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.Modificar.place(x=5,y=90,width=80, height=30)                
        self.Eliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.Eliminar.place(x=5,y=130,width=80, height=30)        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=359)                        
              
        lbl1 = Label(frame2,text="Nombre: ")
        lbl1.place(x=3,y=55)        
        self.nombre=Entry(frame2)
        self.nombre.place(x=3,y=75,width=100, height=20)        
       
        lbl2 = Label(frame2,text="Curso: ")
        lbl2.place(x=3,y=105)        
        self.curso=Entry(frame2)
        self.curso.place(x=3,y=125,width=100, height=20)

        lbl3 = Label(frame2,text="Jornada: ")
        lbl3.place(x=3,y=155)        
        self.jornada=Entry(frame2)
        self.jornada.place(x=3,y=175,width=100, height=20)        
       
        lbl4 = Label(frame2,text="No. de cursos que enseña: ")
        lbl4.place(x=3,y=205)        
        self.cursos=Entry(frame2)
        self.cursos.place(x=3,y=225,width=100, height=20)           
      
        self.Guardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.Guardar.place(x=10,y=290,width=60, height=30)
        self.Cancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.Cancelar.place(x=80,y=290,width=60, height=30)         
        frame3 = Frame(self,bg="yellow" )
        frame3.place(x=247,y=0,width=420, height=359)                      
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=60)
        self.grid.column("col1",width=70, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=70, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
       
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Curso", anchor=CENTER)
        self.grid.heading("col3", text="Jornada", anchor=CENTER)
        self.grid.heading("col4", text="No. de cursos que enseña", anchor=CENTER)              
        self.grid.pack(side=LEFT,fill = Y)        
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill = Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse' 