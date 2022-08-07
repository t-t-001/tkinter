import tkinter as tk

root = tk.Tk()
root.geometry('300x150')
txt = tk.Entry(width=20)
txt.pack(pady=50)
print(root.children)
root.mainloop()