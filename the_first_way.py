import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
import csv
import re
canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
canvas1.pack()
def getCSV():
    all_char = 0
    spaces = 0
    punctuation_marks = 0
    number_of_sentennces = 0
    words = 0
    import_file_path = filedialog.askopenfilename()
    with open(import_file_path, encoding='utf-8') as df:
        read_file = csv.reader(df)
        for line in read_file:
            characters= ",".join(line)
            all_char += len(characters)
            spaces += characters.count(" ")
            punctuation_marks += characters.count(".") + characters.count(",") + characters.count("?") + characters.count("(") + characters.count(")") + characters.count(";") + characters.count("-") + characters.count("_") + characters.count(":") + characters.count("/") + characters.count("\'") + characters.count("\"")
            words += len(re.findall(r"(\w+|\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)", characters))

            number_of_sentennces += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", characters))
        print("Total number of characters:", all_char)
        #print("spaces:", spaces)
        print("Total number of characters without spaces:", all_char - spaces)
        #print("Marks: ", punctuation_marks)
        print("Number of characters without punctuation:", all_char - punctuation_marks)
        print("Number of words:", words)
        print("Number of sentences:", number_of_sentennces)

browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white',
                             font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)
root.mainloop()
