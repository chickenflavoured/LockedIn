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

    for i, field in enumerate(sourcetypes[option]):
        for j, widget in (enumerate(field)):
            widget.grid(row=i, column=j)


root = tk.Tk()
root.geometry(f"960x720")

frm = tk.ttk.Frame(root, padding=10)
frm.grid()

test = tk.Label(frm, text="citation generator")
test.grid(row=0, column=0)

fields = tk.Frame(root)
fields.grid(row=8, column=0)


sourcetypes = {
    "Book": [

        [tk.Label(fields, text="Title"),
        tk.Entry(fields)],

        [tk.Label(fields, text="Subtitle"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Publisher"),
         tk.Entry(fields)],

        [tk.Label(fields, text="DOI"),
         tk.Entry(fields)]

    ],

    "Article": [
        [tk.Label(fields, text="Article title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Journal name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Volume No."),
         tk.Entry(fields)],

        [tk.Label(fields, text="Issue No."),
         tk.Entry(fields)],

        [tk.Label(fields, text="Start page"),
         tk.Entry(fields),
         tk.Label(fields, text="End page"),
         tk.Entry(fields)],

        [tk.Label(fields, text="DOI"),
         tk.Entry(fields)]
    ],

    "Website": [
        [tk.Label(fields, text="Page title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Website name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Date accessed"),
         tk.Entry(fields)]

    ],

    "Blog post": [
        [tk.Label(fields, text="Post title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Blog name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Version number"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Organization name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Date accessed"),
         tk.Entry(fields)]
    ],

    "Social media": [
        [tk.Radiobutton(fields, text="Post", value="post"),
         tk.Radiobutton(fields, text="Comment", value="comment")],

        [tk.Label(fields, text="Author handle"),
         tk.Entry(fields)],

         [tk.Label(fields, text="Content"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Time"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Website name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Date accessed"),
         tk.Entry(fields)],
    ],

    "Video": [
        [tk.Label(fields, text="Video title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Website name"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Uploader"),
        tk.Entry(fields)],
    ],

    "Artwork": [
        [tk.Label(fields, text="Title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Medium"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Location/source"),
         tk.Entry(fields)],

        [tk.Label(fields, text="City"),
         tk.Entry(fields),
         tk.Label(fields, text="Country"),
         tk.Entry(fields)]
    ],

    "Music": [
        [tk.Label(fields, text="Location/source"),
         tk.Entry(fields)],
    ],

    "Podcast": [
    ],

    "Speech or interview": [
    ],

    "Thesis or dissertation": [
    ],

    "Court case": [
    ],

    "Religious text": [
    ],

    "Other": [
    ],

}

sourcetype = tk.Listbox(root, listvariable=tk.Variable(value=list(sourcetypes.keys())), selectmode="browse", height=len(sourcetypes), exportselection=False)
sourcetype.bind("<<ListboxSelect>>", select_type)
sourcetype.grid(row=1, column=0, padx=(50, 20))


tk.Label(root, text="Author's first name").grid(row=3, column=2)
tk.Label(root, text="Author's middle name").grid(row=4, column=2)
tk.Label(root, text="Author's last name").grid(row=5, column=2)
tk.Label(root, text="Publication date").grid(row=4, column=4)
tk.Label(root, text="URL").grid(row=5, column=4)


fn = tk.Entry(root)
fn.grid(row=3, column=3)

mn = tk.Entry(root)
mn.grid(row=4, column=3)

ln = tk.Entry(root)
ln.grid(row=5, column=3)

date = tk.Entry(root)
date.grid(row=4, column=5)

url = tk.Entry(root)
url.grid(row=5, column=5)

textframe = tk.Frame(root)
textframe.grid(row=1, column=9)


f = tk.Text(textframe, wrap="word", width=20, height=10, state="disabled")
f.grid(row=0, column=0)

button = tk.Button(root, text="Get Entry Value", command=get_entry)
button.grid(row=7, column=2)


root.mainloop()
