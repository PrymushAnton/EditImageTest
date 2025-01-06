import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        
        
        self.geometry(f"{800}x{600}")

app = App()