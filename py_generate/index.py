import tkinter as tk
from tkinter import simpledialog

class MyDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title):
        self.url = None
        super().__init__(parent, title)

    def body(self, frame):
        # print(type(frame)) # tkinter.Frame
        self.url_label = tk.Label(frame, width=25, text="URL")
        self.url_label.pack()
        self.url_box = tk.Entry(frame, width=25)
        self.url_box.pack()
    
    def ok_function(self):
        self.url = self.url_box.get()
        self.destory()

    def cancel_function(self):
        self.destroy()

    def buttonbox(self):
        self.ok_button = tk.Button(self, text='OK', width=5, command=self.ok_function)
        self.ok_button.pack(side="left")
        cancel_button = tk.Button(self, text='Cancel', width=5, command=self.cancel_function)
        cancel_button.pack(side="right")
        self.bind("<Return>", lambda event: self.ok_function())
        self.bind("<Escape>", lambda event: self.cancel_function())

def mydialog(app):
    dialog = MyDialog(title='Get URL', parent=app)
    return dialog.url

def main():
    app = tk.Tk()
    app.title('Dialog')

    url = mydialog(app)
    print(url)

    app.mainloop()

main()