import tkinter as tk

class VentanaTkinter(tk.Tk):  # Heredamos solo de tk.Tk
    def __init__(self):  # El método __init__ debe estar bien escrito
        super().__init__()
        self.title("Aplicación con Tkinter")
        self.geometry("400x400")
        

        tk.Label(self, text="¡Bienvenido a Tkinter!", font=("Arial", 14)).pack(pady=50)
        
        frame_text = tk.Frame(self)
        frame_text.pack(pady=50)

        tk.Button(frame_text, text="Cancelar", command=self.quit).pack(side="left", padx=50)
        tk.Button(frame_text, text="Aceptar", command=self.quit).pack(side="left", padx=10)

if __name__ == "__main__":
    app = VentanaTkinter()
    app.mainloop()
