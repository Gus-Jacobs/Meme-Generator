#==============================================================================
# Meme Generator
#
# Created by Gus Jacobs
#
# All Rights Reserved 2024
#
#
#==============================================================================


#============= IMPORTS =============

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from PIL import ImageTk, Image
from random import * 
import sys
import os
import time
import shutil

#============= PROGRAM =============


#====== VARIABLES ======

inFolder = "C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/memes"
files = os.listdir(inFolder)
finalFiles = []
used = []
current_index = -1
meme_number = 0

#====== INITIALIZING FUNCTION ======

def initializeMemes():
 global finalFiles
 finalFiles = []
 memeIndex = []
 while len(memeIndex) < 25:
  x = randrange(len(files))
  if x in memeIndex:
   continue
  else:
   memeIndex.append(x)
 tempFiles = []
 for y in memeIndex:
  tempFiles.append(files[y])
 finalFiles = tempFiles.copy()

initializeMemes()


#====== WINDOW ======

root = tk.Tk()
#root.resizable(width=False, height=False)
root.minsize(width=900, height=900)
x = root.winfo_screenwidth()
y = root.winfo_screenheight() - 50
root.geometry(str(x) + 'x' + str(y) + '+' + str(-5) + '+' + str(0))
#root.eval("tk::PlaceWindow . center")
root.pack_propagate(False)

#====== WIDGETS ======

mainLabel = tk.Label(root, text="Press 'Next' to begin", fg="black", font=("Microsoft JhengHei", 15))
mainLabel.pack()

counter = tk.Label(root, text="  "+str(meme_number)+" of "+str(len(finalFiles))+"  ",
 fg="black", font=("Microsoft JhengHei", 12))
