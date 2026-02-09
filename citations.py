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
    option = sourcetype.get(sourcetype.curselection())

    for widget in fields.winfo_children():
        widget.grid_remove()

    for i, widget in enumerate(sourcetypes[option]):
        widget.grid(row=i, column=0)

        


root = tk.Tk()
root.geometry(f"960x720")

frm = tk.ttk.Frame(root, padding=10)
frm.grid()

test = tk.Label(frm, text="citation generator")
test.grid(row=0, column=0)
print(test)

fields = tk.Frame(root)
fields.grid(row=7, column=0)



sourcetypes = {
    "Book": [
        tk.Label(fields, text="Word")

    ],

    "Article": [
    ],

    "Periodical": [
    ],

    "Scholarly journal": [
    ],

    "Dissertation or thesis": [
    ],

    "Website": [
    ],

    "Blog post": [
    ],

    "Social media": [
    ],

    "Video": [
    ],

    "Image": [
    ],

    "Artwork": [
    ],

    "Music": [
    ],

    "Podcast": [
    ],

    "Speech or interview": [
    ],

    "Court case": [
    ],

    "Religious text": [
    ],

    "Map": [
    ],

    "Other": [
    ],

}

sourcetype = tk.Listbox(root, listvariable=tk.Variable(value=list(sourcetypes.keys())), selectmode="browse", height=len(sourcetypes))
sourcetype.bind("<<ListboxSelect>>", select_type)
sourcetype.grid(row=1, column=0, padx=(20, 20))


tk.Label(root, text="Author's first name").grid(row=3, column=2)
tk.Label(root, text="Author's middle name").grid(row=4, column=2)
tk.Label(root, text="Author's last name").grid(row=5, column=2)

fn = tk.Entry(root)
fn.grid(row=3, column=3)

mn = tk.Entry(root).grid(row=4, column=3)

ln = tk.Entry(root)
ln.grid(row=5, column=3)

textframe = tk.Frame(root)
textframe.grid(row=1, column=4)


f = tk.Text(textframe, wrap="word", width=20, height=10, state="disabled")
f.grid(row=0, column=0)

button = tk.Button(root, text="Get Entry Value", command=get_entry)
button.grid(row=6, column=2)


root.mainloop()
