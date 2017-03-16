import ttk
import Tkinter

root = Tkinter.Tk()

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ffab00")

btn = ttk.Button(text="Sample")
btn.pack()

style = ttk.Style()
style.configure("TLabel", padding=6, relief="flat",
    background="#CF3A24")

lb = ttk.Label(text="This is a test. I hope it works!")
lb.pack()


root.mainloop()
