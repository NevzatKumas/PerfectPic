import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

window = tk.Tk()
window.wm_title("Perfect Pic")
window.config(background="#FFFFFF")

imageFrame = tk.Frame(window, width=600, height=500)
imageFrame.grid(row=0, column=0, padx=10, pady=2)


lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)
def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame) 

def capture_frames():
    counter = 0
    for i in range(20):
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        time.sleep(0.2)
        counter=counter+1
        cv2.imwrite("/Users/abedmiah/Documents/hackru-fall21/Images/temp_" + str(counter) + ".png", frame)

button1 = tk.Button(window, text="capture frames", command = capture_frames).grid(row=2, column=1)


sliderFrame = tk.Frame(window, width=600, height=100)
sliderFrame.grid(row = 600, column=0, padx=10, pady=2)

show_frame()
time.sleep(2)
window.mainloop()
