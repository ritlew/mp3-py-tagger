from tkinter import Tk, Label, Button, Grid

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("MP3py")

        self.v1_label = Label(master, text="ID3v1")
        self.v1_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.v2_label = Label(master, text="ID3v2")
        self.v2_label.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

if __name__ == "__main__":
	root = Tk()

	root.geometry("600x500")
	root.resizable(width=False, height=False)

	for i in range(4):
		Grid.columnconfigure(root, i, weight=1)

	my_gui = MyFirstGUI(root)
	root.mainloop()