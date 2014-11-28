from tkinter import *

def getEnEtTranslation(input):
    global dict_et_en
    global dict_en_et
    
    input = input[0]
    
    if not (dict_en_et and dict_et_en):
        f = open("en_et_words.txt", encoding="UTF8")
        dict_en_et = {}
        dict_et_en = {}
        for line in f:
            line = line.strip("\n").split("\t")
            if len(line) != 2:
                continue
            dict_en_et[line[0]] = line[1]
            dict_et_en[line[1]] = line[0]
        f.close()

    root = Tk()
    root.title("Sõnastik")
    root.geometry("400x200")

    x_scrollbar = Scrollbar(root, orient=HORIZONTAL)
    x_scrollbar.pack(side=BOTTOM, fill=X)
    y_scrollbar = Scrollbar(root)
    y_scrollbar.pack(side=RIGHT, fill=Y)

    listbox = Listbox(root, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)

    if input in dict_en_et:
        output = dict_en_et[input]
        listbox.insert(END, output)

    else:
        alphabetical_list = []
        for key in dict_et_en:
            if input in key:
                output = key + ": " + dict_et_en[key]
                alphabetical_list.append(output)
        alphabetical_list.sort()
        for element in alphabetical_list:
            listbox.insert(END, element)
                #must be active, anchor, end, @x,y, or a number
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    x_scrollbar.config(command=listbox.xview)
    y_scrollbar.config(command=listbox.yview)
    root.mainloop()
