import tkinter as tk
from tkinter import ttk
import pyperclip


def get_entry():
    author = f"{ln.get()}, {fn.get()}"
    f.config(state="normal")
    f.delete(1.0, tk.END)
    f.insert(1.0, author)
    f.config(state="disabled")


def select_type(event):

    if sourcetype.get(1) == "Book":
        print(sourcetype.get(0))
        tk.Label(root, text="Word").grid(row=5, column=5)


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

sourcetype = tk.Listbox(root, listvariable=tk.Variable(value=sourcetypes), selectmode="browse", height=len(sourcetypes))
sourcetype.bind("<<ListboxSelect>>", select_type)
sourcetype.grid(row=2, column=0, padx=(20, 20))


tk.Label(root, text="Author's first name").grid(row=3, column=2)
tk.Label(root, text="Author's middle name").grid(row=4, column=2)
tk.Label(root, text="Author's last name").grid(row=5, column=2)

fn = tk.Entry(root)
fn.grid(row=3, column=3)

mn = tk.Entry(root).grid(row=4, column=3)

ln = tk.Entry(root)
ln.grid(row=5, column=3)

textframe = tk.Frame(root)
textframe.grid(row=6, column=0)


f = tk.Text(textframe, wrap="word", width=20, height=10, state="disabled")
f.insert(1.0, "hello")
f.grid(row=1, column=1)

button = tk.Button(root, text="Get Entry Value", command=get_entry)
button.grid(row=6, column=2)


root.mainloop()