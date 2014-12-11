__version__ = 0.1

from tkinter import *
from tkinter import ttk
from datetime import datetime
import logging
import Main_window
import Internal_commands
import Parse_input
import Function_keywords
import Function_inspection
import Weather
import URL_open
import Equation_and_function_solve
import Inequality_solve
import Function_differentiation
import Function_integration
import Calculator


def getFunctionWithArgs(args):
    if Internal_commands.changeSettingArgsHandler(args):
        # internal setting change?
        return 'Internal_commands.changeSetting'
    spec_url = URL_open.openSpecialUrlArgsHandler(args)
    if spec_url is not None:
        # special url?
        return spec_url
    if URL_open.openUrlArgsHandler(args):
        # URL?
        return 'URL_open.openUrl'
    if Function_differentiation.solveDiffArgsHandler(args):
        return 'Function_differentiation.diffFunction'
    if Function_integration.integrateFunctionArgsHandler(args):
        return 'Function_integration.integrateFunction'
    if Inequality_solve.solveInequalityArgsHandler(args):
        # võrratus?
        return 'Inequality_solve.Inequality'
    if Function_inspection.funcInspectArgsHandler(args):
        # function?
        return 'Equation_and_function_solve.Function'
    if Equation_and_function_solve.solveEquationArgsHandler(args):
        # equation?
        return 'Equation_and_function_solve.Equation'
    if Weather.weatherArgsHandler(args):
        # weather request?
        return 'Weather.weatherInformation'
    return 'Calculator.Calc'

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
        eval('Main_window.root.after(' + str(400*i) + ', errorEntry)')
        eval('Main_window.root.after(' + str(400*(i+1)) + ', restoreEntry)')

def userExit():
    global root
    logging.info('Closed ReisidAafrikasse.')
    Main_window.root.destroy()

def main(*args):
    global user_args
    user_args_coms = Parse_input.parseInput(main_ent.get(), '[', ']')
    if user_args_coms == -1:
        # If user input is incorrect
        incorrectInput()
    elif user_args_coms:
        # If user input is non-empty
        user_args, user_coms = user_args_coms
        logging.info('Argument(s) found: [%s]' %', '.join(user_args))

        if user_coms:
            logging.info('Command(s) found: [%s]' %', '.join(user_coms))
            corr_func_name = getFunctionWithComs(user_coms)
            if corr_func_name is None:
                corr_func_name = getFunctionWithArgs(user_args)
                logging.info('Found function by arguments: %s' % corr_func_name)
            else:
                logging.info('Found function by commands: %s' %corr_func_name)
        else:
            corr_func_name = getFunctionWithArgs(user_args)
            logging.info('Found function by arguments: %s' % corr_func_name)

        try:
            eval(corr_func_name + '(user_args)')
        except Exception as e:
            incorrectInput()
            logging.exception(e)



###########
if __name__ == '__main__':
    logging.basicConfig(filename='.\\logs\\RA_%s.txt' %datetime.now().strftime("%y.%m.%d.%H-%M-%S"), level=logging.DEBUG,
                        format='%(asctime)s | %(levelname)s | %(funcName)s | %(message)s')
    logging.info('Started ReisidAafrikasse %s.' %__version__)

    Main_window.root.title('ReisidAafrikasse %s' %__version__)
    Main_window.root.resizable(width=FALSE, height=FALSE)
    Main_window.root.geometry('345x105')

    mainframe_st = ttk.Style()
    mainframe_st.configure('mainframe.TFrame', background='white')

    mainframe = ttk.Frame(Main_window.root, style='mainframe.TFrame')
    mainframe.place(x=0, y=0, relwidth=1, relheight=1)

    bg_img = PhotoImage(file='main_bg.png')
    bg_lbl = Label(mainframe, image=bg_img)
    bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

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

    Main_window.root.protocol('WM_DELETE_WINDOW', userExit)

    Main_window.root.mainloop()
