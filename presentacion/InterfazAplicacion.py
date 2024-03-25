from dominio.login import Login
from dominio.ranking import Ranking
from presentacion.InterfazGrafico import InterfazGrafico
from tkinter import *
from tkinter import PhotoImage, messagebox
import webbrowser
import re


class InterfazAplicacion:
    # Imágenes
    imagenLogo = "archivosExternos/LogoISINoFondo.png"
    imagenUsuario = "archivosExternos/usuarioLogin.png"
    imagenContrasena = "archivosExternos/contrasenaLogin.png"

    def __init__(self):

        #Configuración de la ventana
        self.ventana = Tk()
        self.ventana.title("Gestión de TuriStatSP")
        self.ventana.geometry("1000x1000")
        self.ventana.resizable(False, False)

        #menu frame
        self.frameMenu = Frame(height=800, width=200, bg='#18171c')
        self.frameMenu.place(x=0, y=0)

        #menu botones
        self.botonInicio = Button(self.frameMenu, height=3, width=30, text ='HOME', bg='#708090', command=self.initMenuInicio)
        self.botonInicio.place(x=-10, y=50)  
        self.botonTarea1Login = Button(self.frameMenu, height=3, width=30, text ='INICIAR SESIÓN', bg='#708090', command=self.initMenuLogin)
        self.botonTarea1Login.place(x=-10, y=105) 
        self.botonTarea2Ranking = Button(self.frameMenu, height=3, width=30, text ='RANKING', bg='#708090', command=self.initMenuRanking)
        self.botonTarea2Ranking.place(x=-10, y=160)
        self.botonTarea2Ranking.config(state=DISABLED)
        self.botonTarea3Seleccion = Button(self.frameMenu, height=3, width=30, text ='SELECCIÓN DE DATOS', bg='#708090', command=self.initMenuSeleccion)
        self.botonTarea3Seleccion.place(x=-10, y=215)
        self.botonTarea3Seleccion.config(state=DISABLED)
        self.botonTarea4Grafico = Button(self.frameMenu, height=3, width=30, text ='GRÁFICO TENDENCIAS', bg='#708090', command=self.initMenuGrafico)
        self.botonTarea4Grafico.place(x=-10, y=270)
        self.botonTarea4Grafico.config(state=DISABLED)
        self.botonMapa = Button(self.frameMenu, height=3, width=30, text ='MAPA DE ESPAÑA', bg='#708090', command=self.abrirMapa)
        self.botonMapa.place(x=-10, y=325)
        self.botonMapa.config(state=DISABLED)

        # Definición frame Inicio
        self.frameInicio = Frame(height=920, width=900, bg = '#317874')
        self.frameInicio.place(x=200,y=0)
        self.InicioText1 = Label(self.frameInicio, height=2,width=50,text='INTEGRACIÓN DE SISTEMAS DE LA INFORMACIÓN', bg='#317874', fg='#FFFFFF', font=100)
        self.InicioText1.place(x=150 ,y=180)
        self.InicioText2 = Label(self.frameInicio, height=2,width=50,text='Aplicación', bg='#317874', fg='#FFFFFF', font=100)
        self.InicioText2.place(x=150 ,y=220)
        self.InicioText3 = Label(self.frameInicio, height=2,width=50,text='TuriStatSP', bg='#317874', fg='#FFFFFF', font=100)
        self.InicioText3.place(x=150 ,y=600)
        self.InicioImagen = PhotoImage(file=self.imagenLogo)  
        self.lblInicioImagen = Label(self.frameInicio, image=self.InicioImagen)
        self.lblInicioImagen.config(width=300, height=300, bg = '#317874')
        self.lblInicioImagen.place(x=420, y=440, anchor=CENTER) 
        
        #Definición frame Login
        self.frameTarea1Login = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea1Login.place(x=200,y=0)

        self.loginLogoImagen = PhotoImage(file=self.imagenLogo)
        self.lblLoginLogoImagen = Label(self.frameTarea1Login, image=self.loginLogoImagen)
        self.lblLoginLogoImagen.config(width=300, height=300, bg = '#81C2AE')
        self.lblLoginLogoImagen.place(x=420, y=150, anchor=CENTER)

        self.loginUsuarioImagen = PhotoImage(file=self.imagenUsuario)
        self.lblLoginUsuarioImagen = Label(self.frameTarea1Login, image=self.loginUsuarioImagen)
        self.lblLoginUsuarioImagen.config(width=100, height=00, bg = '#81C2AE')
        self.lblLoginUsuarioImagen.place(x=200, y=362, anchor=CENTER)

        self.loginContrasenaImagen = PhotoImage(file=self.imagenContrasena)
        self.lblLoginContrasenaImagen = Label(self.frameTarea1Login, image=self.loginContrasenaImagen)
        self.lblLoginContrasenaImagen.config(width=100, height=00, bg = '#81C2AE')
        self.lblLoginContrasenaImagen.place(x=200, y=512, anchor=CENTER)

        #botones del login
        self.botonRegistro = Button(self.frameTarea1Login,text="Registrarse",fg="black", width=20, command=self.registrar_usuario)
        self.botonRegistro.place(x=230 ,y=650)        
        self.botonAutenticarse = Button(self.frameTarea1Login, text="Autenticarse", fg="black", width=20, command=self.verificar_credenciales)
        self.botonAutenticarse.place(x=450 ,y=650)
        
        #labels del login
        self.lblUsuario = Label(self.frameTarea1Login, text="Usuario", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblUsuario.place(x=230 ,y=300)
        self.lblContrasena = Label(self.frameTarea1Login, text="Contraseña", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblContrasena.place(x=230 ,y=450)

        #Texto del login
        self.txtLogin=Entry(self.frameTarea1Login, justify=LEFT, width=33, font=('Comic Sans', 14))
        self.txtLogin.place(x=230 ,y=350)
        self.txtContrasena=Entry(self.frameTarea1Login, justify=LEFT, width=33, font=('Comic Sans', 14), show="*")
        self.txtContrasena.place(x=230 ,y=500)






        #Definición frame Ranking
        self.frameTarea2Ranking = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea2Ranking.place(x=200,y=0)
        
        #labels del Ranking
        self.lblMasVisitado = Label(self.frameTarea2Ranking, text="Comunidades más visitadas", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblMasVisitado.place(x=50 ,y=250)
        self.lblMenosVisitado = Label(self.frameTarea2Ranking, text="Comunidades menos visitadas", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblMenosVisitado.place(x=420 ,y=250)

        #Textos del ranking
        self.txtMasVisitado = Text(self.frameTarea2Ranking, width=40, height=20)
        self.txtMasVisitado.place(x=50 ,y=300)
        self.txtMenosVisitado = Text(self.frameTarea2Ranking, width=40, height=20)
        self.txtMenosVisitado.place(x=420 ,y=300)
        # Llamada al método
        self.mostrar_comunidades_mas_visitadas()
        self.mostrar_comunidades_menos_visitadas()



        #Definición frame Selección
        self.frameTarea3Seleccion = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea3Seleccion.place(x=200,y=0)

        #Definición frame Gráfico
        self.frameTarea4Grafico = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea4Grafico.place(x=200,y=0)

        self.initMenuInicio() 

        # Ejecutar la aplicación
        self.ventana.mainloop()

    def initMenuInicio(self):
        self.frameInicio.place(x=200,y=0)
        self.frameTarea1Login.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

    def initMenuLogin(self):
        self.frameInicio.place_forget()
        self.frameTarea1Login.place(x=200,y=0)
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

        '''
        # Definición de elementos del frame Login
        self.LoginText1 = Label(self.frameTarea1Login, height=2,width=50,text='INICIAR SESIÓN', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText1.place(x=150 ,y=180)
        self.LoginText2 = Label(self.frameTarea1Login, height=2,width=50,text='Ingrese sus credenciales', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText2.place(x=150 ,y=220)
        self.LoginText3 = Label(self.frameTarea1Login, height=2,width=50,text='Usuario:', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText3.place(x=150 ,y=260)
        self.LoginText4 = Label(self.frameTarea1Login, height=2,width=50,text='Contraseña:', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText4.place(x=150 ,y=300)
        self.LoginText5 = Label(self.frameTarea1Login, height=2,width=50,text='¿No tienes cuenta?', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText5.place(x=150 ,y=340)
        self.LoginText6 = Label(self.frameTarea1Login, height=2,width=50,text='Regístrate', bg='#81C2AE', fg='#FFFFFF', font=100)
        self.LoginText6.place(x=150 ,y=380)

        self.entryUsuario = Entry(self.frameTarea1Login, width=30)
        self.entryUsuario.place(x=300, y=270)
        self.entryContrasena = Entry(self.frameTarea1Login, width=30, show='*')
        self.entryContrasena.place(x=300, y=310)
        self.botonIniciarSesion = Button(self.frameTarea1Login, height=2, width=30, text ='INICIO SESIÓN', bg='#708090', command=self.verificar_credenciales)
        '''
    def initMenuRanking(self):
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place(x=200,y=0)
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

    def initMenuSeleccion(self):
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place(x=200,y=0)
        self.frameTarea4Grafico.place_forget()
    
    def initMenuGrafico(self):
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place(x=200,y=0)
        if not hasattr(self, 'grafico_app'):
            self.grafico_app = InterfazGrafico(self.frameTarea4Grafico)
        else:
            self.grafico_app.root.lift()

    def abrirMapa(self):
        # Ruta al archivo HTML del mapa
        ruta_html = 'presentacion\gestionMapa\mapa.html'
        # Abrir el archivo HTML en el navegador predeterminado
        webbrowser.open(ruta_html)

    def registrar_usuario(self):
        usuario = self.txtLogin.get()
        contrasena = self.txtContrasena.get()
        if len(contrasena) < 4:
            messagebox.showerror("Contraseña inválida", "La contraseña debe tener al menos 4 caracteres.")
            self.txtContrasena.delete(0, END)  # Limpiar el campo de contraseña
            return
        login = Login()
        if login.registrar_usuario(usuario, contrasena):
            messagebox.showinfo("Registro exitoso", "¡Registro exitoso!")
        else:
            self.txtContrasena.delete(0, END)
            self.txtLogin.delete(0, END)
            messagebox.showerror("Registro fallido", "¡Registro fallido!")

    def verificar_credenciales(self):
        usuario = self.txtLogin.get()
        contrasena = self.txtContrasena.get()
        login = Login()
        if login.verificar_usuario(usuario, contrasena):
            messagebox.showinfo("Autenticación exitosa", "¡Autenticación exitosa!")
            self.botonTarea2Ranking.config(state=NORMAL)
            self.botonTarea3Seleccion.config(state=NORMAL)
            self.botonTarea4Grafico.config(state=NORMAL)
            self.botonMapa.config(state=NORMAL)
            self.botonTarea1Login.config(state=DISABLED)
            self.initMenuInicio()
        else:
            messagebox.showerror("Autenticación fallida", "¡Autenticación fallida!")
            # Limpiar el contenido del campo de contraseña si la autenticación falla
            self.txtContrasena.delete(0, END)

    def mostrar_comunidades_mas_visitadas(self):
        ranking = Ranking()
        comunidades = ranking.mostrar_comunidades_mas_visitadas()  # Asume que este método devuelve una lista de comunidades
        for comunidad in comunidades:
            self.txtMasVisitado.insert(END, comunidad +'\n')  # Inserta cada comunidad al final del widget de texto
        self.txtMasVisitado.config(state='disabled')

    def mostrar_comunidades_menos_visitadas(self):
        ranking = Ranking()
        comunidades = ranking.mostrar_comunidades_menos_visitadas()  # Asume que este método devuelve una lista de comunidades
        for comunidad in comunidades:
            self.txtMenosVisitado.insert(END, comunidad+'\n')  # Inserta cada comunidad al final del widget de texto
        self.txtMenosVisitado.config(state='disabled')




