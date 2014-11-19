
import turtle


def drawVennDiagram(raw_list):

    def getNegationPos(lst,
                       pos):
        """
        Võtab argumendiks listi antud avaldise kõigi tähemärkidega ning täiendi märgi indeksi listis.
        Tagastab elemendi indeksi, mille ees peab täiendi definitsiooni järgi olema eitus.
        """
        if lst[pos-1] != ')':
            # Kui täiend on hulga tähise järel, s.t ei ole sulu järel
            return pos-1
        else:
            parens_count = 1
            for i in range(pos-2, -1, -1):
                if lst[i] == '(':
                    parens_count -= 1
                elif lst[i] == ')':
                    parens_count += 1
                if parens_count == 0:
                    return i
        # Kui mõni sulg on veel "avatud", kuid oleme jõudnud avaldise algusesse, siis tagastame None,
        # mis väljendab avaldise ebakorrektsust.
        return -1


    def getTrueEvalsAsList(expression,
                           no_of_vars=3):
        """
        Võtab argumendiks lausearvutuse valemi ja erinevate muutujate arvu selles
        valemis. Tagastab listi binaararvudest, mis väljendavad kõiki selle valemi tõeseid väärtustustusi.
        Funktsioon toetab ka nelja muutujaga valemeid, kuid antud programm tervikuna neid ei toeta.
        """
        true_evals = []
        for i in range(2**no_of_vars):
            # Igal valemil on 2^no_of_vars erinevat väärtustust
            temp = bin(i)[2:].rjust(no_of_vars, '0')

            A = (temp[0] == '1')
            B = (temp[1] == '1')
            if no_of_vars >= 3:
                C = (temp[2] == '1')
            if no_of_vars >= 4:
                D = (temp[3] == '1')

            try:
                if eval(expression):
                    true_evals.append(temp)
            except:
                # Kui tekib probleem seoses valemi väärtustamisega, siis kasutati
                # avaldises illegaalseid sümboleid või muutujaid.
                return -1
        return true_evals


    def getColorBasedOnValue(evaluation):
        """
        Väljastab ala värvimise värvi, sõltuvalt sellele alale
        vastava TDNK liikme olemasolust.
        """
        if evaluation in true_areas:
            return '#CBDCF5'
        else:
            return '#FFFFFF'

    def popupProblem():
        from tkinter import messagebox
        messagebox.showinfo(title='Poiss! Missa vassid!?', message='Paistab, et sisestatud avaldis on ebakorrektne! :(')

    # Järgnevad funktsioonid on välja töötatud geomeetriliste arvutuste teel. Kaarte joonistamisel
    # kasutatud funktsiooni seth() argumendid saadakse järgnevate arvutuste teel:
    # leitakse ringjoone puutuja tõus vajalikus punktis ja võetakse sellest arkustangens, mis
    # annab tõusunurga. Vajalike kaarte pikkused kraadides saadakse järgneva valemi abil:
    # L / (2*pi*r) * 360, kus L on kaare pikkus ühikutes ja r ringi raadius.

    def draw000():
        turtle.begin_fill()
        turtle.seth(270)
        turtle.fd(410)
        turtle.seth(0)
        turtle.fd(420)
        turtle.seth(90)
        turtle.fd(410)
        turtle.seth(180)
        turtle.fd(420)
        turtle.end_fill()


    def draw100():
        turtle.begin_fill()
        turtle.seth(138.19)
        turtle.circle(circle_radius, 206.64)
        turtle.seth(68.38)
        turtle.circle(-circle_radius, 53.1)
        turtle.seth(111.62)
        turtle.circle(-circle_radius, 69.91)
        turtle.end_fill()


    def draw010():
        turtle.begin_fill()
        turtle.circle(-circle_radius, 206.64)
        turtle.seth(111.62)
        turtle.circle(circle_radius, 53.1)
        turtle.seth(68.38)
        turtle.circle(circle_radius, 69.91)
        turtle.end_fill()


    def draw110():
        turtle.begin_fill()
        turtle.circle(circle_radius, -69.91)
        turtle.seth(164.75)
        turtle.circle(circle_radius, 30.56)
        turtle.seth(111.62)
        turtle.circle(-circle_radius, 69.91)
        turtle.end_fill()


    def draw111():
        turtle.begin_fill()
        turtle.seth(41.81)
        turtle.circle(circle_radius, 26.532)
        turtle.seth(164.75)
        turtle.circle(circle_radius, 30.56)
        turtle.seth(291.62)
        turtle.circle(circle_radius, 26.532)
        turtle.end_fill()


    def draw011():
        turtle.begin_fill()
        turtle.circle(circle_radius, 57.1)
        turtle.seth(111.62)
        turtle.circle(circle_radius, 53.1)
        turtle.seth(68.38)
        turtle.circle(circle_radius, -26.53)
        turtle.end_fill()


    def draw101():
        turtle.begin_fill()
        turtle.circle(circle_radius, -57.1)
        turtle.seth(68.38)
        turtle.circle(-circle_radius, 53.1)
        turtle.seth(291.62)
        turtle.circle(circle_radius, 26.53)
        turtle.end_fill()


    def draw001():
        turtle.begin_fill()
        turtle.circle(circle_radius, 57.1)
        turtle.seth(111.62)
        turtle.circle(circle_radius, -223.27)
        turtle.seth(344.75)
        turtle.circle(circle_radius, 57.1)
        turtle.end_fill()

    # ## Funktsioonide definitsioonid lõppevad

    given_set = raw_list[0]

    corrected_set = given_set.upper().replace('|', ' or ').replace('U', ' or ').replace('∪', ' or ') \
        .replace('&', ' and ').replace('∩', ' and ') \
        .replace('\\', ' and not ').replace('/', ' and not ') \
        .replace('X', 'A').replace('Y', 'B').replace('Z', 'C') \

    ### Täiendi eemaldamine algab
    char_list = list(corrected_set)
    element_position = 0
    for el in char_list:
        if el == "'":
            neg_pos = getNegationPos(char_list, element_position)
            if neg_pos == -1:
                popupProblem()
                return
            # Lisame negatsiooni
            char_list.insert(neg_pos, " not ")
            # Eemaldame täiendi
            del char_list[element_position + 1]
        element_position += 1
    ### Täiendi eemaldamine lõpeb

    corrected_set = ''.join(char_list)

    true_areas = getTrueEvalsAsList(corrected_set)
    if true_areas == -1:
        popupProblem()
        return


    ### Venni diagrammi joonistamine algab
    circle_radius = 100
    U_placement = (-215, 200)  # Kontrollpunkti U asukoht
    X_placement = (-5, 130)  # Kontrollpunkti X asukoht
    Y_placement = (-5, -19)  # Kontrollpunkti Y asukoht

    turtle.setup(width=540, height=450)
    turtle.pencolor('#0052CC')
    turtle.pensize(2)
    turtle.speed(0)
    turtle.title('Hulga ' + given_set + ' Venni diagramm [Kaspar Papli, 17.10.14]')

    turtle.up()
    turtle.goto(U_placement)  # Liigume kontrollpunkti U, sealt saab joonistada diagrammi osa 000
    turtle.down()

    turtle.fillcolor(getColorBasedOnValue('000'))
    draw000()

    turtle.up()
    turtle.goto(X_placement)  # Liigume kontrollpunkti X, et joonistada 3 järgnevat diagrammi osa: 100, 010 ja 110.
    turtle.down()

    turtle.fillcolor(getColorBasedOnValue('100'))
    draw100()
    turtle.fillcolor(getColorBasedOnValue('010'))
    draw010()
    turtle.fillcolor(getColorBasedOnValue('110'))
    draw110()

    turtle.up()
    turtle.goto(Y_placement)  # Liigume kontrollpunkti Y, et joonistada 4 viimast diagrammi osa: 111, 011, 101 ja 001.
    turtle.down()

    turtle.fillcolor(getColorBasedOnValue('111'))
    draw111()
    turtle.fillcolor(getColorBasedOnValue('011'))
    draw011()
    turtle.fillcolor(getColorBasedOnValue('101'))
    draw101()
    turtle.fillcolor(getColorBasedOnValue('001'))
    draw001()
    ### Venni diagrammi joonistamine lõpeb

    ### Hulkade tähiste kirjutamine algab
    turtle.up()
    turtle.goto(-180, 130)
    turtle.write('A', font=('Arial', 14, 'normal'))
    turtle.goto(155, 130)
    turtle.write('B', font=('Arial', 14, 'normal'))
    turtle.goto(85, -180)
    turtle.write('C', font=('Arial', 14, 'normal'))
    ### Hulkade tähiste kirjutamine lõpeb

    turtle.hideturtle()
    turtle.done()
