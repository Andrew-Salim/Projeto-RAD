import customtkinter as ctk

class Painel(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Consultor de CNPJ")
        self.geometry("700x500")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, width=180, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.main_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.titulo = ctk.CTkLabel(
            self.main_frame,
            text="Consultor de CNPJ",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.titulo.pack(anchor="w", pady=(0, 20))

        # campo de busca
        frame_busca = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        frame_busca.pack(fill="x", pady=(0, 15))

        self.entry_cnpj = ctk.CTkEntry(
            frame_busca,
            placeholder_text="Digite o CNPJ — ex: 00.000.000/0001-00",
            width=350
        )
        self.entry_cnpj.pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            frame_busca,
            text="Consultar",
            width=100,
            command=self.consultar_cnpj
        ).pack(side="left")

    def consultar_cnpj(self):
        cnpj = self.entry_cnpj.get()
        print(f"CNPJ digitado: {cnpj}")

if __name__ == "__main__":
    app = Painel()
    app.mainloop()