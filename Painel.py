import customtkinter as ctk

class Painel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Painel de Controle")
        self.geometry("400x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.main_frame = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="transparent" )
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.titulo = ctk.CTkLabel(self.main_frame, text="Bem-vindo ao Painel de Controle", font=ctk.CTkFont(size=20, weight="bold"))
        self.titulo.pack(pady=20)

if __name__ == "__main__":
    app = Painel()
    app.mainloop()