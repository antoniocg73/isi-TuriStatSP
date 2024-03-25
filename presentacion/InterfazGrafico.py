from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dominio.TendenciasResidentes import TendenciasGrafico


class InterfazGrafico:
    def __init__(self, parent):
        self.root = parent
        self.input_frame = Frame(self.root)
        self.input_frame.pack(pady=20)

        # Lista de comunidades
        comunidades = [
            "01 Andalucía",
            "02 Aragón",
            "03 Asturias, Principado de",
            "04 Balears, Illes",
            "05 Canarias",
            "06 Cantabria",
            "07 Castilla y León",
            "08 Castilla - La Mancha",
            "09 Cataluña",
            "10 Comunitat Valenciana",
            "11 Extremadura",
            "12 Galicia",
            "13 Madrid, Comunidad de",
            "14 Murcia, Región de",
            "15 Navarra, Comunidad Foral de",
            "16 País Vasco",
            "17 Rioja, La",
            "18 Ceuta",
            "19 Melilla"
        ]
        Label(self.input_frame, text="Comunidad:").pack(side=LEFT)
        self.comunidad_combo = ttk.Combobox(self.input_frame, values=comunidades)
        self.comunidad_combo.pack(side=LEFT)
        self.comunidad_combo.set(comunidades[0])

        años = list(range(2018, 2023))
        Label(self.input_frame, text="Año Inicio:").pack(side=LEFT)
        self.anio_inicio_combo = ttk.Combobox(self.input_frame, values=años)
        self.anio_inicio_combo.pack(side=LEFT)
        self.anio_inicio_combo.set(años[-1])

        Label(self.input_frame, text="Año Fin:").pack(side=LEFT)
        self.anio_fin_combo = ttk.Combobox(self.input_frame, values=años)
        self.anio_fin_combo.pack(side=LEFT)
        self.anio_fin_combo.set(años[-1])

        self.plot_frame = Frame(self.root)
        self.plot_frame.pack(fill=BOTH, expand=1)

        self.tendencias_grafico = TendenciasGrafico()

        submit_btn = Button(self.input_frame, text="Consultar", command=self.on_submit)
        submit_btn.pack(side=LEFT, padx=10)

    def on_submit(self):
        comunidad = self.comunidad_combo.get()
        anio_inicio = self.anio_inicio_combo.get()
        anio_fin = self.anio_fin_combo.get()
        if anio_fin < anio_inicio:
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