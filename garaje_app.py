
import tkinter as tk
from tkinter import messagebox

# =========================
# MODELO
# =========================
class Vehiculo:

    def __init__(self, placa, marca, propietario):
        self.placa = placa
        self.marca = marca
        self.propietario = propietario

    def __str__(self):
        return f"{self.placa} - {self.marca} - {self.propietario}"


# =========================
# SERVICIO
# =========================
class GarajeServicio:

    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def listar_vehiculos(self):
        return self.vehiculos


# =========================
# INTERFAZ GRAFICA
# =========================
class GarajeApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema Básico de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Título
        titulo = tk.Label(root, text="Registro de Vehículos del Garaje", font=("Arial", 14))
        titulo.grid(row=0, column=0, columnspan=2, pady=10)

        # Labels
        tk.Label(root, text="Placa").grid(row=1, column=0)
        tk.Label(root, text="Marca").grid(row=2, column=0)
        tk.Label(root, text="Propietario").grid(row=3, column=0)

        # Entradas
        self.placa_entry = tk.Entry(root)
        self.marca_entry = tk.Entry(root)
        self.propietario_entry = tk.Entry(root)

        self.placa_entry.grid(row=1, column=1)
        self.marca_entry.grid(row=2, column=1)
        self.propietario_entry.grid(row=3, column=1)

        # Botones
        btn_agregar = tk.Button(root, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=4, column=0, pady=10)

        btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_campos)
        btn_limpiar.grid(row=4, column=1)

        # Lista de vehículos
        self.lista = tk.Listbox(root, width=50)
        self.lista.grid(row=5, column=0, columnspan=2, pady=10)

    def agregar_vehiculo(self):

        placa = self.placa_entry.get()
        marca = self.marca_entry.get()
        propietario = self.propietario_entry.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, propietario)
        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_lista()
        self.limpiar_campos()

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for vehiculo in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, vehiculo)

    def limpiar_campos(self):

        self.placa_entry.delete(0, tk.END)
        self.marca_entry.delete(0, tk.END)
        self.propietario_entry.delete(0, tk.END)


# =========================
# MAIN
# =========================
def main():
    root = tk.Tk()
    app = GarajeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
