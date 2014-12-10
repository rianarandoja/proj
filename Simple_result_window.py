from tkinter import *

def resultWindow(result, user_input):

    s_res_win = Tk()
    s_res_win.title("Aafrika")

    listbox = Listbox(s_res_win, selectmode=MULTIPLE, height=5, width=50, selectbackground="gold2", activestyle="none")
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    listbox.insert(0, "")
    listbox.insert(1, " "*30 + user_input)
    listbox.insert(2, "")

    if isinstance(result, list):
        for el in result:
            listbox.insert(END, str("           •   " + str(el).strip()))

    else:
        listbox.insert(3, str("           •   " + str(result).strip()))

    listbox.insert(END, "")

    s_res_win.mainloop()
