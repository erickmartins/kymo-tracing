import tkinter as tk
from tkinter import filedialog


def read_file():
    """Simple function to call a dialog window asking for a file


    returns:
    file_path - string with the location of the chosen file
    """

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path
