from tkinter import Tk, Frame, Label, BOTH, YES, Toplevel, Button
from PIL import Image, ImageTk


class varis:
	# opens the picture (must be .png) whos name is written in the "Name" txt file
    with open("Desktop/My stuff/FrameWidget/Name", "r") as file:
        pics = file.read().strip("\n").split(", ")
        pic = pics[0]

    w, h = Image.open(f"Desktop/My stuff/FrameWidget/Pictures/{pic}.png").size
    w = int(w / 1.4)
    h = int(h / 1.4)

    root = Tk()
    root.title("Frame")

    root.configure(background="black")
    root.overrideredirect(False)
    dummy = Label(None)
    root.focus_set()

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int(ws - w)
    y = int(hs - h)

    root.geometry(f"{w}x{h}+{x}+{y}")


var = varis()


class NotMyCode(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)

        self.image = Image.open(f"Desktop/My stuff/FrameWidget/Pictures/{var.pic}.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self.resize_image)
        self.p = 0

    def resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


var.root.overrideredirect(True)
e = NotMyCode(var.root)
e.pack(fill=BOTH, expand=YES)
var.root.attributes("-topmost", False)


def button():
    def loop():
        if e.p % 2 == 0:
            var.root.withdraw()
            B.geometry(f"10x10+{var.ws-10}+{var.hs-10}")
            e.p += 1
        else:
            var.root.deiconify()
            B.geometry(f"10x10+{var.x - 10}+{var.hs-10}")
            e.p += 1

    B = Toplevel()
    B.geometry(f"10x10+{var.x - 10}+{var.hs-10}")
    b1 = Button(B, text="", command=loop, bg="#324959", fg="#324959", relief="flat", highlightbackground="#324959")
    b1.pack()
    B.attributes("-topmost", True)
    B.overrideredirect(True)


button()


var.root.mainloop()
