import tkinter as tk

def end():
    quit()

def print_fun():
    print("hello")

window = tk.Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()

window.geometry('%dx%d+0+0' % (width,height))

print_button=quit_butt = tk.Button(master=window, text="print", command=print_fun,height= 4,width=8, bg="blue",
    fg="white",padx=100, pady=100)


quit_button = tk.Button(master=window, text="quit", command=end,height= 4,width=8, bg="red",
    fg="white",padx=100, pady=100)

print_button.grid(column=0, row=0)
quit_butt.grid(column=1, row=0)


window.mainloop()

print("Hello Jarob")
print("hello corey")