import os
import pathlib
import shutil
import tkinter as tk
from tkinter import filedialog

fileFormat = {
    "Web": [".html5", ".html", ".htm", ".xhtml"],
    "Picture": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"],
    "Video": [".avi", ".mkv",".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    "Document": [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", "pptx"],
    "Compressed": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
    "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
}

fileTypes = list(fileFormat.keys())
fileFormats = list(fileFormat.values())

def Organize_Files():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return

    for file in os.scandir(folder_selected):
        fileName = pathlib.Path(file)
        fileFormatType = fileName.suffix.lower()

        src = str(fileName)
        dest = "Other"

        if fileFormatType == "":
            output.insert(tk.END, src+ " has no file extension!\n")
            continue
        else:
            for formats in fileFormats:
                if fileFormatType in formats:
                    folder = fileTypes[fileFormats.index(formats)]
                    if not os.path.isdir(os.path.join(folder_selected, folder)):
                        os.mkdir(os.path.join(folder_selected, folder))
                    dest = os.path.join(folder_selected, folder)

            else:
                if not os.path.isdir(os.path.join(folder_selected, "Other")):
                    os.mkdir(os.path.join(folder_selected, "Other"))
                dest = os.path.join(folder_selected, "Other")

        output.insert(tk.END, src+" moved to "+dest+"!\n")
        shutil.move(src, dest)

    output.insert(tk.END, "Organizing complete!\n")

def Clear_Output():
    output.delete("1.0", tk.END)

def Exit_App():
    root.destroy()

root = tk.Tk()
root.title("File Organizer")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack()

organize_button = tk.Button(frame, text="Organize Files", command=Organize_Files)
organize_button.pack(pady=10)

clear_button = tk.Button(frame, text="Clear Output", command=Clear_Output)
clear_button.pack(pady=10)

exit_button = tk.Button(frame, text="Exit", command=Exit_App)
exit_button.pack(pady=10)

output = tk.Text(root, height=20, width=50)
output.pack(pady=10)

root.mainloop()