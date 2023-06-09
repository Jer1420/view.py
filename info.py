import webbrowser
import ttkbootstrap as ttk


class About(ttk.Toplevel):
    def __init__(self):
        super().__init__(resizable=(False, False))
        self.title("")
        self.iconbitmap("images/Logo.ico")
        self.geometry("220x155")
        self.lb1 = ttk.Frame(self)
        self.lb2 = ttk.Frame(self)
        self.bouton = ttk.Frame(self)

        # Create button ok
        self.ok = ttk.Button(
            self.bouton,
            command=self.destroy,
            text="Ok",
            style="warning-outline",
            width=10,
        )

        lb_pseudo = ttk.Label(
            self.lb1, text="Créé par Jeremy".center(40, " "), style="warning"
        )
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=5, padx=10)
        self.lb1.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        lb_pseudo = ttk.Label(
            self.lb2, text="https://github.com/Jer1420".center(32, " "), style="warning"
        )
        lb_pseudo.bind("<Button-1>", self.do_open_url)
        lb_pseudo.grid(column=0, row=0, sticky=ttk.N, pady=5, padx=10)
        self.lb2.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)

        self.ok.grid(column=1, row=0, sticky=ttk.N, pady=20, padx=10)
        self.bouton.pack(expand=False, fill=ttk.X, side=ttk.TOP, anchor=ttk.N)
        lb_vide = ttk.Label(self.bouton, text="      ")
        lb_vide.grid(column=0, row=0, sticky=ttk.N, pady=10, padx=10)
        self.position_center()

    # Open the webpage
    def do_open_url(self, event):
        webbrowser.open("https://github.com/Jer1420")
