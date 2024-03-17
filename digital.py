import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

root = tk.Tk()
root.title("Simple GUI Clock")

label = tk.Label(root, font=('Helvetica', 48))
label.pack(padx=20, pady=20)

update_time()

root.mainloop()
