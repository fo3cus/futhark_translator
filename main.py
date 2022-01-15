from dicts import *
from tkinter import Tk, font, ttk, StringVar, Entry, Button


# * Translate input to elder futhark
def translator():
    i = txt.get()

    for l in letters:
        i = i.lower().replace(l, futhark[l])

    print(i)
    output.set(i)


# * Close all windows
def quit_all(*args):
    root.destroy()


# * Create main display
root = Tk()
root.configure(background="black")

window_width = 800
window_height = 500

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.resizable(False, False)
root.title("Sign In")


# * Set up form display
font_input = font.Font(family="Helvetica", size=20, weight="bold")
font_output = font.Font(family="Helvetica", size=65, weight="bold")

txt = StringVar()
txtbox = Entry(root, textvariable=txt)

# * Text input
txt_label = ttk.Label(root, text="Enter your english text to translate", font=font_input, foreground="white", background="black")
txt_label.pack(fill="x", expand=True, padx=15, pady=15)

txt_entry = ttk.Entry(root, textvariable=txt)
txt_entry.pack(fill="x", expand=True, padx=15, pady=15)
txt_entry.focus()


# * Button
translate_button = ttk.Button(root, text="Translate", command=translator)
translate_button.pack(fill="x", expand=True, padx=15, pady=15)

# * Output
output = StringVar()

out_label = ttk.Label(root, textvariable=output, font=font_output, foreground="white", background="black", anchor="center")
out_label.pack(fill="x", expand=True, padx=15, pady=15)


if __name__ == "__main__":
    # * Start main loop
    root.mainloop()
