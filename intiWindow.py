#LIBRARIES
#WAS USED FOR TESTING CODE,NOT PART OF MAIN PROGRAM
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont


#Creating GUI Window.
root = Tk()
root.title("Say Cheese!")
root.geometry("1920x1080")

#LABELS
welcomeLbl = Label(root, text="Say Cheese!")
welcomeLbl.pack(side="top")
welcomeLbl.config(width=45)
welcomeLbl.config(font=("Courier", 44))

#DESCRIPTION
logo = tk.PhotoImage(file="smalllogo.png")

w1 = tk.Label(root, image=logo).pack(side="bottom")


explanation = """Welcome to "Say Cheese"!

To take a picture:
Specify how much time you would like to get into position, then simply press “Im ready”. When the timer completes, "Say Cheese!" will take a series of photos over a 3 second interval, try to smile and keep your eyes open during this time. Once complete, your best image will be shown, and you can choose to keep it, or try it again. Enjoy!"""

w2 = tk.Label(root, justify=tk.LEFT,padx = 50, text=explanation, font=("Courier", 12),wraplength=1000).pack(side="left")

funcBtn = Button(root,text="Take Picture", padx=40,pady=40).pack(side="bottom")

imageFrame = tk.Frame(root, width=600, height=500).pack()

#LAUNCH GUI
root.mainloop()
