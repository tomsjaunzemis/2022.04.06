import tkinter as tk
import tkinter.ttk as ttk
 
class Window:
    def __init__(self, master):
        self.master = master
 
        style = ttk.Style()
        style.theme_settings("default", {
           "TButton": {
               "configure": {"padding": 10},
               "map": {
                   "background": [("active", "yellow3"),
                                  ("!disabled", "yellow")],
                   "foreground": [("focus", "Red"),
                                  ("active", "green"),
                                  ("!disabled", "Blue")]
               }
           }
        })
 
        style.theme_use("default")
 
        button = ttk.Button(master, text = "Nospied mani")
        button.pack(padx = 5, pady = 5)

        label = ttk.Label(master, text = "label")
        label.pack(padx = 5, pady = 5)
 
root = tk.Tk()
window = Window(root)
root.mainloop()