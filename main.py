from tkinter import *
from tkinter import ttk
import Parse_input
import Function_keywords
import Venn_diagram
import Function_inspection
import Weather


def getFunctionWithArgs(args):
    if Function_inspection.funcInspectArgsHandler(args):
        return 'Function_inspection.funcInspect'
    if Weather.weatherArgsHandler(args):
        global user_args
        #print('enne user args: ' + str(user_args))  # DB
        for i in range(len(user_args)): user_args[i] = user_args[i].replace('ilm', '')
        #print('pärast user args: ' + str(user_args))  # DB
        return 'Weather.weatherInformation'
    return ''

def getFunctionWithComs(user_coms):
    user_coms_str = ''.join(user_coms)
    for func in Function_keywords.func_kw_list:
        for i in range(1, len(func)):
            if func[i] in user_coms_str.lower():
                return func[0]

def restoreEntry():
    main_ent_st.configure("EntryStyle.TEntry", fieldbackground="white", foreground="black")
    main_ent.delete(0, END)
    main_ent.insert(0, last_inp)

def errorEntry():
    main_ent_st.configure("EntryStyle.TEntry", fieldbackground="fireBrick3", foreground="#FFF5E7")
    main_ent.delete(0, END)
    main_ent.insert(0, 'Vigane sisend!')

def incorrectInput():
    global last_inp
    last_inp = main_ent.get()
    for i in range(0, 3, 2):
        eval('root.after(' + str(400*i) + ', errorEntry)')
        eval('root.after(' + str(400*(i+1)) + ', restoreEntry)')

def main(*args):
    global user_args
    user_args_coms = Parse_input.parseInput(main_ent.get(), '[', ']')
    if user_args_coms == -1:
        # If user input is incorrect
        incorrectInput()
    elif user_args_coms:
        # If user input is non-empty
        user_args, user_coms = user_args_coms
        print('args:', user_args)  #| DB
        print('coms:', user_coms)  #| DB
        if user_coms:
            #print('command')  # DB
            corr_func_name = getFunctionWithComs(user_coms)
            if corr_func_name is None:
                corr_func_name = getFunctionWithArgs(user_args)
        else:
            #print('w/o command')  # DB
            corr_func_name = getFunctionWithArgs(user_args)

        corr_func = corr_func_name + '(user_args)'
        eval(corr_func)


###########

root = Tk()
root.title('ReisidAafrikasse')
root.wm_attributes('-topmost', 1)  # Always of top
root.wm_attributes('-topmost', 0)  # Always of top
root.resizable(width=FALSE, height=FALSE)
root.geometry('345x105')

mainframe_st = ttk.Style()
mainframe_st.configure('mainframe.TFrame', background='white')

mainframe = ttk.Frame(root, style='mainframe.TFrame')
mainframe.place(x=0, y=0, relwidth=1, relheight=1)

bg_img = PhotoImage(file='main_bg.png')
bg_lbl = Label(mainframe, image=bg_img)
bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

menu_bar = Menu()


main_ent_st = ttk.Style()
# Fimagzen
# http://stackoverflow.com/questions/17635905/ttk-entry-background-colour [20.11.14]
main_ent_st.element_create("plain.field", "from", "clam")
main_ent_st.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])


main_ent = ttk.Entry(mainframe, width=50, style='EntryStyle.TEntry')
main_ent.place(x=20, y=45)
main_ent.focus_set()

ttk.Button(mainframe, text='√Reisile!', command=main).place(x=135, y=65)
main_ent.bind('<Return>', main)

root.mainloop()
