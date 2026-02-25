import tkinter as tk
from tkinter import ttk
import pyperclip


def get_entry():
    f.config(state="normal")
    f.delete(1.0, tk.END)

    author = f"{ln.get()}, {fn.get()[0]}. "
    f.insert(1.0, author)

    time = f"({date.get()}). "
    f.insert(2.0, time)

    ititle = f"*{variables["ititle"][0].get()}*. "
    f.insert(3.0, ititle)

    title = f"{variables["title"][0].get()}. "
    f.insert(3.0, title)

    f.config(state="disabled")


def select_type(event):
    option = sourcetype.get(sourcetype.curselection())

    for widget in fields.winfo_children():
        widget.grid_remove()

    i = 0
    fields_used = sourcetypes[option]
    for field in fields_used:
        i += 1
        tk.Label(fields, text=field).grid(row=i, column=0)
        for j, widget in enumerate(variables[fields_used[field]]):
            widget.grid(row=i, column=j + 1)


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

variables = {
    "author": [tk.Entry(fields)],
    "ititle": [tk.Entry(fields)],
    "title": [tk.Entry(fields)],
    "subtitle": [tk.Entry(fields)],
    "pub": [tk.Entry(fields)],
    "ipub": [tk.Entry(fields)],
    "episode": [tk.Entry(fields)],
    "edition": [tk.Entry(fields)],
    "volume": [tk.Entry(fields)],
    "issue": [tk.Entry(fields)],
    "type": [tk.Entry(fields)],
    "source": [tk.Entry(fields)],
    "isource": [tk.Entry(fields)],
    "album": [tk.Entry(fields)],
    "city": [tk.Entry(fields)],
    "country": [tk.Entry(fields)],
    "institution": [tk.Entry(fields)],
    "date": [tk.Entry(fields)],
    "sp": [tk.Entry(fields)],
    "ep": [tk.Entry(fields)],
    "sy": [tk.Entry(fields)],
    "ey": [tk.Entry(fields)],
    "doi": [tk.Entry(fields)],
    "url": [tk.Entry(fields)],
    "accessed": [tk.Entry(fields)],

    "media": [tk.Radiobutton(fields, text="Post", value="post"),
              tk.Radiobutton(fields, text="Comment", value="comment")],

    "isep": [tk.Radiobutton(fields, text="Whole podcast", value="podcast"),
                tk.Radiobutton(fields, text="Single episode", value="episode")],

    "podtype": [tk.Radiobutton(fields, text="Audio", value="audio"),
                tk.Radiobutton(fields, text="Video", value="video")],
    
    "degree": [tk.Radiobutton(fields, text="Thesis", value="thesis"),
                tk.Radiobutton(fields, text="Dissertation", value="dissertation")]
}

sourcetypes = {
    "Book": {
        "Title": "ititle",
        "Subtitle": "subtitle",
        "Publisher": "pub",
        "Edition": "edition",
        "Volume": "volume",
        "DOI": "doi"
    },

    "Article": {
        "Article title": "title",
        "Journal name": "isource",
        "Volume No.": "volume",
        "Issue No.": "issue",
        "Start page": "sp",
        "End page": "ep",
        "DOI": "doi"
    },

    "Website": {
        "Page title": "ititle",
        "Website name": "source",
        "Date accessed": "accessed"
    },

    "Blog post": {
        "Post title": "title",
        "Blog name": "isource",
        "Publisher": "ipub",
        "Date accessed": "accessed",
    },

    "Social media": {
        "Post or comment": "media",
        "Post title": "ititle",
        "Content": "ititle",
        "Website name": "source",
        "Date accessed": "accessed"
        
    },

    "Video": {
        "Video title": "ititle",
        "Website name": "source"
    },

    "Artwork": {
        "Title": "ititle",
        "Medium": "type",
        "Museum or source": "source",
        "City": "city",
        "Country": "country"
    },

    "Image": {
        "Title or description": "title",
        "Medium": "type",
        "Source": "source"
    },

    "Music": {
        "Title": "title",
        "Album": "album",
        "Label": "source"
    },

    "Podcast": {
        "Audio or video": "podtype",
        "Episode or podcast": "isep",
        "Podcast title": "isource",
        "Episode title": "title",
        "Episode number": "episode",
        "Year started": "sy",
        "Year ended": "ey",
        "Production company": "source",
    },

    "Presentation": {
        "Title": "ititle",
        "Type of presentation": "type",
        "Title of conference": "source",
        "City": "city",
        "Country": "country"
    },

    "Thesis or dissertation": {
        "Thesis or dissertation": "degree",
        "Title": "ititle",
        "Institution": "institution",
        "Source name": "source"
    }
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
