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

    """Funktsioon võtab sisse listi valemitega. Valemite arv ei ole piiratud. Funktsioon joonistab seejärel teljestiku
     ja graafiku. Pärast iga suurendust joonistatakse kõik uuesti. Uuesti ei joonistata navigeerides, tulenevalt sellest on
     navigeerimine limiteeritud (jõudlust silmas pidades).
     Akna suuruse muutmine põhjustab koordinaatide arvutamises vigu. Tekstiväljad on teistele programmidele kasutamiseks.

     - Väärtus axis_num kalibreerib numbrid teljestiku ja pikslitega. Ta on oluline, et suurendus töötaks.
     - Väärtus magnification_level määrab ära võrrandi suurenduse.
     - Väärtused move_to_x ja move_to_y liidetakse pikslitele otsa, mis tagab õigete koordinaadite kuvamise pärast graafiku liigutamist.
     - Väärtused move_x ja move_y liigutavad graafikut.
     - count_moves_horizontally ja count_moves_vertically limiteerivad kasutaja graafiku liigutamist."""

    equations = []
    for equation in raw_equations:
        if ',' in equation:
            for new_equation in equation.split(','):
                equations.append(new_equation)
        else:
            equations.append(equation)

    height_width = 800

    global coordinates
    global count_moves_horizontally
    global count_moves_vertically
    global move_to_x
    global move_to_y
    count_moves_horizontally, count_moves_vertically = 0, 0 # Graafiku liigutamine
    coordinates = ""
    move_to_x, move_to_y = 0, 0

    global magnification_level
    global axis_num  # Teljenumbrid.
    axis_num = 30  # Teljenumbrid + kalibreerimine.
    zoom_level = 2  # Graafiku suurendus.
    magnification_level = 30  # Graafiku suurendus.

    global count_event  # Koordinaatide kuvamise fn.
    count_event = 0  # Koordinaatide kuvamise fn.

    root = Tk()
    root.title("Funktsioonide uurimine")
    root.geometry("400x400")
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
        x_axis = (-width_, height_//4, width_, height_//4)  # X-telje pikkus
        y_axis = (width_//4, -height_, width_//4, height_)  # Y-telje pikkus

        axis_color = "black"  # Telje värv
        grid_color = "lightgrey"  # Ruudustiku värvus
        number_font = "Times 8"

        if axis_num <= 232:  # Ruudustik
            for x in range(-height_ + 10, height_, 15):# 10 kalibreerib teljestiku numbritega.
                canvas.create_line((-width_ + axis_num, x + axis_num, width_,  x + axis_num), fill=grid_color)
                canvas.create_line((x + axis_num, height_, x + axis_num, -height_), fill=grid_color)

            for x in range(-height_ + 10, height_, 30):  # 10 liigutab teljekriipsud paika
                text_x = round((x-200)/axis_num + 1, 1)
                if text_x == 0.0:
                    text_x = 0
                canvas.create_text(x + axis_num, (height_/4) - 15, text=str(text_x), font=number_font)
                canvas.create_line((x + axis_num, 197, x + axis_num, 203), fill="grey")
                # Y-telg:
                text_y = -round((x-200)/axis_num + 1, 1)
                if text_y == 0.0:  # Topelt 0.0 ei ole sobiv.
                    text_y = ""
                canvas.create_text((width_//4) - 15, x + axis_num, text=str(text_y), font=number_font)
                canvas.create_line((197, x + axis_num, 203, x + axis_num), fill="grey")

        else:
            for grid_ in range(-width_, width_, 15):
                canvas.create_line((0, grid_, width_, grid_), fill=grid_color)
                canvas.create_line((grid_, height_, grid_, 0), fill=grid_color)

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
        function_line_colors = ["red", "green", "blue", "yellow", "DarkMagenta", "orange"]
        points = []
        i = 0  # Värvi arvestus.

        for equation in function:
            fn_text_count = 1  # fn'i teksti arvestus.
            for x in range(-width_, width_):
                try:
                    points.append(-x)  # "-" peegeldab graafikut.
                    x = -(x/magnification_level)
                    y = eval(equation)
                except (ZeroDivisionError, ValueError) as _:
                    points.pop()
                    continue

                y = -y*magnification_level  # "-" peegeldab & suurendab graafikut.
                points.append(y)

                x *= magnification_level  # Fn nimede kuvamine.
                if -170 < x < 170 and -170 < y < 170 and fn_text_count != 0:  # Tagab tahvlile jäämise.
                    text = canvas.create_text(x-15, y-10, text=equation, font=font, fill=function_line_colors[i])  # Tekstiväli.
                    canvas.move(text, 200, 200)
                    fn_text_count = 0  # Igale fn'ile üks nimi.
            if i == len(function_line_colors):  # Failsafe.
                i = 0

            function_line = canvas.create_line(points, fill=function_line_colors[i], width=2)  # Loob graafiku
            i += 1
            canvas.move(function_line, 200, 200)  # Liigutab f-n õigesse kohta
            points = []  # Kustutab koordinaadid
        canvas.pack()

    def zoom_out():
        zoomInOut(False)

    def zoom_in():
        zoomInOut(True)

    def zoomInOut(z_in):
        global magnification_level
        global axis_num
        global move_to_x
        global move_to_y
        move_to_x = 1
        move_to_y = 1

        # Taastab graafiku liigutamise võimaluse
        global count_moves_horizontally
        global count_moves_vertically
        count_moves_horizontally, count_moves_vertically = 0, 0
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
        global axis_num
        global move_to_x
        global move_to_y

        if count_event != 0:
            canvas.delete(coordinates)  # Teksivälja kustutamine.
        text_to_display = "X=" + str(round((event.x-200+move_to_x)/axis_num, 2)) + " Y=" + str(round(-(event.y-200+move_to_y)/axis_num, 2))
        coordinates = canvas.create_text(40, 10, text=text_to_display, font=font + " 9")
        count_event += 1

    menu_bar = Menu(root)
    menu_bar.add_command(label="Vähenda", command=zoom_out)
    menu_bar.add_command(label="Suurenda", command=zoom_in)
    root.config(menu=menu_bar)

    def onWheel(event):
        d = event.delta
        if d < 0:
            zoom_out()
        else:
            zoom_in()

    def scroll_function(left=False, right=False, up=FALSE, down=False):
        global count_moves_horizontally
        global count_moves_vertically
        global move_x
        global move_y
        global move_to_x
        global move_to_y
        global coordinates
        move_y, move_x = 0, 0
        canvas.delete(coordinates)
        if left:
            if count_moves_horizontally >= -12:
                move_x += 30
                count_moves_horizontally -= 1
                move_to_x = move_x*count_moves_horizontally
        if right:
            if count_moves_horizontally <= 12:
                move_x -= 30
                count_moves_horizontally += 1
                move_to_x = -move_x*count_moves_horizontally
        if up:
            if count_moves_vertically <= 12:
                move_y += 30
                count_moves_vertically += 1
                move_to_y = -move_y*count_moves_vertically
        if down:
            if count_moves_vertically >= -12:
                move_y -= 30
                count_moves_vertically -= 1
                move_to_y = move_y*count_moves_vertically
        canvas.move(ALL, move_x, move_y)

    def left(event):
        scroll_function(left=True)

    def right(event):
        scroll_function(right=True)

    def up(event):
        scroll_function(up=True)

    def down(event):
        scroll_function(down=True)

    root.bind("<Button-1>", get_Coordinates)  # Koordinaatide kuvamise bindimine.
    root.bind("<MouseWheel>", onWheel)
    root.bind("<Up>", up)
    root.bind("<Down>", down)
    root.bind("<Left>", left)
    root.bind("<Right>", right)
    getCartesianCoordinateSystem()
    plot_function()
    root.mainloop()
