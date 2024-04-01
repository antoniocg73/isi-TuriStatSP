from dominio.login import Login
from dominio.ranking import Ranking
from dominio.seleccion import Seleccion
from presentacion.InterfazGrafico import InterfazGrafico
from tkinter import *
from tkinter import PhotoImage, messagebox
from tkinter.ttk import Combobox
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
        self.valor_seleccion = IntVar(value=0) 

        # Lista de comunidades
        self.comunidades = {
            'Andalucia': '01 Andalucía',
            'Aragon': '02 Aragón',
            'Asturias': '03 Asturias, Principado de',
            'Baleares': '04 Balears, Illes',
            'Canarias': '05 Canarias',
            'Cantabria': '06 Cantabria',
            'Castilla y Leon': '07 Castilla y León',
            'Castilla-La Mancha': '08 Castilla - La Mancha',
            'Cataluna': '09 Cataluña',
            'Comunidad Valenciana': '10 Comunitat Valenciana',
            'Extremadura': '11 Extremadura',
            'Galicia': '12 Galicia',
            'Madrid': '13 Madrid, Comunidad de',
            'Murcia': '14 Murcia, Región de',
            'Navarra': '15 Navarra, Comunidad Foral de',
            'Pais Vasco': '16 País Vasco',
            'La Rioja': '17 Rioja, La',
            'Ceuta': '18 Ceuta',
            'Melilla': '19 Melilla',
        }
        self.comunidades_inverso = {valor: clave for clave, valor in self.comunidades.items()}


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
        self.lblInicioImagen.place(x=430, y=440, anchor=CENTER) 
        
        #Definición frame Login
        self.frameTarea1Login = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea1Login.place(x=200,y=0)

        self.loginLogoImagen = PhotoImage(file=self.imagenLogo)
        self.lblLoginLogoImagen = Label(self.frameTarea1Login, image=self.loginLogoImagen)
        self.lblLoginLogoImagen.config(width=300, height=300, bg = '#81C2AE')
        self.lblLoginLogoImagen.place(x=410, y=150, anchor=CENTER)

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
        self.frameTuristas = Frame(self.frameTarea3Seleccion, bg = '#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameTuristas.place(x=15, y=70, width=450, height=300)
        self.frameTuristasSegundaSeccion = Frame(self.frameTarea3Seleccion, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        # Frame para mostrar resultados de comunidades
        self.frameResultadosComunidades = Frame(self.frameTarea3Seleccion, bg='#81C2AE', highlightbackground="white", highlightcolor="white", highlightthickness=2)
        self.frameResultadosComunidades.place(x=470, y=70, width=320, height=650)



        #labels del Selección primera sección
        self.lblNumeroTuristas = Label(self.frameTarea3Seleccion, text="Número de Turistas", font=("Comic Sans",16), fg="white", background="#81C2AE")
        self.lblNumeroTuristas.place(x=50 ,y=100)
        self.lblComunidadTuristas = Label(self.frameTarea3Seleccion, text="Comunidad", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblComunidadTuristas.place(x=50 ,y=150)
        self.lblPeriodoTuristas = Label(self.frameTarea3Seleccion, text="Periodo", font=("Comic Sans",14), fg="white", background="#81C2AE")       
        self.lblPeriodoTuristas.place(x=50 ,y=200)
        self.lblTuristas = Label(self.frameTarea3Seleccion, text="Turistas", font=("Comic Sans",14), fg="white", background="#81C2AE")       
        self.lblTuristas.place(x=50 ,y=250)

        #labels del Selección segunda sección
        self.frameTuristasSegundaSeccion.place(x=15, y=420, width=450, height=300)
        self.lblComunidades = Label(self.frameTuristasSegundaSeccion, text="Comunidades", font=("Comic Sans",16), fg="white", background="#81C2AE")
        self.lblComunidades.place(x=20 ,y=30)
        self.lblTuristasNumero = Label(self.frameTuristasSegundaSeccion, text="Turistas", font=("Comic Sans",14), fg="white", background="#81C2AE")
        self.lblTuristasNumero.place(x=20 ,y=80)
        self.lblAnoTuristas = Label(self.frameTuristasSegundaSeccion, text="Año", font=("Comic Sans",14), fg="white", background="#81C2AE")       
        self.lblAnoTuristas.place(x=20 ,y=130)
        self.lblEscoger = Label(self.frameTuristasSegundaSeccion, text="Escoger", font=("Comic Sans",14), fg="white", background="#81C2AE")       
        self.lblEscoger.place(x=20 ,y=180)

        # Label para el título de los resultados
        self.lblResultadosTitulo = Label(self.frameResultadosComunidades, text="Resultados", font=("Comic Sans", 16), fg="white", background="#81C2AE")
        self.lblResultadosTitulo.place(x=50, y=10)

        #combo box del Selección primera seccion
        comunidades = ['Andalucia','Aragon','Asturias','Baleares','Canarias','Cantabria','Castilla y Leon','Castilla-La Mancha',
        'Cataluna','Comunidad Valenciana','Extremadura','Galicia','Madrid','Murcia','Navarra','Pais Vasco','La Rioja','Ceuta','Melilla']
        self.comunidad_combo = Combobox(self.frameTarea3Seleccion, values=comunidades, width=30, state="readonly")
        self.comunidad_combo.place(x=200 ,y=150)
        ano = ['2018','2019','2020','2021','2022']
        self.periodo_combo = Combobox(self.frameTarea3Seleccion, values=ano, width=30, state="readonly")
        self.periodo_combo.place(x=200 ,y=200)

        #combo box del Selección segunda seccion
        turistas = ['10.000', '50.000', '100.000', '200.000', '500.000', '1.000.000', '2.500.000', '5.000.000', '8.000.000']
        self.turistas_combo = Combobox(self.frameTuristasSegundaSeccion, values=turistas, width=30, state="readonly")
        self.turistas_combo.place(x=170 ,y=80)
        ano = ['2018','2019','2020','2021','2022']
        self.anioTuristas_combo = Combobox(self.frameTuristasSegundaSeccion, values=ano, width=30, state="readonly")
        self.anioTuristas_combo.place(x=170 ,y=130)

        #Radiobuttons para escoger Más o Menos
        self.radio_mas = Radiobutton(self.frameTuristasSegundaSeccion, text="Más", value=1, variable=self.valor_seleccion, bg='#81C2AE')
        self.radio_mas.place(x=170, y=180)
        self.radio_menos = Radiobutton(self.frameTuristasSegundaSeccion, text="Menos", value=2, variable=self.valor_seleccion, bg='#81C2AE')
        self.radio_menos.place(x=270, y=180)

        #texto del Selección
        self.txtComunidadesTuristas = Text(self.frameTarea3Seleccion, width=25, height=1)
        self.txtComunidadesTuristas.place(x=200 ,y=250)
        
        #boton del Selección primera seccion
        self.botonSeleccionTuristas = Button(self.frameTarea3Seleccion, text="Obtener turistas", fg="black", width=30, command=self.mostrar_turistas)
        self.botonSeleccionTuristas.place(x=200 ,y=300)

        #boton del Selección segunda seccion
        self.botonComunidadesTuristas = Button(self.frameTuristasSegundaSeccion, text="Buscar", fg="black", width=30, command=self.buscar_comunidades)
        self.botonComunidadesTuristas.place(x=170 ,y=230)

        # Listbox para mostrar las comunidades
        self.listboxComunidades = Listbox(self.frameResultadosComunidades, fg="black", bg="white", width=45, height=30)
        self.listboxComunidades.place(x=20, y=50)










        #Definición frame Gráfico
        self.frameTarea4Grafico = Frame(height=920, width=900, bg = '#81C2AE')
        self.frameTarea4Grafico.place(x=200,y=0)

        self.initMenuInicio() 

        # Ejecutar la aplicación
        self.ventana.mainloop()

    def initMenuInicio(self):
        self.limpiarCampos()
        self.frameInicio.place(x=200,y=0)
        self.frameTarea1Login.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

    def initMenuLogin(self):
        self.limpiarCampos()
        self.frameInicio.place_forget()
        self.frameTarea1Login.place(x=200,y=0)
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

    def initMenuRanking(self):
        self.limpiarCampos()
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place(x=200,y=0)
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place_forget()

    def initMenuSeleccion(self):
        self.limpiarCampos()
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place(x=200,y=0)
        self.frameTarea4Grafico.place_forget()
    
    def initMenuGrafico(self):
        self.limpiarCampos()
        self.frameTarea1Login.place_forget()
        self.frameInicio.place_forget()
        self.frameTarea2Ranking.place_forget()
        self.frameTarea3Seleccion.place_forget()
        self.frameTarea4Grafico.place(x=200,y=0)
        if not hasattr(self, 'grafico_app'):
            self.grafico_app = InterfazGrafico(self.frameTarea4Grafico)
        else:
            self.grafico_app.root.lift()

    def limpiarCampos(self):
        self.txtLogin.delete(0, END)
        self.txtContrasena.delete(0, END)
        self.txtComunidadesTuristas.config(state='normal')
        self.txtComunidadesTuristas.delete(1.0, END)
        self.txtComunidadesTuristas.config(state='disabled')
        self.listboxComunidades.delete(0, END)
        self.txtMasVisitado.delete(1.0, END)
        self.txtMenosVisitado.delete(1.0, END)
        self.turistas_combo.set('')
        self.anioTuristas_combo.set('')
        self.comunidad_combo.set('')
        self.periodo_combo.set('')
        self.valor_seleccion.set(0)
        self.radio_mas.deselect()
        self.radio_menos.deselect()

    def abrirMapa(self):
        # Ruta al archivo HTML del mapa
        ruta_html = 'presentacion\gestionMapa\mapa.html'
        self.limpiarCampos()
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

    # Función para actualizar el listbox con los resultados de la base de datos
    def actualizar_listbox_comunidades(self, resultados):
        # Limpia el listbox antes de añadir nuevos resultados
        self.listboxComunidades.delete(0, END)
        # Convierte la lista de resultados en un conjunto para eliminar duplicados
        comunidades_unicas = set([comunidad[0] for comunidad in resultados])
        # Eliminar espacio en blanco vacío y ordenar alfabéticamente las comunidades
        comunidades_unicas = sorted([comunidad.strip() for comunidad in comunidades_unicas if comunidad.strip()])
        # Añade las comunidades únicas al listbox
        for abreviatura in comunidades_unicas:
            nombre_completo = self.comunidades_inverso.get(abreviatura, abreviatura)
            self.listboxComunidades.insert(END, nombre_completo)

    def mostrar_turistas(self):

        # Verificar si se ha seleccionado una comunidad y un año
        if not self.comunidad_combo.get() or not self.periodo_combo.get():
            messagebox.showwarning("Advertencia", "Por favor, selecciona una comunidad y un año.")
            return
        
        self.txtComunidadesTuristas.config(state='normal')
        self.txtComunidadesTuristas.delete(1.0, END) # Limpia el widget de texto
        valor_comunidad = self.comunidad_combo.get()
        print(valor_comunidad)
        valor_periodo = self.periodo_combo.get()
        print(valor_periodo)
        seleccion = Seleccion()
        turistas = seleccion.mostrar_numero_turistas(self.comunidades.get(valor_comunidad), valor_periodo)  # Asume que este método devuelve una lista de comunidades
        self.txtComunidadesTuristas.insert(END, turistas[0][1])  # Inserta cada comunidad al final del widget de texto
        self.txtComunidadesTuristas.config(state='disabled')

    def buscar_comunidades(self):
    # Verificar si se ha seleccionado un número de turistas y un año
        if not self.turistas_combo.get() or not self.anioTuristas_combo.get():
            messagebox.showwarning("Advertencia", "Por favor, selecciona un número de turistas y un año.")
            return

        # Obtiene los valores seleccionados por el usuario
        turistas_combo = self.turistas_combo.get().replace('.', '')  # Asumiendo que necesitas remover puntos
        anioTuristas_combo = self.anioTuristas_combo.get()

        mas_o_menos = self.valor_seleccion.get()  # Obtiene 1 o 2, dependiendo de la selección del usuario

        # Verifica que mas_o_menos tenga un valor válido (1 o 2)
        if mas_o_menos not in [1, 2]:
            messagebox.showerror("Error", "Seleccione 'Más' o 'Menos' para proceder.")
            return

        # Instancia la clase de selección y llama al método para obtener los datos
        seleccion = Seleccion()
        resultados = seleccion.mostrar_comunidades(anioTuristas_combo, int(turistas_combo), mas_o_menos)
        print(resultados)

        # Actualiza la listbox con los nombres de las comunidades obtenidas de la consulta
        self.actualizar_listbox_comunidades(resultados)



