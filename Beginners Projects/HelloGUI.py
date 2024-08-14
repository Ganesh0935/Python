import tkinter as tk

def say_hello():
    label.config(text="Hello,World!")

#create the main window
root = tk.Tk()
root.title("Hello World GUI")

#create a label widget
label = tk.Label(root, text="")
label.pack(pady=20)

#create a button widget
button = tk.Button(root, text="Say Hello",command = say_hello)
button.pack()

#Run the main event loop
root.mainloop()