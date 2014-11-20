from tkinter import *
from tkinter import ttk
from math import *

def funcInspectArgsHandler(user_args):
    pass

def funcInspect(raw_equations,
                text_1="",
                text_2="",
                text_3="",
                text_4="",
                text_5="",
                text_6=""):
    equations = []
    for equation in raw_equations:
        if ',' in equation:
            for new_equation in equation.split(','):
                equations.append(new_equation)
        else:
            equations.append(equation)


    height_width = 400
    height_width = 400

    global magnification_level
    global axis_num                                                                           # Teljenumbrid.
    axis_num = 29                                                                             # Teljenumbrid.
    zoom_level = 2                                                                            # Graafiku suurendus.
    magnification_level = 30                                                                  # Graafiku suurendus.

    global count_event                                                                        # Koordinaatide kuvamise fn.
    count_event = 0                                                                           # Koordinaatide kuvamise fn.

    root = Tk()                                                                              # Raam
    root.title("Funktsioonide uurimine")
    root.geometry(str(height_width) + "x" + str(height_width))
    root.resizable(width=FALSE, height=FALSE)
    canvas = Canvas(root, width=height_width, height=height_width, background="white")
    font = "Calibri"

    def getCartesianCoordinateSystem(height_=height_width,
                                     width_=height_width,
                                     font=font,
                                     text_1=text_1,
                                     text_2=text_2,
                                     text_3=text_3,
                                     text_4=text_4,
                                     text_5=text_5,
                                     text_6=text_6):
        global axis_num
        x_axis = (0, height_//2, width_, height_//2)  # X-telje pikkus
        y_axis = (width_//2, 0, width_//2, height_)  # Y-telje pikkus

        axis_color = "black"  # Telje värv
        grid_color = "lightgrey"  # Ruudustiku värvus
        number_font = "Times 8"

        # Ruudustik:
        for grid_ in range(-width_, width_, 15):
            canvas.create_line((0, grid_, width_, grid_), fill=grid_color)
        for grid_ in range(-height_, height_, 15):
            canvas.create_line((grid_, height_, grid_, 0), fill=grid_color)

        # Numbrikriipsud:
        for number_line_x in range(-height_, height_-10, 15):  # (X-telg)
            canvas.create_line((number_line_x, 200, number_line_x, 203), fill="grey")
        for number_line_y in range(-width_+15, width_, 15):  # (Y-telg)
            canvas.create_line((200, number_line_y, 203, number_line_y), fill="grey")

        # Numbrid teljel
        canvas.create_text((width_/2) - 5, (height_/2) - 7, text="0", font=number_font)
        canvas.create_text((width_/2) - axis_num, (height_/2) - 7, text="1", font=number_font)
        canvas.create_text((width_/2) - 5, (height_/2) - axis_num, text="1", font=number_font)
        canvas.create_text((width_/2) + (3.17*axis_num), (height_/2) - 7, text="π", font=number_font)

        canvas.create_line(x_axis, fill=axis_color, arrow=LAST)  # X-telg (koos noolega)
        canvas.create_line(y_axis, fill=axis_color, arrow=FIRST)  # Y-telg (koos noolega)

        # Tekstiväljad:
        canvas.create_text(60, 300, text=text_1, font=font)
        canvas.create_text(60, 330, text=text_2, font=font)
        canvas.create_text(60, 360, text=text_3, font=font)
        canvas.create_text(260, 300, text=text_4, font=font)
        canvas.create_text(260, 330, text=text_5, font=font)
        canvas.create_text(260, 360, text=text_6, font=font)

    def plot_function(width_=height_width,
                      function=equations):
        function_line_colors = ["red", "green", "blue", "yellow","DarkMagenta", "orange"]
        points = []
        i = 0  # Värvi arvestus.

        for equation in function:
            fn_text_count = 1  # fn'i teksti arvestus.
            for x in range(-width_, width_):
                try:
                    points.append(-x)  # "-" peegeldab graafikut.
                    x = -(x/magnification_level)
                    y = eval(equation)  # Väärtustab sõne
                except (ZeroDivisionError, ValueError) as _:
                    points.pop()
                    continue

                y = -y*magnification_level  # "-" peegeldab & suurendab graafikut.
                points.append(y)

                x *= magnification_level  # Fn nimede kuvamine.
                if -170 < x < 170 and -170 < y < 170 and fn_text_count != 0:  # Tagab tahvlile jäämise.
                    text = canvas.create_text(x-15 , y-10, text=equation, font=font, fill=function_line_colors[i])  # Tekstiväli.
                    canvas.move(text, 200, 200)
                    fn_text_count = 0  # Igale fn'ile üks nimi.
            if i == len(function_line_colors):  # Failsafe.
                i = 0

            function_line = canvas.create_line(points, fill=function_line_colors[i], width=2)  # Loob graafiku
            i += 1
            canvas.move(function_line, 200, 200)  # Liigutab f-n õigesse kohta
            points = []  # Kustutab koordinaadid
        canvas.pack()

    def zoom_out():  # F-n vähendus
        zoomInOut(False)

    def zoom_in():  # F-n Suurendus
        zoomInOut(True)

    def zoomInOut(z_in):
        global magnification_level
        global axis_num
        canvas.delete(ALL)
        if z_in:
            magnification_level *= zoom_level
            axis_num *= zoom_level
        else:
            magnification_level /= zoom_level
            axis_num /= zoom_level
        getCartesianCoordinateSystem()
        plot_function()

    def get_Coordinates(event):  # Väljastab koordinaadid.
        global count_event  # Loeb, kui palju on fn käivitatud.
        global coordinates  # Tekstiväli koordinaatidele.
        global axis_num  # Paneb suurenduse paika
        if count_event != 0:
            canvas.delete(coordinates)  # Teksivälja kustutamine.
        text_to_display = "X=" + str(round((event.x-200)/axis_num,2)) + " Y=" + str(round(-(event.y-200)/axis_num,2))
        coordinates = canvas.create_text(40, 10, text=text_to_display, font=font + " 9")
        count_event += 1

    menubar = Menu(root)  # Menüüd suurendamiseks.
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Vähenda", command=zoom_out)
    filemenu.add_command(label="Suurenda", command=zoom_in)
    menubar.add_cascade(label="Suurenda/vähenda", menu=filemenu)
    root.config(menu=menubar)

    root.bind("<Button-1>", get_Coordinates)  # Koordinaatide kuvamise bindimine.
    getCartesianCoordinateSystem()
    plot_function()
    root.mainloop()
