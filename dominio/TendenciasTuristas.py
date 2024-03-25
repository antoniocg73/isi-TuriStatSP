#Hay que instalar la librería matplotlib con el comando pip install matplotlib
import requests
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TendenciasGrafico:
    def fetch_data(self, comunidad, anio_inicio, anio_fin):
        """Obtiene los datos del servidor y devuelve una lista de tuplas."""
        url = f"http://127.0.0.1:5000/tendenciasComunidad?comunidad={comunidad}&anio_inicio={anio_inicio}&anio_fin={anio_fin}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Error al obtener los datos:", response.status_code)
            return []

    def plot_data(self, frame, data, anio_inicio, anio_fin):
        """Limpia el frame actual y genera una nueva gráfica con los datos obtenidos."""
        for widget in frame.winfo_children():
            widget.destroy()

        if data:
            fig = Figure(figsize=(8, 6), dpi=100)
            plot = fig.add_subplot(1, 1, 1)

            años = np.array([item[1] for item in data], dtype=np.float64)
            residentes_españa = np.array([item[2] for item in data], dtype=np.float64)
            residentes_extranjero = np.array([item[3] for item in data], dtype=np.float64)

            plot.plot(años, residentes_españa, 'bo-', label='Turistas españoles')
            plot.plot(años, residentes_extranjero, 'go-', label='Turistas extranjeros')

            if anio_inicio != anio_fin:
                años_proyección = np.linspace(int(anio_inicio), int(anio_fin) + 5, 100)

                coeficientes_españa = np.polyfit(años - int(anio_inicio), residentes_españa, 1)
                polinomio_españa = np.poly1d(coeficientes_españa)
                plot.plot(años_proyección, polinomio_españa(años_proyección - int(anio_inicio)), "b--", label='Tendencia españoles')

                coeficientes_extranjero = np.polyfit(años - int(anio_inicio), residentes_extranjero, 1)
                polinomio_extranjero = np.poly1d(coeficientes_extranjero)
                plot.plot(años_proyección, polinomio_extranjero(años_proyección - int(anio_inicio)), "g--", label='Tendencia extranjeros')
                plot.set_title('Tendencia de Turistas')
                plot.set_xlabel('Año')
                plot.set_ylabel('Número de Turistas')
                plot.legend()
                canvas = FigureCanvasTkAgg(fig, master=frame)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            else:
                messagebox.showwarning("Error", "El año de inicio y fin son el mismo. No se trazan líneas de tendencia.")
                canvas.clear()

            