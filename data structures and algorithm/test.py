
def popup():
    import tkinter as tk

    
    root = tk.Tk()

    
    root.geometry("300x100")

    
    root.title("happy birthday")

    
    label = tk.Label(root, text="Happy birthday\n try closing me")

    
    label.pack(pady=20)

    
    root.mainloop()
while True:
    popup()


