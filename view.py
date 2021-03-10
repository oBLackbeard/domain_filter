import tkinter as tk
from tkinter import ttk, filedialog
from controlle import Attak


class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.control = Attak(view=self)

        label_header = tk.Label(
            parent, text="DomainFilter", font=("Verdana Pro Cond Black", 25))
        label_header.place(rely=0.01, relx=0.80)

        label = tk.Label(parent, text='import you mailiste')
        label.place(rely=0.06, relx=0.02)
        self.label_dict_file = tk.Label(parent, relief="ridge", anchor="w")
        self.label_dict_file.place(rely=0.09, relx=0.02, height=23, width=750)
        btn_dict_file = ttk.Button(
            parent, text="Browse...", command=self.set_path)
        btn_dict_file.place(rely=0.09, relx=0.80)

        btn_launch_attack = ttk.Button(
            parent, text="Start!", command=self.start)
        btn_launch_attack.place(rely=0.09, relx=0.90)

        frame_output = tk.LabelFrame(parent, text="Attack Output")
        frame_output.place(rely=0.14, relx=0.02, height=475, width=980)

        self.text_output = tk.Text(frame_output, wrap=tk.NONE)
        self.text_output.place(relheight=1, relwidth=1)
        text_scrolly = tk.Scrollbar(
            frame_output, orient="vertical", command=self.text_output.yview)
        text_scrollx = tk.Scrollbar(
            frame_output, orient="horizontal", command=self.text_output.xview)
        self.text_output.configure(
            yscrollcommand=text_scrolly.set, xscrollcommand=text_scrollx.set)
        text_scrolly.pack(side="right", fill="y")
        text_scrollx.pack(side="bottom", fill="x")

    def file_dialog(self):
        filename = tk.filedialog.askopenfilename(
            initialdir='/', title='Select Combo', filetypes=(('Text Files', '*.txt'), ('All files', '*.*')))
        return filename

    def set_path(self):
        path = self.file_dialog()
        self.label_dict_file['text'] = path

    def display_output(self, message, update_task=False):
        self.text_output.insert('end', f"{message} \n")
        self.text_output.see('end')
        if update_task:
            self.text_output.update_idletasks()

    def clear_output(self):
        self.text_output.delete('1.0', 'end')

    def start(self):
        mailliste_file = self.label_dict_file['text']
        self.control.launch(mailliste_file)
