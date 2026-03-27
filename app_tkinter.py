import tkinter as tk
from tkinter import messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")
        self.root.geometry("500x400")

        self.crear_widgets()
        self.cargar_tareas()

    def crear_widgets(self):
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        self.entry.bind("<Return>", self.agregar_tarea_evento)

        frame = tk.Frame(self.root)
        frame.pack()

        tk.Button(frame, text="Añadir Tarea", command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Marcar Completada", command=self.marcar_completada).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Eliminar", command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

        self.lista = tk.Listbox(self.root, width=60)
        self.lista.pack(pady=10)

        self.lista.bind("<Double-1>", self.marcar_completada_evento)

    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto:
            self.servicio.agregar_tarea(texto)
            self.entry.delete(0, tk.END)
            self.cargar_tareas()
        else:
            messagebox.showwarning("Aviso", "Ingrese una tarea")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def cargar_tareas(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            texto = f"[Hecho] {tarea.descripcion}" if tarea.completado else tarea.descripcion
            self.lista.insert(tk.END, texto)

            if tarea.completado:
                self.lista.itemconfig(tk.END, {'fg': 'gray'})

    def obtener_seleccion(self):
        seleccion = self.lista.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione una tarea")
            return None
        return seleccion[0]

    def marcar_completada(self):
        index = self.obtener_seleccion()
        if index is not None:
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.completar_tarea(tarea.id)
            self.cargar_tareas()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        index = self.obtener_seleccion()
        if index is not None:
            tarea = self.servicio.obtener_tareas()[index]
            self.servicio.eliminar_tarea(tarea.id)
            self.cargar_tareas()
