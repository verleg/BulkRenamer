# Python3 code to rename multiple files in a folder at once.

import os
from tkinter import filedialog
from tkinter import *

window = Tk()
folder_selected = "none"
window.title("BulkRenamer")


def clicked():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    lbl.configure(text="Folder: " + folder_selected)


def run():
    i = 0
    print(folder_selected)
    for filename in os.listdir(folder_selected):
        extension = os.path.splitext(filename)[1]
        print(filename)
        dst = txt.get() + str(i)

        if filename != "rename.py":
            os.rename((folder_selected + "/" + filename),
                      (folder_selected+'/' + dst + extension))

            i += 1

    sys.exit()

selectFolderLbl = Label(window, text="Select a folder to rename all files inside:")
selectFolderLbl.grid(column=0, row=0, columnspan=6, sticky=N+S+E+W)

selectFolderBtn = Button(window, text="Select a folder", command=clicked)
selectFolderBtn.grid(column=0, row=1, columnspan=6, sticky=N+S+E+W)

fileNamePaternLbl = Label(window, text="Please enter the new file name:")
fileNamePaternLbl.grid(column=0, row=2, columnspan=6, sticky=N+S+E+W)

txt = Entry(window, width=10)
txt.grid(column=0, row=3, columnspan=6, sticky=N+S+E+W)

renameBtn = Button(window, text="Rename", command=run)
renameBtn.grid(column=0, row=5, columnspan=6, sticky=N+S+E+W)

window.mainloop()
