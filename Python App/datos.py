import pymysql 

class sql_conexion:
    
    def __init__(self):

    # To connect MySql database
     self.cnn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password= "",
        db = 'usuarios'
     )

    def __str__(self):
        datos=self.consulta_paises()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_alumno(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM alumnos")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_alumno(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM alumnos WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def consulta_maestro(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM maestros")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_maestro(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM maestros WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    

    def inserta_usuario(self,Name, usuario, correo, contra):
        cur = self.cnn.cursor()
        sql='''INSERT INTO registro (nombre, usuario, correo, contra) 
        VALUES('{}', '{}','{}', '{}')'''.format(Name, usuario, correo, contra)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def inserta_maestro(self,nombre, curso, jornada, cursos):
        cur = self.cnn.cursor()
        sql='''INSERT INTO maestros (nombre, curso, jornada, cursos) 
        VALUES('{}', '{}','{}', '{}')'''.format(nombre, curso, jornada, cursos)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  

    def elimina_maestro(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM maestros WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_maestro(self,Id, nombre, curso, jornada, cursos):
        cur = self.cnn.cursor()
        sql='''UPDATE maestros  nombre='{}', curso='{}', jornada='{}', cursos='{}',
        WHERE Id={}'''.format(nombre, curso, jornada, cursos, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

