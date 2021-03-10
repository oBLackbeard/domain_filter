import tkinter as tk
from view import View


APP_HEIGHT = 1024
APP_WIDTH = 600


class Aplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Domain Filter')
        main_frame = tk.Frame(self, height=APP_HEIGHT, width=APP_WIDTH)
        main_frame.pack_propagate(0)
        main_frame.pack(fill='both', expand=True)
        self.resizable(0, 0)
        self.geometry(f'{APP_HEIGHT}x{APP_WIDTH}')

        page = View(parent=main_frame)
        page.place(rely=0, relx=0)
        page.tkraise()


if __name__ == '__main__':
    root = Aplication()
    root.mainloop()
