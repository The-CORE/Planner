import tkinter

WINDOW_DIMENSIONS = (1280, 720)

window = tkinter.Tk()

window.title("Planner")
window.geometry(
    "{}x{}".format(*WINDOW_DIMENSIONS)
)
window.resizable(width=False, height=False)

class App:
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.button = tkinter.Button(
            frame,
            text="QUIT",
            fg="red",
            command=frame.quit
        )
        self.button.pack(side=tkinter.LEFT)

        self.hi_there = tkinter.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=tkinter.BOTTOM)

    def say_hi(self):
        print("Hi there, everyone!")

root = tkinter.Tk()

app = App(root)

root.mainloop()
