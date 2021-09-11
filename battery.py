from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import psutil
import time



root = Tk()
root.title("Battery Monitor")
root.geometry("300x150")
root.iconbitmap("battery.ico")


canvas = Canvas(root, bg="#212120")
canvas.place(relheight=0.5, relwidth=1, relx=0, rely=0)

canvas2 = Canvas(root)
canvas2.place(relheight=0.5, relwidth=1, relx=0, rely=0.5)

battery = psutil.sensors_battery()
bat = battery.percent



Label(canvas, text="Battery Monitor", bg="#212120", fg="white", font=("Arial", 20, 'bold')).pack(pady=10)

progress = ttk.Progressbar(canvas2, orient=HORIZONTAL, length=200, mode='determinate')




progress.pack(pady=10, padx=10)
x = Label(canvas2, font=("Arial", 15))
x.pack()



def bar():
        battery = psutil.sensors_battery()
        bat = battery.percent
        
        progress['value'] = bat
        root.update_idletasks()
        
        x.config(text=str(bat)+"%")
        
        if bat <=30:
            messagebox.showwarning("Battery Monitor", "Battery is Less than 30%! Charge Now!!!")
            time.sleep(5)
            
        if bat ==100:
            messagebox.showwarning("Battery Monitor", "Battery is fully Charged! Remove Charge Now!")
            time.sleep(5)
            

        root.after(10, bar)
        
bar()
root.mainloop()