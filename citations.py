import tkinter as tk
from tkinter import ttk
import pyperclip


def get_entry():
    author = f"{ln.get()}, {fn.get()}"

    f.config(state="normal")
    f.delete(1.0, tk.END)
    f.insert(1.0, author)
    f.insert(1.5, mn.get())
    f.config(state="disabled")


def select_type(event):
    option = sourcetype.get(sourcetype.curselection())

    for widget in fields.winfo_children():
        widget.grid_remove()

    for i, field in enumerate(sourcetypes[option]):
        for j, widget in (enumerate(field)):
            widget.grid(row=i, column=j)


FORMAT = {
    "name"
}


def select_style(event):
    pass


def render_citation(**kwargs):
    pass


root = tk.Tk()
root.geometry(f"960x720")

general = tk.Frame(root)
general.grid(row=1, column=0)

fields = tk.Frame(root)
fields.grid(row=8, column=0)


"""
Every field has
- Label
- Entry
- variable

{"variable": [Label, Entry]}
"""



sourcetypes = {
    "Book": [

        [tk.Label(fields, text="Title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Subtitle"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Publisher"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Edition"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Volume"),
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

        [tk.Label(fields, text="Location"),
         tk.Entry(fields)],

        [tk.Label(fields, text="City"),
         tk.Entry(fields),
         tk.Label(fields, text="Country"),
         tk.Entry(fields)]
    ],

    "Image": [
        [tk.Label(fields, text="Title or description"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Medium"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Website name"),
         tk.Entry(fields)]
    ],

    "Music": [
        [tk.Label(fields, text="Title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Album or suite"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Label"),
         tk.Entry(fields)],
    ],

    "Podcast": [
        [tk.Radiobutton(fields, text="Podcast", value="podcast"),
         tk.Radiobutton(fields, text="Episode", value="episode")],
        [tk.Label(fields, text="Podcast title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Episode title"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Episode number"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Year started"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Year ended"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Production company"),
         tk.Entry(fields)],

        [tk.Radiobutton(fields, text="Audio", value="audio"),
         tk.Radiobutton(fields, text="Video", value="video")],
    ],

    "Presentation": [
        [tk.Label(fields, text="Title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Type of presentation"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Location"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="City"),
         tk.Entry(fields),
         tk.Label(fields, text="Country"),
         tk.Entry(fields)]
    ],

    "Thesis or dissertation": [
        [tk.Radiobutton(fields, text="Thesis", value="thesis"),
         tk.Radiobutton(fields, text="Dissertation", value="dissertation")],

        [tk.Label(fields, text="Title"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Institution"),
         tk.Entry(fields)],

        [tk.Label(fields, text="Source name"),
         tk.Entry(fields)],

    ],

    "Court case": [
        [tk.Label(fields, text="Plaintiff"),
         tk.Entry(fields),
         tk.Label(fields, text="Defendant"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Volume number"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Reporter"),
         tk.Entry(fields)],
        
        [tk.Label(fields, text="Court jurisdiction"),
         tk.Entry(fields)]
    ]

}

sourcetype = tk.Listbox(general, listvariable=tk.Variable(value=list(sourcetypes.keys())), selectmode="browse", height=len(sourcetypes), exportselection=False)
sourcetype.bind("<<ListboxSelect>>", select_type)
sourcetype.grid(row=1, column=0, padx=40, pady=40)

"""
style = tk.ttk.Combobox(general, values=["APA", "MLA", "Chicago"])
style.bind("<<ComboboxSelected>>", select_style)
style.grid(row=2, column=0)
"""


tk.Label(general, text="Author's first name").grid(row=3, column=2)
tk.Label(general, text="Author's middle name").grid(row=4, column=2)
tk.Label(general, text="Author's last name").grid(row=5, column=2)
tk.Label(general, text="Author nickname").grid(row=6, column=2)
tk.Label(general, text="Publication date").grid(row=4, column=4)
tk.Label(general, text="URL").grid(row=5, column=4)


fn = tk.Entry(general)
fn.grid(row=3, column=3)

mn = tk.Entry(general)
mn.grid(row=4, column=3)

ln = tk.Entry(general)
ln.grid(row=5, column=3)

nn = tk.Entry(general)
nn.grid(row=6, column=3)

date = tk.Entry(general)
date.grid(row=4, column=5)

url = tk.Entry(general)
url.grid(row=5, column=5)

textframe = tk.Frame(general)
textframe.grid(row=1, column=2)


f = tk.Text(textframe, wrap="word", width=20, height=10, state="disabled")
f.grid(row=0, column=0)

style = tk.OptionMenu(textframe, tk.StringVar(general, "Style..."), "APA", "MLA", "Chicago")
style.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(general, text="Update", command=get_entry)
button.grid(row=7, column=2, padx=10, pady=10)


root.mainloop()
