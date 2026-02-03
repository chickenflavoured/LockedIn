import tkinter as tk
from tkinter import ttk
import pyperclip



root = tk.Tk()
root.geometry(f"960x720")

frm = tk.ttk.Frame(root, padding=10)
frm.grid()

tk.Label(frm, text="citation generator").grid(row=1, column=0)

sourcetypes = (
    "Book",
    "Article",
    "Periodical",
    "Scholarly journal",
    "Dissertation or thesis",
    "Website",
    "Blog post",
    "Social media",
    "Video",
    "Image",
    "Artwork",
    "Music",
    "Podcast",
    "Speech or lecture",
    "Interview",
    "Court case",
    "Map",
    "Religious text",
    "Other"
)

sourcetype = tk.Listbox(root, listvariable=tk.Variable(value=sourcetypes), height=len(sourcetypes))
sourcetype.grid(row=2, column=0, padx=(20, 20))


tk.Label(root, text="Author's first name").grid(row=3, column=2)
tk.Label(root, text="Author's middle name").grid(row=4, column=2)
tk.Label(root, text="Author's last name").grid(row=5, column=2)

fn = tk.Entry(root).grid(row=3, column=3)
mn = tk.Entry(root).grid(row=4, column=3)
ln = tk.Entry(root).grid(row=5, column=3)


root.mainloop()