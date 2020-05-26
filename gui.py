import tkinter as tk
from MoveFile import move_images
from tkinter import filedialog
import os

def move(originalDirectory,endDirectory,width,height):
    if not(os.path.isdir(str(originalDirectory[:-1])) and os.path.isdir(str(endDirectory[:-1]))):
        errorMsg.set('One of the listed Directories does not exist')
        return
    if(originalDirectory == endDirectory):
        errorMsg.set('Why are you trying to move pictures to the same directory?')
        return
    try:
        w = int(width)
        h = int(height)
        if(w < 0 or h < 0):
            errorMsg.set('Please enter positive integers for the max dimension')
            return
    except:
        w = 0
        h = 0
        errorMsg.set('Please enter positive integers for the max dimension')
    if not(w==0 or h==0):
        error.destroy()
        move_images(originalDirectory[:-1],endDirectory[:-1],w,h)

# Inserts selected directory into the directory text box
def directory(e):
    e.delete(1.0,tk.END)
    e.insert(tk.END,filedialog.askdirectory())

# Setup window
main = tk.Tk()
main.title('Image Relocator')
main.geometry("600x400")
main.resizable(0,0)

# Original and End Directory Text
origDir = tk.Text(main,width=60,height=1)
endDir = tk.Text(main,width=60,height=1)

# Pic size
picHeight = tk.Text(main,width=20,height=1)
picWidth = tk.Text(main,width=20,height=1)

# Labels
orDir = tk.Label(main, text='Source Directory')
enDir = tk.Label(main, text='Target Directory')
height = tk.Label(main, text='Height')
width = tk.Label(main, text='Width')
Descrip = tk.Label(main, text='Maximum Image Dimension:')
global errorMsg
errorMsg = tk.StringVar()
error = tk.Label(main, textvariable = errorMsg, fg='red')

# Buttons
browse1 = tk.Button(main, text='Browse', bg='#a6a3a0',
                    command=lambda:directory(origDir))
browse2 = tk.Button(main, text='Browse', bg='#a6a3a0',
                    command=lambda:directory(endDir))
stop = tk.Button(main, text='Quit', bg='#a6a3a0', width=10,
                    command=lambda: main.destroy())
start = tk.Button(main, text='Start', bg='#a6a3a0', width=10,
                    command=lambda:move(origDir.get(1.0,tk.END),
                                        endDir.get(1.0,tk.END),
                                        picWidth.get(1.0,tk.END),
                                        picHeight.get(1.0,tk.END)))

# Placements in window
orDir.place(x=10,y=24)
enDir.place(x=10,y=109)
origDir.pack(fill=tk.X, padx=10, pady=45)
browse1.place(x=275,y=70)
endDir.pack(fill=tk.X, padx=10, pady=20)
browse2.place(x=275,y=155)
Descrip.pack(pady=49)
picWidth.place(x=110,y=240)
width.place(x=110,y=260)
picHeight.place(x=325,y=240)
height.place(x=325,y=260)
error.pack(pady=45)
start.place(x=500,y=360)
stop.place(x=400,y=360)

main.mainloop()
