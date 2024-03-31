from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from dominio.TendenciasTuristas import TendenciasGrafico


class InterfazGrafico:
    def __init__(self, parent):
        self.root = parent
        self.input_frame = Frame(self.root)
        self.input_frame.pack(pady=20, fill='x', expand=False)

        self.input_frame.grid_columnconfigure(1, weight=1)
        self.input_frame.grid_columnconfigure(3, weight=1)

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

        nombres_simplificados = list(self.comunidades.keys())

        Label(self.input_frame, text="Comunidad:").grid(row=0, column=0, sticky='ew')
        self.comunidad_combo = Combobox(self.input_frame, values=nombres_simplificados, width=30)
        self.comunidad_combo.grid(row=0, column=1, sticky='ew', padx=5)
        self.comunidad_combo.set(nombres_simplificados[0])

        años = list(range(2018, 2023))
        Label(self.input_frame, text="Año Inicio:").grid(row=0, column=2, sticky='ew')
        self.anio_inicio_combo = Combobox(self.input_frame, values=años, width=20)
        self.anio_inicio_combo.grid(row=0, column=3, sticky='ew', padx=5)
        self.anio_inicio_combo.set(años[-1])

        Label(self.input_frame, text="Año Fin:").grid(row=0, column=4, sticky='ew')
        self.anio_fin_combo = Combobox(self.input_frame, values=años, width=20)
        self.anio_fin_combo.grid(row=0, column=5, sticky='ew', padx=5)
        self.anio_fin_combo.set(años[-1])

        # Asegúrate de no usar pack aquí ya que estamos usando grid en el input_frame
        submit_btn = Button(self.input_frame, text="Consultar", command=self.on_submit)
        submit_btn.grid(row=0, column=6, sticky='ew', padx=17)

        # Frame para la gráfica
        self.plot_frame = Frame(self.root)
        self.plot_frame.pack(fill=BOTH, expand=True)

        self.tendencias_grafico = TendenciasGrafico()

    def on_submit(self):
        comunidad_simplificada = self.comunidad_combo.get()
        comunidad = self.comunidades[comunidad_simplificada]
        
        anio_inicio = self.anio_inicio_combo.get()
        anio_fin = self.anio_fin_combo.get()
        if anio_fin < anio_inicio:
            # Limpiar el contenido del frame de la gráfica
            for widget in self.plot_frame.winfo_children():
                widget.destroy()
                
            messagebox.showerror("Error", "El año final no puede ser menor que el año inicial.")
            return
        
        data = self.tendencias_grafico.fetch_data(comunidad, anio_inicio, anio_fin)
        self.tendencias_grafico.plot_data(self.plot_frame, data, anio_inicio, anio_fin)

def main():
    root = Tk()
    app = InterfazGrafico(root)
    root.mainloop()

if __name__ == "__main__":
    main()