counter.place(x=root.winfo_screenwidth()/2, y=root.winfo_screenheight()//1.2)

# imgSrc = Image.open("C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/cover.png")
# imgSrc = imgSrc.resize((700, 500), Image.Resampling.LANCZOS)
# img = ImageTk.PhotoImage(file=imgSrc)
img = ImageTk.PhotoImage(file="C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/cover.png")
img_widget = tk.Label(root, image=img, cursor="hand2",
 height=root.winfo_screenheight()//1.5, width=root.winfo_screenwidth()-100)
img_widget.image = img
img_widget.grid(row=2, column=1, pady=50, padx=50)

nextBtn = tk.Button(root, text="Next", font=("Gadugi", 12),
 bg="#731e93", fg="white", cursor="hand2", activebackground="#8c15b7",
  activeforeground="white", command=lambda:next())
nextBtn.place(x=root.winfo_screenwidth()/2+100, y=root.winfo_screenheight()//1.2)

backBtn = tk.Button(root, text="Back", font=("Gadugi", 12),
 bg="#c4c4c4", fg="gray", cursor="hand2", activebackground="#c4c4c4",
  activeforeground="gray", command=lambda:tooFarBack())
backBtn.place(x=root.winfo_screenwidth()/2-75, y=root.winfo_screenheight()//1.2)

matureBtn = tk.Button(root, text="+18", font=("Gadugi", 12),
 bg="#ff9d00", fg="white", cursor="hand2", activebackground="#ff9d00",
  activeforeground="white", command=lambda:mature())
matureBtn.place(x=root.winfo_screenwidth()-48, y=5)

infoBtn = tk.Button(root, text=" ? ", font=("Gadugi", 12),
 bg="#0066ff", fg="white", cursor="hand2", activebackground="#0059de",
  activeforeground="white", command=lambda:info())
infoBtn.place(x=5, y=5)

addBtn = tk.Button(root, text=" + ", font=("Gadugi", 12),
    bg="#3cbd76", fg="white", cursor="hand2", activebackground="#3cbd76",
    activeforeground="white", command=lambda:add())  
addBtn.place(x=root.winfo_screenwidth()-50, y=root.winfo_screenheight()-110)


# =========== HIDDEN WIDGETS ===========


reshuffleBtn = tk.Button(root, text="Reshuffle", font=("Gadugi", 12),
   bg="#3cbd76", fg="white", cursor="hand2", activebackground="#3cbd76",
    activeforeground="white", command=lambda:reshuffle())

quitBtn = tk.Button(root, text="Quit", font=("Gadugi", 12),
   bg="#00c8ff", fg="white", cursor="hand2", activebackground="#00c8ff",
    activeforeground="white", command=lambda:end())

returnLabel = tk.Label(root, text="Click 'Return' to return to the memes")

infoLabel = tk.Label(root, text="\n Application Information: \n|  Programmer: Gus Jacobs            |\n| Company Name: Flying Saucer inc. |\n|  Date Created: 1/1/2024           |\n  This app contains hundreds of memes, randomly chosen when prompted  \n Due to design structure this app doesn't allow you to resize the window \n The app contains a data folder with base memes but you can add your own to select from!  \n  The base memes are for all ages, but we include mature memes for an older crowd  \n  To view the adult memes, click the '+18' button  \n  To add memes, click the '+' button \n To remove a meme, click the '-' button \nPlease note, this is the beta version of this software,\n so be prepared for any bugs we have not yet found or fixed\n\nNeed help?\nContact us at:\n  memeGenerator@flyingSaucer.com  |   1-952-945-8697  \nNow to get back to the memes\n\n", bg="white", font=("Gadugi", 24))

returnBtn = tk.Button(root,text="Return", font=("Gadugi", 12),
   bg="#3cbd76", fg="white", cursor="hand2", activebackground="#3cbd76",
    activeforeground="white", command=lambda:returnToMain())

rmvBtn = tk.Button(root, text=" - ", font=("Gadugi", 12),
    bg="#ff0000", fg="white", cursor="hand2", activebackground="#ff0000",
    activeforeground="white", command=lambda:confirm())


# =========== FUNCTIONS ===========


def next():
 global meme_number
 global current_index
 mainLabel.pack_forget()
 rmvBtn.place(x=5, y=root.winfo_screenheight()-110)
 if len(used) == len(finalFiles):
  nextBtn.place_forget()
  backBtn.place_forget()
  counter.place_forget()
  reshuffleBtn.place(x=root.winfo_screenwidth()/2, y=root.winfo_screenheight()//1.2)
  quitBtn.place(x=root.winfo_screenwidth()/1.95, y=root.winfo_screenheight()//1.145)
 else:
  meme_number = meme_number + 1
  if current_index == -1:
   while True:
    x = randrange(0, len(finalFiles))
    if x in used:
     continue 
    else:
     used.append(x)
     img2 = Image.open(inFolder + "/" + finalFiles[x])
     imgSrc2 = img2.resize((600, 550))
     img2final = ImageTk.PhotoImage(imgSrc2)
     #img2 = ImageTk.PhotoImage(file=inFolder + "/" + finalFiles[x])
     img_widget.configure(image=img2final)
     img_widget.image = img2final
     break
  else:
   current_index = current_index+1
   z = used[current_index]
   img2 = ImageTk.PhotoImage(file=inFolder + "/" + finalFiles[z])
   img_widget.configure(image=img2)
   img_widget.image = img2
   if used[1] == z:
    backBtn.configure(bg="gray", fg="black", cursor="hand2", activebackground="white",activeforeground="black", command=lambda:back())
  if len(used) > 1:
   backBtn.configure(bg="gray", fg="black", cursor="hand2", activebackground="white",activeforeground="black", command=lambda:back())
 counter.configure(text="  "+str(meme_number)+" of "+str(len(finalFiles))+"  ")  

def back():
 global meme_number
 global current_index
 meme_number = meme_number - 1
 current_index = current_index - 1
 print(current_index)
 x = used[current_index]
 # img2 = ImageTk.PhotoImage(file=inFolder + "/" + finalFiles[x])
 # img_widget.configure(image=img2)
 # img_widget.image = img2
 img2 = Image.open(inFolder + "/" + finalFiles[x])
 imgSrc2 = img2.resize((600, 600))
 img2final = ImageTk.PhotoImage(imgSrc2)
 img_widget.configure(image=img2final)
 img_widget.image = img2final
 if used[0] == x:
  backBtn.configure(bg="#c4c4c4", fg="gray", activebackground="#c4c4c4", activeforeground="gray",command=lambda:tooFarBack())
 if used[len(used)-1] == x:
  nextBtn.configure(bg="#731e93", fg="white", cursor="hand2", activebackground="#8c15b7",activeforeground="white", command=lambda:next())
 counter.configure(text="  "+str(meme_number)+" of "+str(len(finalFiles))+"  ")

def mature():
 global files
 global inFolder
 global used
 global meme_number
 global current_index
 current_index = -1
 used = []
 inFolder = "C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/memes18"
 files = os.listdir(inFolder)
 coverImg = ImageTk.PhotoImage(file="C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/cover2.png")
 img_widget.configure(image=coverImg)
 img_widget.image = coverImg
 initializeMemes()
 counter.configure(text="  "+"0"+" of "+str(len(finalFiles))+"  ")
 # if meme_number <= 1:
 backBtn.configure(bg="#c4c4c4", fg="gray", activebackground="#c4c4c4",activeforeground="gray",command=lambda:tooFarBack())
 # if meme_number > 1:
 #  backBtn.configure(bg="gray", fg="black", activebackground="white",activeforeground="black",command=lambda:back())
 meme_number = 0
 matureBtn.configure(text="  E  ", bg="#17ae00", command=lambda:everyone())

def everyone():
 global files
 global inFolder
 global used
 global meme_number
 global current_index
 current_index = -1
 used = []
 inFolder = "C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/memes"
 files = os.listdir(inFolder)
 coverImg = ImageTk.PhotoImage(file="C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/cover.png")
 img_widget.configure(image=coverImg)
 img_widget.image = coverImg
 initializeMemes()
 counter.configure(text="  "+"0"+" of "+str(len(finalFiles))+"  ")
 # if meme_number <= 1:
 backBtn.configure(bg="#c4c4c4", fg="gray", activebackground="#c4c4c4",activeforeground="gray",command=lambda:tooFarBack())
 # if meme_number > 1:
 #  backBtn.configure(bg="gray", fg="black", activebackground="white",activeforeground="black",command=lambda:back())
 meme_number = 0
 matureBtn.configure(text="+18", bg="#ff9d00", command=lambda:mature())

def info():
 img_widget.grid_forget()
 nextBtn.place_forget()
 backBtn.place_forget()
 mainLabel.pack_forget()
 counter.place_forget()
 addBtn.place_forget()
 rmvBtn.place_forget()
 matureBtn.place_forget()
 returnLabel.pack()
 infoLabel.place(x=60, y=20)
 returnBtn.place(x=root.winfo_screenwidth()/2.1, y=root.winfo_screenheight()//1.15)

def returnToMain():
 returnLabel.pack_forget()
 infoLabel.place_forget()
 returnBtn.place_forget()
 img_widget.grid(row=2, column=1, pady=50, padx=50)
 nextBtn.place(x=root.winfo_screenwidth()/2+100, y=root.winfo_screenheight()//1.2)
 backBtn.place(x=root.winfo_screenwidth()/2-75, y=root.winfo_screenheight()//1.2)
 mainLabel.pack()
 counter.place(x=root.winfo_screenwidth()/2, y=root.winfo_screenheight()//1.2)
 addBtn.place(x=root.winfo_screenwidth()-50, y=root.winfo_screenheight()-110)
 matureBtn.place(x=root.winfo_screenwidth()-48, y=5)

def reshuffle():
 global used
 global meme_number 
 used = []
 meme_number = 0
 nextBtn.place(x=root.winfo_screenwidth()/2+100, y=root.winfo_screenheight()//1.2)
 backBtn.place(x=root.winfo_screenwidth()/2-75, y=root.winfo_screenheight()//1.2)
 counter.place(x=root.winfo_screenwidth()/2, y=root.winfo_screenheight()//1.2)
 reshuffleBtn.place_forget()
 quitBtn.place_forget()
 initializeMemes()

def end():
 time.sleep(1)
 quit()

def add():
 fname = askopenfilename()
 print(fname)
 shutil.copy(fname,inFolder)
 if inFolder == "C:/Users/Gus/Documents/Programming Files/Projects/Meme Generator/memes":
  everyone()
 else:
  mature()

def remove():
 global meme_number
 x = used[-1]
 y = finalFiles[x]
 os.remove(inFolder+"/"+y)
 used.remove(x)
 finalFiles.remove(y)
 meme_number = meme_number-1
 next()
 print(y) # for dev use

def confirm():
 x = tk.messagebox.askokcancel(title="Confirm Delete", message="Are you sure you want to remove and delete '"+finalFiles[used[-1]]+"' permanently? (Notice: this action cannot be undone)")
 if x == True:
  remove()

def tooFarBack():
 x = tk.messagebox.showinfo(title="Cannot Go Back", message="You have reached the back of the meme list")


root.mainloop()


# ============== DEV LOG ==============


# ---  PROJECT COMPLETE  ---